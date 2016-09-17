# coding : utf -8
import feedparser
from flask_admin.actions import action
from quokka import admin
from quokka.utils.translation import _, _l
from quokka.core.admin.models import ModelAdmin
from .models import ExternalBlogs, AggregatedTopic
from quokka.modules.posts.models import Post


class ExternalBlogsAdmin(ModelAdmin):
    roles_accepted = ('admin')
    column_filters = ('name', 'root_url')
    column_searchable_list = ('name', 'root_url', 'feeds_url')
    column_list = ('name', 'root_url', 'feeds_url', 'channel')
    form_columns = ('name', 'root_url', 'feeds_url', 'channel')

    __content_format_dict = {
        'text/plain': 'plaintext',
        'plaintext': 'plaintext',
        'text/html': 'html',
        'html': 'html',
        'text/markdown': 'markdown',
        'markdown': 'markdown',
    }

    @action('get_external_posts', _l('Get external topics'))
    def get_external_posts(self, ids):
        blogs = ExternalBlogs.objects(id__in=ids)

        for blog in blogs:
            feed = feedparser.parse(blog.feeds_url)

            for entry in feed['entries']:

                # If already exist a topic with this url
                if AggregatedTopic.objects(original_url=entry['feedburner_origlink']).first():
                    continue # Go to next iteration

                body = '{sumary}... <a href={link}>Continue reading</a>'.format(
                    sumary=entry['summary'].encode('ascii', 'ignore'),
                    link=entry['feedburner_origlink'].encode('ascii', 'ignore')
                )
                content_format = self.__content_format_dict[entry['content'][0]['type']]

                post = {
                    "title": entry['title'].encode('ascii', 'ignore'),
                    "slug": entry['title'].replace(' ', '-').encode('ascii', 'ignore'),
                    "summary": entry['summary'],
                    "content_format": content_format,
                    "body": body,
                    "channel": blog.channel,
                    "tags": [tag['term'].encode('ascii', 'ignore') for tag in entry['tags']],
                    "published": True
                }
                post, _ = Post.objects.get_or_create(**post)

                AggregatedTopic(
                    original_url=entry['feedburner_origlink'].encode('ascii', 'ignore'),
                    blog=blog,
                    post=post
                ).save()


class AggregatedTopicAdmin(ModelAdmin):
    roles_accepted = ('admin', 'editor')
    column_filters = ('date_added', 'original_url', 'blog', 'post')
    column_searchable_list = ['original_url']
    column_list = ('date_added', 'blog', 'original_url', 'post')
    form_columns = ('date_added', 'blog', 'original_url', 'post')

    def on_model_delete(self, topic):
        topic.post.delete()

# Register RSSaggregator models to quokka admin page
admin.register(ExternalBlogs, ExternalBlogsAdmin, category=_("RSSaggregator"), name=_l("External Blogs"))
admin.register(AggregatedTopic, AggregatedTopicAdmin, category=_("RSSaggregator"), name=_l("Aggregated Topics"))

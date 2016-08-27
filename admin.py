# coding : utf -8
from quokka import admin
from quokka.utils.translation import _, _l
from quokka.core.admin.models import ModelAdmin
from .models import ExternalBlogs, AggregatedTopic


class ExternalBlogsAdmin(ModelAdmin):
    roles_accepted = ('admin', 'editor')
    column_filters = ('name', 'root_url')
    column_searchable_list = ('name', 'root_url', 'feeds_url')
    column_list = ('name', 'root_url', 'feeds_url')
    form_columns = ('name', 'root_url', 'feeds_url')


class AggregatedTopicAdmin(ModelAdmin):

    roles_accepted = ('admin', 'editor')
    column_filters = ('title', 'date', 'blog')
    column_searchable_list = ('title', 'topic_url')
    column_list = ('title', 'date', 'blog', 'topic_url', 'description')
    form_columns = ('title', 'date', 'blog', 'topic_url', 'description')

admin.register(ExternalBlogs, ExternalBlogsAdmin, category=_("RSSaggregator"), name=_l("External Blogs"))
admin.register(AggregatedTopic, AggregatedTopicAdmin, category=_("RSSaggregator"), name=_l("Aggregated Topics"))

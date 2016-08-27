from quokka.core.db import db


class ExternalBlogs(db.Document):
    """
    Blogs that should be aggregated
    """
    name = db.StringField(max_length=255, required=True)
    root_url = db.StringField(default='')
    feeds_url = db.StringField(required=True)

    def __str__(self):
        return self.name


class AggregatedTopic(db.Document):
    """
    Store topics from external blogs
    """

    title = db.StringField(max_length=255, required=True)
    description = db.StringField(required=False)
    topic_url = db.StringField(required=True)
    date = db.DateTimeField(required=False)
    blog = db.ReferenceField('ExternalBlogs', required=True, reverse_delete_rule=db.CASCADE)

    def __str__(self):
        return self.title

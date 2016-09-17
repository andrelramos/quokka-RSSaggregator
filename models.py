from datetime import datetime
from quokka.core.db import db


class ExternalBlogs(db.Document):
    """
    Blogs that should be aggregated
    """
    name = db.StringField(max_length=255, required=True)
    root_url = db.StringField(default='')
    feeds_url = db.StringField(required=True)
    channel = db.ReferenceField('Channel', required=True, reverse_delete_rule=db.CASCADE)

    def __str__(self):
        return self.name


class AggregatedTopic(db.Document):
    """
    Store topics from external blogs
    """

    original_url = db.StringField(required=True)
    date_added = db.DateTimeField(default=datetime.now())
    blog = db.ReferenceField('ExternalBlogs', required=True, reverse_delete_rule=db.CASCADE)
    post = db.ReferenceField('Post', required=True, reverse_delete_rule=db.CASCADE)

    def __str__(self):
        return self.post.title

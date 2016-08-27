# coding: utf-8
from .models import AggregatedTopic


def get_external_topic(**kwargs):
    topics = AggregatedTopic.objects(**kwargs)

    return topics.order_by('date')


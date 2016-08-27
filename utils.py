# coding: utf-8
from .models import AggregatedTopic


def get_external_topic(**kwargs):
    '''
    :param kwargs: This function allows kwargs to give filter power for user
    :return: AggregatedTopic List
    '''
    topics = AggregatedTopic.objects(**kwargs)

    return topics.order_by('date')


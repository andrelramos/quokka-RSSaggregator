#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from quokka.core.templates import render_template
from .utils import get_external_topic


class AggregatedTopicsListView(MethodView):
    """
    Show a full list of external blogs
    """

    def get(self):
        return render_template('RSSaggregator/external_topics_list.html', topics=get_external_topic())

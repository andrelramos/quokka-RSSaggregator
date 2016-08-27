# coding: utf-8

from quokka.core.app import QuokkaModule
from .views import AggregatedTopicsListView

# Blueprint endpoints
module = QuokkaModule("rssaggregator", __name__, template_folder="templates")
module.add_url_rule('/aggregated-topics/', view_func=AggregatedTopicsListView.as_view('aggregated topic'))

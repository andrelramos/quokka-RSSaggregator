# coding: utf-8

from quokka.core.app import QuokkaModule
from .views import ExternalBlogListView
from .utils import get_external_blog


module = QuokkaModule("rssaggregator", __name__, template_folder="templates")
module.add_url_rule('/rssaggregator/', view_func=ExternalBlogListView.as_view('external blogs'))

#module.add_app_template_global(get_external_blog)

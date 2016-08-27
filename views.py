#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.views import MethodView
from quokka.core.templates import render_template
from .utils import get_external_blog


class ExternalBlogListView(MethodView):
    """
    Show a full list of external blogs
    """

    def get(self):
        return render_template('RSSaggregator/blogs_list.html', blogs=get_external_blog())


'''class ExternalBlogView(MethodView):
    """
    Show specific external blog
    """

    def get(self, blog_id):
        blog = get_external_blog(blog_id=blog_id)
        contents = get_author_contents(author)
        return render_template('authors/detail.html',author=author, contents=contents)'''

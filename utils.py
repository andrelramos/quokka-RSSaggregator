# coding: utf-8
from .models import ExternalBlogs


def get_external_blog(**kwargs):
    blogs = ExternalBlogs.objects(**kwargs)

    return blogs.order_by('name')


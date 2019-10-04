#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: fqy time: 19-8-24


from django.urls import path
from . import views

urlpatterns = [
    path('like_change', views.like_change, name='like_change')
]

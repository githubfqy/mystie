#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: fqy time: 19-9-4
from .forms import LoginForm


def login_modal_form(request):
    return {'login_modal_form': LoginForm()}

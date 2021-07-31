# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 01:25:00 2021

@author: Huang
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
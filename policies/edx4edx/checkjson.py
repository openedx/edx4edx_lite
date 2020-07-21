#!/usr/bin/python

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import json


def check(fn):
    print("checking %s" % fn)
    try:
        json.loads(open(fn).read())
        print("Ok")
    except Exception as err:
        raise

check('policy.json')
check('grading_policy.json')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

INTEREST_AREAS = {
    'a': 'Android Development',
    'c': 'Computer Vision',
    'i': 'Information Security',
    'm': 'Machine Learning',
    'w': 'Web Development',
}


class Mentor(models.Model):
    mentor_name = models.CharField(max_length=50)
    mentor_github = models.CharField(max_length=1000)
    mentor_interest = models.CharField(max_length=20)
    mentor_emailid = models.CharField(max_length=100)

    def __str__(self):
        return self.mentor_name

    def interest_as_list(self):
        return list(self.mentor_interest)

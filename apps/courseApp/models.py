# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        # check all fields for emptyness
        for field, value in post_data.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is reqired".format(field.replace('_', ' '))

            # check name fields for min length
            if field == "name":
                if not field in errors and len(value) < 3:
                    errors[field] = "{} field must bet at least 3 characters".format(field.replace('_', ' '))
        if len(self.filter(name=post_data['name'])) > 1:
                errors['name'] = "name already in use"
        return errors

class Course(models.Model):
      name = models.CharField(max_length=255)
      desc = models.TextField(max_length=511)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
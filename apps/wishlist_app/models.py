# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..lr_app.models import User
from django.db import models

# Create your models here.
class WishlistManager(models.Manager):
    def list_validator(self,postData, user_id):
        errors = []
        if len(postData['item']) == 0:
            errors.append('Item field cannot remain blank')
        if len(postData['item']) < 3:
            errors.append('Item name must contain at least 3 characters')
        if len(errors) > 0:
            return (False, errors)
        else:
            logged_user = User.objects.get(id=user_id)
            item = Wishlist.objects.create(item=postData['item'], contributor=logged_user)
            item.people_interested.add(logged_user)
            return (True, item)

class Wishlist(models.Model):
    item = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    contributor = models.ForeignKey(User, related_name='items_added')
    people_interested = models.ManyToManyField(User, related_name='items_wanted')
    objects = WishlistManager()
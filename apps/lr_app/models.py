# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = []
        if len(postData['name']) < 3:
            errors.append('Name must be at least 3 characters')
        if len(postData['username']) < 3:
            errors.append('Username must be at least 3 characters')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters.')
        if postData['password'] != postData['passwordcheck']:
            errors.append('Passwords do not match')  
        if len(errors) > 0:
            return (False, errors)
        else:
            password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            u = User.objects.create(name=postData['name'], username=postData['username'], password=password)
            return (True, u)  

    def login_validator(self, postData):
        errors = []
        if len(postData['username']) < 3:
            errors.append('Username must be more than 3 characters')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters')
        if len(errors) > 0:
            return (False, errors)
        else:
            u = User.objects.filter(username=postData['username'])
            if u:    
                print 'found user', 0
                if bcrypt.checkpw(postData['password'].encode(), u[0].password.encode()):
                    return (True, u[0]) 
                else:
                    errors.append('Password is incorrect')
                    return (False, errors)
            else:
                print 'no user found'
                errors.append('No user exists with this username')
                return (False, errors)

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return 'name: {}, username: {}'.format(self.name, self.username)
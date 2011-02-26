from django.db import models

class Person
    user = models.OneToOneField('auth.User', blank=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/user/%s" % (self.user)
    
class Project
    name = models.CharField(max_length=75)
    name_slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(Person)
    repo = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        return "/project/%s" % (self.name_slug)
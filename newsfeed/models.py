from django.db import models

from tagging.models import Tag
from tagging.fields import TagField

class Categories(models.Model):
    name = models.CharField(max_length=100)
    # Good view in adminka    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class News(models.Model):
    name = models.CharField(max_length=160)
    cat = models.ForeignKey('Categories')
    anounce = models.TextField(max_length=160)
    fulltext = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    img = models.ImageField(upload_to='photos/%Y/%m/%d')
    tags = TagField()
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
        
    def get_tags(self):
        return Tag.objects.get_for_object(self)
    
    def _set_tags(self, tag_list):
        Tag.objects.update_tags(self, tag_list)
    


from django.contrib import admin

from newsfeed.models import News
from newsfeed.models import Categories

admin.site.register(News)
admin.site.register(Categories)

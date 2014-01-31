# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from newsfeed.models import News
from newsfeed.models import Categories

# For using tags
from tagging.fields import TagField
from tagging.models import TaggedItem, Tag
   
    
############ Processing index page #############################################
def index(request):
    latest_news_list = News.objects.all().order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {'latest_news_list': latest_news_list})
    return HttpResponse(template.render(context))
#################################################################################   
    
    
    
############ Processing detailed news page ######################################
def detail(request, news_id=None):
    one_news = get_object_or_404(News, pk=news_id)
    return render(request, 'onenews.html', {'news': one_news})
##################################################################################      




############ Processing for news filter by category page ##########################     
def news_list(request, cat_id):
    filtered_news_list = News.objects.filter(cat=cat_id)
    return render(request, 'category.html', {'filtered_news_list': filtered_news_list})
####################################################################################  


############ Processing for news filter by tag ##################################### 
# Using python-django-tagging module https://code.google.com/p/django-tagging/
def news_bytag_name(request, tag_name):
    active_tag = get_object_or_404(Tag, name=tag_name)
    filtered_news_bytag_list = TaggedItem.objects.get_by_model(News, active_tag)
    return render(request, 'tags.html', {'filtered_news_list': filtered_news_bytag_list})
##########################################################################################    
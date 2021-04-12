from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^search/', views.search_businesses, name='search_results'),
    url(r'^business/(\d+)', views.get_business, name='business_results'),
    url(r'^new/business$', views.new_business, name='new-business'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^accounts/profile/$', views.user_profiles, name='profile'),
   
]
from django.urls import re_path, path
from blogs import views 
 
urlpatterns = [ 
    re_path(r'^api/blogs$', views.blog_list),
    re_path(r'^api/blogs/(?P<pk>[0-9]+)$', views.blog_detail),
    re_path(r'^api/blogs/published$', views.blog_list_published)
]
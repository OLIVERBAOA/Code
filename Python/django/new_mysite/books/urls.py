from django.conf.urls import url
from books import views
urlpatterns = [
    url(r'hello/^$', views.hello),        
]

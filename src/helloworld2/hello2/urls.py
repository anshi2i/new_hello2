from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.hello2, name='hello2'),

]

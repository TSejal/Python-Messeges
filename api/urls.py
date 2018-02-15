from django.conf.urls import patterns, url
from api.views import *

urlpatterns = patterns('',

    url(r'^message/14/$', question_14, name='14'),
    url(r'^message/15/$', question_15, name='15'),
    url(r'^message/16/$', question_16, name='16'),
    url(r'^message/17/$', question_17, name='17'),
    url(r'^message/18/$', question_18, name='18'),
    url(r'^message/19/$', question_19, name='19'),
    url(r'^message/20/$', question_20, name='20'),
)


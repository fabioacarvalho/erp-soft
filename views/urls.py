from views.views import *

from django.urls import path, include, re_path as url

urlpatterns = [
    path('', dashboard, name="dashboard"),
]
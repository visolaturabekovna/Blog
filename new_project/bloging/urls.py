from pydoc import importfile

from django.urls import path

from config.urls import urlpatterns
from .view import BlogListView,BlogDetailView
urlpatterns=[
    path('',BlogListView.as_view(),name='home')
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
]
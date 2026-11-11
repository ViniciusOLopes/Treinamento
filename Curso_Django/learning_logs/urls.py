from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path("topics", views.topics, name='topics'),
    path("topic/<topic_id>/", views.topic, name='topic'),
    path("add_topic", views.add_topic, name='add_topic'),
    path("add_entry/<topic_id>/", views.add_entry, name='add_entry'),

]

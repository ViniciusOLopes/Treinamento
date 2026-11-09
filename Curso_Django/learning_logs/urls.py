from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path("topics", views.topics, name='topics'),
    path("topic/<topic_id>/", views.topic, name='topic'),

]

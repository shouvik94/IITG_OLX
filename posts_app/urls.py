from django.urls import path
from posts_app import views

urlpatterns = [
    # path(r'^$',)
    path('', views.IndexView.as_view(), name='index'),
]
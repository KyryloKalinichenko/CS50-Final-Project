from django.urls import path
# from . import views
from .views import Blogline, DetailPost, DetailProgramme, Home, Sources, About

urlpatterns = [
    # path('', views.home, name='home'),
    path('', Home, name='home'),
    path('articles', Blogline.as_view(), name='articles'),
    path('sources', Sources.as_view(), name='sources'),
    path('about', About, name='about'),
    path('article/<int:pk>', DetailPost.as_view(), name='detail')
]
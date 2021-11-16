from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
# from . import views
from .views import Blogline, DetailPost, DetailProgramme, Home, Sources, About


urlpatterns = [
    # path('', views.home, name='home'),
    path('', Home, name='home'),
    path('articles', Blogline.as_view(), name='articles'),
    path('sources', Sources.as_view(), name='sources'),
    path('about', About, name='about'),
    path('article/<int:pk>', DetailPost.as_view(), name='detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     # static files (images, css, javascript, etc.)
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
#         'document_root': settings.MEDIA_ROOT}))
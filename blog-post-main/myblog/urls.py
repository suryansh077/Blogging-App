from django.urls import path
from.import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home),
    path('article',views.article),
    path('search',views.search),
    path('edit/<str:title>',views.edit),
    path('update/<str:title>',views.update),
    path('',views.login),
    path('user',views.user)
       
]+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)

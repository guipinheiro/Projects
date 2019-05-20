from django.urls import path
from . import views

#instead of creating all URLs inside our website urls.py file,
#we will create specific URLs for each app
#and them we will import them on website/urls.py

urlpatterns = [
	# /music/
    path('', views.index, name='index'),

    # music/71/
    path('<int:album_id>/', views.detail, name='detail'),
]

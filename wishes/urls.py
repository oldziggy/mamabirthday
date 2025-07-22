from django.urls import path

from . import views

app_name = "wishes"
urlpatterns = [

    path('', views.index, name='index'),
    path('wishes/', views.detail, name='detail_no_id'),
    path('wishes/<int:wish_id>/', views.detail, name='detail'),

]

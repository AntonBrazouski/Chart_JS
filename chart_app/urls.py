from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('november', views.november, name='november' ),
    path('november/week01', views.nov_week_01, name='nov_week_01')

]

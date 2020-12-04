from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('november', views.november, name='november' ),
    path('november/week01', views.nov_week_01, name='nov_week_01'),
    path('chart_setup', views.chart_setup, name='chart_setup' ),
    path('chart_custom', views.chart_custom, {'header': 'custom'}, name='chart_custom')

]

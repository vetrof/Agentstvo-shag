from django.urls import path

from homes.views import list_views, detail_view

app_name = 'homes'

urlpatterns = [
    path('', list_views, name='main_page'),
    path('home/<int:pk>', detail_view, name='detail_page'),
]
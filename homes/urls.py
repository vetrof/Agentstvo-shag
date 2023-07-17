from django.urls import path

from homes.views import list_views, detail_view

urlpatterns = [
    path('', list_views),
    path('home/<int:pk>', detail_view, name='detail_page'),
]
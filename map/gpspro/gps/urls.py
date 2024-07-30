from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    
    path('assets/',views.list_assets,name='list_assets'),
    path('assets/id=<str:myid>/',views.asset_by_id,name='asset_by_id'),
    path('assets/type=<str:myid>/',views.asset_by_type,name='asset_by_type'),
    path('assets/<str:myid>/',views.asset_by_timezone,name='asset_timezone'),
    
]

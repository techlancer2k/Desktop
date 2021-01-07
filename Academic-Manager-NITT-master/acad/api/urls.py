from django.urls import path,include
from .views import home

urlpatterns = [
    path('',home,name='api.home'),
    path('customAdmin/',include('api.customAdmin.urls')),
    path('load/', include('api.uploadApp.urls')),
    
]

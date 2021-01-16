from django.urls import path, include 

urlpatterns = [
    path('app_ex/', include("app_ex.urls","inicio")),
]
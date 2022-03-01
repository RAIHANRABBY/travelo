
from django.urls import path
from .views import log_reg,logout_view

urlpatterns = [
    path('register/',log_reg),
    path('logout/',logout_view),
]

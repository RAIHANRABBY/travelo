
from django.urls import path
from .views import registration_view,\
                    logout_view,\
    login_view,\
    home,\
    about_view,\
    contact_view,gallery_view,\
    places_info,spots_view,bus_ticket,\
    train_ticket,flight_ticket

urlpatterns = [
    path('register/',registration_view,name="register"),
    path('logout/',logout_view,name="logout"),
    path('login/',login_view,name="login"),

    path('',home,name='home_page'),
    path('home/',home,name='home_page'),
    path('about/',about_view,name='about'),
    path('contact/',contact_view,name='contact'),
    path('gallery/',gallery_view,name='gallery'),
    path('places/<int:id>/',places_info),
    path('places/spots/<int:id>/',spots_view),
    path('bus/',bus_ticket),
    path('train/',train_ticket),
    path('flight/',flight_ticket),


]

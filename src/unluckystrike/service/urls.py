from django.urls import path
from . import views


urlpatterns = [
    path('', views.service_index, name="service_index"),
    path('open-webcam-test', views.open_webcam_test, name="open_webcam_test"),
    path('random-access-music', views.random_access_music, name="random_access_music"),
    path('fishingram', views.Fishingram.as_view(), name="fishingram"),
    path('<service>', views.service_detail, name="service_detail"),
]
from django.conf.urls import url, include
from .views import cfhaz, crhaz, cmast, cchemcam, cmahli, cmardi, cnavcam
from django.urls import path

urlpatterns = [
    path('curiosity_front_hazard_avoidance_camera/', cfhaz, name='C_FHAZ'),
    path('curiosity_rear_hazard_avoidance_camera/', crhaz, name='C_RHAZ'),
    path('curiosity_mast_camera/', cmast, name='C_MAST'),
    path('curiosity_CHEMCAM/', cchemcam, name='C_CHEMCAM'),
    path('curiosity_MAHLI/', cmahli, name='C_MAHLI'),
    path('curiosity_MARDI/', cmardi, name='C_MARDI'),
    path('curiosity_NAVCAM/', cnavcam, name='C_NAVCAM'),
]

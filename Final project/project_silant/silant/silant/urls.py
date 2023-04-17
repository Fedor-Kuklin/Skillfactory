"""silant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urlss import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urlss'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from polls.api import *

router = routers.DefaultRouter()
router.register(r'car', CarViewset)
router.register(r'maintenance', MaintenanceViewset)
router.register(r'claim', ClaimViewset)
router.register(r'model_technics', ModelTechnicsViewset)
router.register(r'model_motor', ModelMotorViewset)
router.register(r'model_transmissions', ModelTransmissionsViewset)
router.register(r'model_driving_bridge', ModelDrivingBridgeViewset)
router.register(r'model_controlled_bridge', ModelControlledBridgeViewset)
router.register(r'type_maintenance', TypeMaintenanceViewset)
router.register(r'type_fault', TypeFaultViewset)
router.register(r'recovery_method', RecoveryMethodViewset)
router.register(r'user', UserViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]

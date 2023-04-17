from django.urls import path, include

from .views import (
    LoginUser,
    logout_user,
    SearchAll,
    SearchAllBlank,
    ReferencesList,
)

urlpatterns = [
    path('car_all', SearchAll.as_view(), name='car_all'),
    path('', SearchAllBlank.as_view(), name='car_all_blank'),
    path('user/', include('polls.urlss.urlsUser')),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('car/', include('polls.urlss.urlsCar')),
    path('maintenance/', include('polls.urlss.urlsMaintenance')),
    path('claim/', include('polls.urlss.urlsClaim')),
    path('model_technics/', include('polls.urlss.urlsModelTechnics')),
    path('model_motor/', include('polls.urlss.urlsModelMotor')),
    path('model_transmissions/', include('polls.urlss.urlsModelTransmissions')),
    path('model_driving_bridge/', include('polls.urlss.urlsModelDrivingBridge')),
    path('model_controlled_bridge/', include('polls.urlss.urlsModelControlledBridge')),
    path('type_maintenance/', include('polls.urlss.urlsTypeMaintenance')),
    path('type_fault/', include('polls.urlss.urlsTypeFault')),
    path('recovery_method/', include('polls.urlss.urlsRecoveryMethod')),
    path('references/', ReferencesList.as_view(), name='references')
    ]

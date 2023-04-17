from django.urls import path

from polls.views import ModelTechnicsUpdateView, \
    ModelTechnicsDeleteView, ModelTechnicsDetail, ModelTechnicsCreateView, ModelTechnicsList

urlpatterns = [
    path('model_technics/', ModelTechnicsList.as_view(), name='model_technics'),
    path('create_model_technics/', ModelTechnicsCreateView.as_view(), name='model_technics_create'),
    path('update_model_technics/<int:pk>', ModelTechnicsUpdateView.as_view(), name='model_technics_update'),
    path('delete_model_technics/<int:pk>', ModelTechnicsDeleteView.as_view(), name='model_technics_delete'),
    path('model_technics_one/<int:pk>', ModelTechnicsDetail.as_view(), name='model_technics_detail'),
    ]
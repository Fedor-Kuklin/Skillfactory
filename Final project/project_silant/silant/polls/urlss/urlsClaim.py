from django.urls import path

from polls.views import SearchClaim, ClaimDetail, ClaimCreateView, ClaimUpdateView, ClaimDeleteView


urlpatterns = [
    path('search_claim/', SearchClaim.as_view(), name='claim'),
    path('claim_one/<int:pk>', ClaimDetail.as_view(), name='claim_detail'),
    path('create_claim/', ClaimCreateView.as_view(), name='claim_create'),
    path('update_claim/<int:pk>', ClaimUpdateView.as_view(), name='claim_update'),
    path('delete_claim/<int:pk>', ClaimDeleteView.as_view(), name='claim_delete'),
    ]
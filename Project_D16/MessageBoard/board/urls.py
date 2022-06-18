from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', AdList.as_view(), name='ad'),
    path('<int:pk>', AdDetail.as_view(), name='one_ad'),
    path('comment/', CommentList.as_view(), name='comment'),
    path('create/', AdCreate.as_view(), name='ad_create'),
    path('update/<int:pk>', AdUpdate.as_view(), name='ad_update'),
    path('search/', AdSearch.as_view(), name='ad_search'),
    path('comment/', CommentList.as_view(), name='comment'),
    path('comment_accept/<int:pk>', CommentAccept.as_view(), name='accept'),
    path('comment_remove/<int:pk>', CommentRemove.as_view(), name='remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
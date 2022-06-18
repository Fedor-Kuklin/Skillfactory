from django_filters import FilterSet

from .models import Ad, Comment


class AdFilter(FilterSet):
    class Meta:
        model = Ad
        fields = ('author', 'categoryType',)


class CommentFilter(FilterSet):
    class Meta:
        model = Comment
        fields = ('commentAd_id',)
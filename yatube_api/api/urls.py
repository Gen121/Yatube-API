from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
urlpatterns = [path('v1/', include(urlpatterns))]

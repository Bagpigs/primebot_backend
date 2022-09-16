from django.urls import path
from rest_framework.routers import SimpleRouter

from app_api.modules.teams.views import TeamViewSet, api_root, MatchViewSet

router = SimpleRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'matches', MatchViewSet, basename='match')

urlpatterns = [
    path('', api_root)
]

urlpatterns += router.urls

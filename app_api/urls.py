from django.urls import path, include

urlpatterns = [
    path('settings/', include("app_api.modules.team_settings.urls"), ),
    path('status/', include("app_api.modules.status.urls"), ),
    path('v1/', include("app_api.modules.teams.urls"), ),
]


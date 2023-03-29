from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path("health_check/", views.health_check, name="health_check"),
    path("admin/", admin.site.urls),
    path("project/", include("api.project.urls")),
]

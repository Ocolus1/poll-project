from django.contrib import admin
from django.urls import path

from poll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("vote/<poll_id>/", views.vote, name="vote"),
    path("results/<poll_id>/", views.results, name="results"),
]

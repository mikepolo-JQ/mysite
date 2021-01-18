from django.urls import path

from applications.main.views import view_main

urlpatterns = [
    path("", view_main, name="main"),
]

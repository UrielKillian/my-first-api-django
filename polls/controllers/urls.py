from django.urls import path
import polls.views.views as poll_controller

urlpatterns = [
    path("", poll_controller.index, name="index"),
]
from django.urls import path
import polls.views.views as pollController

urlpatterns = [
    path("", pollController.index, name="index"),
]
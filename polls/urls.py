from django.urls import path
import polls.views as poll_controller

app_name = "polls"
urlpatterns = [
    path("", poll_controller.index, name="index"),
    path("<int:question_id>/", poll_controller.detail, name="detail"),
    path("<int:question_id>/results/", poll_controller.results, name="results"),
    path("<int:question_id>/vote/", poll_controller.vote, name="vote"),
]
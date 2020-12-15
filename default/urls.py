from django.urls import path
from .views import

urlpatterns = [
    # path('poll/',views.poll_list),
    path('poll/',PollList.as_view()),
    path('poll/int:pk>/', PollDetail.as_view()),
    path('option/<int:oid>/',PollVote.as_view()),
    path('poll/create/',Pollcreate.as_view()),
    path('poll/<int:pk>/edit/',PollEdit.as_view()),
    path('poll/<int:pk>/delete/',PollDelete.as_view()),
    path('poll/<int:pk>/add/',OptionAdd.as_view()),
    path('opyion/<int:pk>/edit/',OptionEdit.as_view()),
    path('option/<int:pk>/delete/',OptionDelete.as_view())
    
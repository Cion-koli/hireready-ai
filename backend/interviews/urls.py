from django.urls import path
from .views import (
    InterviewListCreateView,
    InterviewDetailView,
    InterviewStartResumeView,
    NextQuestionView,
    SubmitAnswerView,
    EndInterviewEarlyView
)
from evaluations.views import CompleteInterviewView

urlpatterns = [
    path('', InterviewListCreateView.as_view(), name='interview_list_create'),
    path('<int:pk>/', InterviewDetailView.as_view(), name='interview_detail'),
    path('<int:pk>/start/', InterviewStartResumeView.as_view(), name='interview_start'),
    path('<int:pk>/questions/next/', NextQuestionView.as_view(), name='interview_next_question'),
    path('<int:pk>/answers/', SubmitAnswerView.as_view(), name='interview_submit_answer'),
    path('<int:pk>/end/', EndInterviewEarlyView.as_view(), name='interview_end_early'),
    path('<int:pk>/complete/', CompleteInterviewView.as_view(), name='interview_complete'),
]

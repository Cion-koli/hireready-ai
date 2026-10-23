from django.urls import path
from .views import InterviewReportView, UserReportsListView, DashboardStatsView

urlpatterns = [
    path('', UserReportsListView.as_view(), name='user_reports_list'),
    path('<int:pk>/', InterviewReportView.as_view(), name='report_detail'),
    path('stats/dashboard/', DashboardStatsView.as_view(), name='dashboard_stats'),
]

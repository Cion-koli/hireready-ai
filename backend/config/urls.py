from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from evaluations.views import DashboardStatsView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth endpoints
    path('api/auth/', include('accounts.urls')),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Interview session endpoints
    path('api/interviews/', include('interviews.urls')),
    
    # Reports & Stats endpoints
    path('api/reports/', include('evaluations.urls')),
    path('api/stats/dashboard/', DashboardStatsView.as_view(), name='root_dashboard_stats'),
]

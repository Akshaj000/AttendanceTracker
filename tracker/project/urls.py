from django.contrib import admin
from django.urls import path

from tracker.views import DeviceLogCreateView
from session.views import CreateSession, RecordAttendance
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/device/log/', DeviceLogCreateView.as_view(), name='device-log'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/session/create/', CreateSession.as_view(), name='create-session'),
    path('api/session/record/', RecordAttendance.as_view(), name='record-attendance'),
]

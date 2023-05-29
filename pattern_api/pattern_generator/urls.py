from django.urls import path, include
from .views import PatternAPIViewBase64, TestPatternAPIView

app_name = 'pattern_generator'

urlpatterns = [
    path('api/v1/test/', TestPatternAPIView.as_view()),
    path('api/v1/make_pattern_base64', PatternAPIViewBase64.as_view()),
]

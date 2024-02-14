from django.urls import path
from .views import AlaCreateApiView,AlaListApiView


urlpatterns = [
    path('/alacreate',AlaCreateApiView.as_view()),
    path('/alalist',AlaListApiView.as_view())
]
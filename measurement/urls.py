from django.urls import path
from .views import SensorListCreateView, SensorCreateView, SensorListView, SensorUpdateView, MeasurementCreateView, MeasurementListView

urlpatterns = [
    path ('home/', SensorListCreateView.as_view()),
    path ('sensor/create/', SensorCreateView.as_view()),
    path ('measurement/create/', MeasurementCreateView.as_view()),
    path ('sensor/', SensorListView.as_view()),
    path ('sensor/<pk>/', SensorUpdateView.as_view()),
    path ('measurement/<pk>/', MeasurementListView.as_view()),
]

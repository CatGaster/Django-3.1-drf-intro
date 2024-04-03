from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from measurement.serializers import SensorSerializer, MeasurementSerializer
from measurement.models import Sensor, Measurement


class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorCreateView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorListView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class MeasurementListView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
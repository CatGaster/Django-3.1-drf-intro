from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    
class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.temperature}"

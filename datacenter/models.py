from django.db import models

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class Cable(models.Model):
    nep = models.PositiveBigIntegerField(default=0)
    ponta_a = models.CharField(max_length=50)
    ponta_b = models.CharField(max_length=50)
    group = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    device = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'NEP : {self.nep} | Ponta A : {self.ponta_a} | Ponta B: {self.ponta_b}'

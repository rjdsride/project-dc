from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=50, null=False)
    vendor = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.name

class Group(models.Model):
    group_dev = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.group_dev

class Cable(models.Model):
    nep = models.PositiveBigIntegerField(default=0, unique=True)
    dev_a = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="dev_a"
    )
    ponta_a = models.CharField(max_length=50)
    dev_b = models.ForeignKey(
        Device,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="dev_b"
    )
    ponta_b = models.CharField(max_length=50)
    group_dev = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name= 'Group',
    )
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return f'NEP: {self.nep} | Ponta A: {self.ponta_a} | Ponta B: {self.ponta_b}'

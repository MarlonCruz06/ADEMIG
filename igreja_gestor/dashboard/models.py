from django.db import models

class DashboardModel(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
    campo3 = models.DateField()

    def __str__(self):
        return self.campo1

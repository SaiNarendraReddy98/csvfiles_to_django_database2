from django.db import models

# Create your models here.
class EmployeeBusiness(models.Model):
    Series_reference = models.CharField(max_length=100)
    Period = models.DecimalField(max_digits=10,decimal_places=3)
    Data_value = models.CharField(max_length=100)
    Suppressed = models.CharField(max_length=100,null=True,blank=True)
    Status = models.CharField(max_length=100)
    Units = models.CharField(max_length=100)
    Magnitude = models.IntegerField()
    Subject = models.CharField(max_length=100)
    Group = models.CharField(max_length=100)
    Series_title_1 = models.CharField(max_length=100)
    Series_title_2 = models.CharField(max_length=100)
    Series_title_3 = models.CharField(max_length=100)
    Series_title_4 = models.CharField(max_length=100)
    Series_title_5 = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.Subject




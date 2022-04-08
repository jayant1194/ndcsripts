from django.db import models

# Create your models here.
class bike(models.Model):
    SERVICE_CHOICE= [('p','platinum'),('g','gold')]
    bike_model=models.CharField(max_length=12)
    bike_number = models.CharField(max_length=12)
    sevice_type= models.CharField(choices=SERVICE_CHOICE,max_length=1)
    notes=models.CharField(max_length=12)
    service_charge= models.CharField(max_length=12,blank=True)
    submission_date=models.DateTimeField()
    servicing=models.ManyToManyField('service',blank=True)



class service(models.Model):
    name=models.CharField(max_length=12)


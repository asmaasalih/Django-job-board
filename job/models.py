from django.db import models


# Create your models here.
class Job(models.Model):

    JOB_TYPE = (
    ('Full time','Full time'),
    ('Part time','Part time')
   ) 

    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE, default='Full time')
    describtion = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)

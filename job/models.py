from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def image_upload(instance,filename):
    image_name , extension = filename.split('.')
    return 'media/jobs/%s%s' %(instance.id,extension)


class Job(models.Model):
    JOB_TYPE = (
    ('Full time','Full time'),
    ('Part time','Part time')
   ) 

    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE, default='Full time')
    describtion = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to=image_upload)

    def __str__(self):
        return self.title
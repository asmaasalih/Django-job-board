from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

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
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
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
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)


    def __str__(self):
        return self.title

class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)     
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    website = models.URLField()  
    cv = models.FileField(upload_to='apply/', max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    cover_letter = models.TextField(max_length=500)

    def __str__(self):
        return self.name

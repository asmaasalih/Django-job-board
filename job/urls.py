from django.urls import path
from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.job_detail,name='job_detail'),
    
    #api urls
    path('api/jobs',api.jobs_api,name='jobs_api'),
    path('api/jobs/<int:id>',api.job_detail_api,name='job_detail_api'),
    path('api/joblist/', api.JobList.as_view()),
    path('api/joblist/<int:pk>/', api.JobDetail.as_view()),
]

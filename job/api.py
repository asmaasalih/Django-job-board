from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Job
from .serializers import JobSerializer
from rest_framework import generics


@api_view(['GET'])
def jobs_api(request):
    all_jobs = Job.objects.all()
    serializer = JobSerializer(all_jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = Job.objects.get(id=id)
    serializer = JobSerializer(job_detail)
    return Response(serializer.data)

#api using class based views
class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
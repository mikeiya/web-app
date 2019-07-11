from django.shortcuts import render
from .models import my_job

# Create your views here.
def home(request):
    jobs = my_job.objects
    return render(request,'my_jobs/home.html',{'jobs':jobs})

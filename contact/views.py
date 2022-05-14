from django.shortcuts import render, redirect
from .models import Info
from django.core.mail import send_mail
from django.conf import settings


def send_message(request):
    my_info = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
        )
        return redirect(reverse('jobs:job_list'))    

    return render(request,'contact/contact.html',{'my_info':my_info})
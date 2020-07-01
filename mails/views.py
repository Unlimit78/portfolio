from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from rest_framework import serializers
from rest_framework import viewsets,permissions
from django.core.files.base import ContentFile
# Create your views here.
from .models import  Attachments,Mail

def index(request):
    if request.method =='POST':

        name = request.POST.get('name')
        e_mail = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = str(e_mail)+'\n'+str(message)
        files = request.FILES.getlist('file')

        send_mail = EmailMessage(subject, data, e_mail, ['fderg12345@gmail.com'])
        mail = Mail.objects.create(name=name, subject=subject, email=e_mail, message=message)
        print(files)
        for f in files:
            data = f.read()
            send_mail.attach(f.name,data)
            Attachments.objects.create(file=f,location=mail)
        send_mail.send()


    return render(request,'index.html')




class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model =Attachments
        fields = '__all__'

class FileViewSet(viewsets.ModelViewSet):
    queryset = Attachments.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FileSerializer
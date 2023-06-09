from django.shortcuts import render
from django.views import View
import requests
import random
from django.core.mail import send_mail
from django.http import HttpResponse
from project12.settings import EMAIL_HOST_USER
from .forms import RegForm

# Create your views here.
class Home(View):
    def get(self,request):
        rf=RegForm()
        con_dic={'rf':rf}
        return render(request,'home.html',context=con_dic)
class Reg(View):
    def post(self,request):
        otp=str(random.randint(10000000,99999999))
        print(otp)
        mobno=request.POST["Mobno"]
        emailid=request.POST["Email"]
        resp = requests.post('https://textbelt.com/text', {
            'phone': mobno,
            'message': otp,
            'key': 'deb651692eabe6a8c4dc2bf4c540d840302c14beufATt5cvEXUzaN5EDcNM17S9q',
        })
        print(resp.json())
        send_mail("otp for registration",otp,EMAIL_HOST_USER,[emailid],fail_silently=True)
        rf=RegForm(request.POST)
        if rf.is_valid():
            rf.save()
            return HttpResponse("reg success")

# Create your views here.

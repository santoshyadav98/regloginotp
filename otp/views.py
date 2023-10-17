from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
import requests
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from reglogin.settings import EMAIL_HOST_USER
from .forms import RegForm
from otp.models import Reg
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class reginput(View):    
    def get(self,request):
        r_f={'regform':RegForm()}
        return render(request,'reginput.html',r_f)
    
class Reg(View):
    def post(self,request):
        rf=RegForm(request.POST)
        rf.save()
        if rf.is_valid():
            otp=str(random.randint(10000000,99999999))
            request.session["deatils"]=request.POST
            request.session["otp"]=otp
            print(otp)
            mobno=request.POST["MobileNo"]
            emailid=request.POST["Emailid"]
            resp = requests.post('https://textbelt.com/text', {
                'phone': mobno,
                'message': otp,
                'key': 'deb651692eabe6a8c4dc2bf4c540d840302c14beufATt5cvEXUzaN5EDcNM17S9q',
            })
        print(resp.json())
        subject='welcome to santosh dout'
        email_user=otp
        from_mail=settings.EMAIL_HOST_USER
        to_list=[request.POST['Emailid']]
        send_mail(subject,email_user,from_mail,to_list,fail_silently=True)
        return render(request,'otpinput.html')

class otpver(View):
    def post(self,request):
        Sotp=request.session['otp']
        Rotp=request.POST['t1']
        if Sotp==Rotp:
            rmf=RegForm(request.session['deatils'])
            return HttpResponse("registration sucess")
        else:
            return HttpResponse('Registration failed')
        
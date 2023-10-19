import random
import requests

from django.shortcuts import render
from django.views import View
from .forms import UserForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html',{'form': UserForm()})
class Regview(View):
    def post(self,request):
        form = UserForm(request.POST)
        if form.is_valid():
            otp = str(random.randint(1000,9999))
            request.session['details'] = request.POST
            request.session['otp'] = otp

            resp = requests.post('https://textbelt.com/text', {
                'phone': '+91'+str(request.POST['mobile']),
                'message': otp,
                'key': 'textbelt',
            })
            print(resp.json())
            print(otp)
            subject = 'Hi! User Did You get OTP?'
            message = 'Your OTP is ' + otp
            form_email = request.POST['email']
            print(form_email)
            email = [request.POST['email']]
            send_mail(subject,message,form_email,email)
            return render(request,'otp.html')
class OTPView(View):
    def post(self,request):
        sotp = request.session['otp']
        rotp = request.POST['t1']
        if sotp == rotp:
            rmf = UserForm(request.session['details'])
            rmf.save()

            return HttpResponse(f'''<center> <h1 style="color: red"> OTP Matched </h1> </center>''')
        else:
            return HttpResponse(f"""<center> <h1 style="color: red"> OTP Not Matched </h1> </center>""")




from django.shortcuts import render
from .models import Register
import datetime
# Create your views here.
def input(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email = request.POST['Email']
        Mobile = request.POST['Mobile']
        date = datetime.datetime.now()
        s=Register(Name=Name,Email=Email,Mobile=Mobile,date_and_time=date)
        s.save()
        dict={'Time':date}

        return render(request,'base.html',dict)
    return render(request, 'base.html')


def display(request):
    r=Register.objects.all()
    f={'data':r}
    return render(request,'base2.html',f)

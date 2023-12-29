from django.shortcuts import render
from .serilizers import Userserilizer
from .models import UserApp

# Create your views here.
count=0
def pages(request):
    global count
    if count==0:
        if request.method=="POST":
            username=request.POST['username']
            password = request.POST['password']
            s=UserApp(username=username,password=password)
            s.save()
            count+=1
            return render(request,'sample2.html')
        return render(request,'sample1.html')
    if count==1:
        if request.method == "POST":
            username1=request.POST.get('username')
            password1=request.POST.get('password')
            try:
                user=UserApp.objects.get(username=username1)
                serilizer=Userserilizer(user)
                if password1 == serilizer.data['password']:
                    count+=1
                    return render(request,'sample3.html')
                return render(request,'sample2.html')
            except:
                return render(request,'sample2.html')
        return render(request,'sample2.html')
    if count==2:
        if request.method == "POST":
            count=0
            return render(request,'sample1.html')
        return render(request,'sample2.html')
    return render(request,'sample1.html')




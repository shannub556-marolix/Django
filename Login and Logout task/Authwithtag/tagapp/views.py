from django.shortcuts import render
from .models import Tag
from .serilizer import Userserilizer
# Create your views here.
def register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            s = Tag(username=username, password=password)
            s.save()
        except:
            return render(request, 'sample1.html')
        return render(request, 'sample11.html')
    return render(request, 'sample1.html')

def login(request):
    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        try:
            user = Tag.objects.get(username=username1)
            serilizer = Userserilizer(user)
            if password1 == serilizer.data['password']:
                return render(request, 'sample3.html')
            return render(request, 'sample2.html')
        except:
            return render(request, 'sample2.html')
    return render(request, 'sample2.html')

def home(request):
    return render(request, 'sample4.html')
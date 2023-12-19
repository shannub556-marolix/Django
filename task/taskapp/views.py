from django.shortcuts import render
from .models import Employee

# Create your views here.
def taskapp(request):
    if request.method=='POST':
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Email=request.POST['Email']
        Dob=request.POST['Dob']
        Gender=request.POST['Gender']
        Mobile=request.POST['Mobile']
        Domain=request.POST['Domain']
        Company=request.POST['Company']
        Salary=request.POST['Salary']
        e1=Employee(Fname=Fname,Lname=Lname,Email=Email,Dob=Dob,Gender=Gender,Mobile=Mobile,Domain=Domain,Company=Company,Salary=Salary)
        e1.save()
        e2 = Employee.objects.all()
        return render(request, 'index.html', {'e3': e2})

    return render(request, 'index.html')

def details(request):
    e2 = Employee.objects.all()
    return render(request, 'index2.html', {'e3': e2})



from django.shortcuts import render,redirect
from app.models import Register
from app.forms import RegisterForm
from django.contrib.auth import authenticate

def login(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        pwd=request.POST.get('Password')
        print(name)
        print(pwd)
        try:
            user=authenticate(request,username=name,password=pwd)
            print(user)
            if user is not None:
                return redirect('register_read')
            else:
                return redirect ('login')

        except:
            pass  
    return render(request,'login.html')

def register_create(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_read')
    return render(request, 'create.html', {'form': form})

def register_read(request):
    read = Register.objects.all()
    return render(request, 'read.html', {'read': read})

def register_update(request,pk):
    forms=Register.objects.get(id=pk)
    form = RegisterForm(request.POST or None, instance =forms)
    if form.is_valid():
         form.save()
         return redirect('register_read')
        
    return render(request, 'update.html', {'form' : form})

def register_delete(request,pk):
    form=Register.objects.get(id=pk)
    form.delete()
    return redirect('register_read')   





# Create your views here.

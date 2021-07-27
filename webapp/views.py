from django.db.models import query
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponse,redirect
from datetime import datetime
from django.contrib import messages
from .forms import ImageForm
from .models import Image
from django.contrib.auth.models import User ,auth


def uploadimg(request):
    if request.user.is_authenticated:   
        if request.method == 'POST':
            form = ImageForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
        form = ImageForm() 
        img = Image.objects.all()
        if 'term' in request.GET:
            q = request.GET['term']
            data = User.objects.filter(first_name=q)
        else:
            data = User.objects.all()

        return render(request, 'uploadimg.html',{'img':img,'form':form,'data':data})
    else:
        return HttpResponseRedirect('/login')

def register(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['mobileno']
        password1 = request.POST['password1']
        confirm_password = request.POST['password2']

        if password1 == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username alrady taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email alredy register')
                return render(request,'register')
            
            else:
                user = User.objects.create_user(username=username,first_name=name,email=email,password=password1)
                user.save()
                
                messages.success(request,'Register Successfully goto Login !')
                return render(request,'login.html')
        
        else:
            messages.info(request,'password not  matching ...')
            return render(request,'register.html')
    else:
        return render(request,'register.html')

def index(request):
    if request.user.is_authenticated:   
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/login')



def autosuggest(request):
    print(request.GET)
    query_original = request.GET.get('term')
    queryset = User.objects.filter(first_name=query_original)
    mylist = []
    mylist += [x.first_name for x in queryset]

    return JsonResponse(mylist,safe=False)

def loginuser(request):

    if request.method =="POST":
        username = request.POST['mobileno']
        password1 = request.POST['password1']


        user = auth.authenticate(username=username,password=password1)

        if user is not None:
            auth.login(request,user)

            return render(request,'index.html')
        else:
            messages.info(request,'Invailid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
   
    return render(request, 'login.html')


def logoutuser(request):
    auth.logout(request)
    messages.success(request,'logout Successfully!')

    return render(request, 'login.html')

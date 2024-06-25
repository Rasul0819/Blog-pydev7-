from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from . import models


def homepage(request):
    posts = models.Blog.objects.all()
    return render(request,'home.html',{'posts':posts})

def post_detail(request,id):
    post = get_object_or_404(models.Blog,id=id)
    return render(request,'post_detail.html',{'post':post})



def registration(reqeust):
    if reqeust.method =='POST':
        form = forms.RegistrationForm(reqeust.POST)
        if form.is_valid():
            user = form.save()
            login(reqeust,user)
            return redirect('homepage')
    else:
        form = forms.RegistrationForm()
    return render(reqeust,'registration.html',{'form':form})
    
def log_in(request):
    if request.method =='POST':
        form = forms.AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('homepage')
    else:
        form = forms.AuthenticationForm()
    return render(request,'log_in.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('homepage')


def create_post(request):
    if request.method =='POST':
        form = forms.BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form=forms.BlogForm()
    return render(request,'create_post.html',{'form':form})


def update_post(request,id):
    model = models.Blog.objects.get(id=id)
    form = forms.BlogForm(request.POST or None , request.FILES,instance=model)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request,'update.html',{'form':form})

def delete_post(request,id):
    model = models.Blog.objects.get(id=id)
    if request.method=='POST':
        model.delete()
        return redirect('homepage')
    return render(request,'delete.html',{'model':model})





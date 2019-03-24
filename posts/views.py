from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.urls import reverse
from .forms import PostForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from .forms import SignUpForm,UserEditForm
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def index(request):
    return render(request,'post/index.html')


def home(request):
    instance = Post.objects.all().order_by('-timestamp')
    query = request.GET.get('q')
    if query:
        instance = Post.objects.filter(title__icontains=query)
    paginator = Paginator(instance, 10)
    page = request.GET.get('page')
    instance = paginator.get_page(page)
    return render(request,'post/home.html',{'instance':instance})


def detail(request,instance_id):
    instance = Post.objects.get(id=instance_id)
    return render(request,'post/detail.html',{'instance':instance})


def create(request):
    form = PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"The post was successfully created")
        return HttpResponseRedirect('/home')


    return render(request,'post/create.html',{'form':form})


def edit(request,instance_id):
    instance = Post.objects.get(id=instance_id)
    if instance.user == request.user:
        form = PostForm(request.POST or None,request.FILES or None,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse('detail',args=(instance_id,)))
    else:
        messages.error(request,"You are not the creator of this post")
        return HttpResponseRedirect(reverse('detail',args=(instance_id,)))

    return render(request,'post/edit.html',{'instance':instance,'form':form})




def delete(request,instance_id):
    instance = Post.objects.get(id=instance_id)
    if instance.user == request.user:
        instance.delete()
        messages.success(request,"The post was deleted successfully")

        return HttpResponseRedirect('/home/')
    else:
        messages.error(request,"You are not the creator of this post")
        return redirect('/home/')

def likes(request,instance_id):
    obj = get_object_or_404(Post,id=instance_id)
    user = request.user
    if user.is_authenticated:
        if user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)
    return  HttpResponseRedirect(reverse('detail', args=(instance_id,)))




def signup(request):
    if request.method=="POST":
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            if user is not None and user.is_active:
                login(request,user)
                return HttpResponseRedirect('/home/')
    else:
        form = SignUpForm()
    return render(request,'post/signup.html',{'form':form})

def logoutv(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request):
    user = request.user
    return render(request,'post/profile.html',{'user':user})

def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST or None , instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserEditForm(instance=user)
    return render(request,'post/edit_profile.html',{'user':user,'form':form})

def change_password(request):
    if request.method == "POST":

        form = PasswordChangeForm(data = request.POST , user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'The password was changed successfully')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request,'post/passwordchange.html',{'form':form})

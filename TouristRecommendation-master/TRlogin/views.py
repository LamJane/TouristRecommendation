from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from TRsale import models
from TRlogin import models
from TRlogin.forms import RegisterForm, UserForm


def shouye(request):
    return render(request,'shouye.html')


def login(request):
    if request.session.get('is_login',None):
        return redirect('comment')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    request.session['user_tags'] = user.tags
                    return redirect('comment')
                else:
                        message="密码不正确！"
            except:
                message="用户不存在！"
        return render(request,'login.html',locals())

    login_form = UserForm()
    return render(request,'login.html',locals())

def register(request):
    if request.session.get('is_login',None):
        return redirect('')
    if request.method == "POST":
        tags_lis = request.POST.getlist('tags')
        print(tags_lis)
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  #验证数据
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            password2 = register_form.cleaned_data['password2']
            if password != password2:
                message = "两次输入的密码不一样！"
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:
                    message='用户已存在,请重新选择用户名！'
                    return render(request, 'register.html',locals())
                new_user = models.User.objects.create()
                new_user.username = username
                new_user.password = password
                # for i in tags_lis:
                new_user.tags = tags_lis
                new_user.save()
                print("用户创建成功！")
                return redirect('login')
    register_form = RegisterForm()
    return render(request,'register.html',locals())

def logout(request):
    login_form = UserForm()
    if not request.session.get('is_login',None):
        return redirect('login')
    request.session.flush()
    return render(request,'login.html',locals())
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
import models
import django_comments
# Create your views here.


def index(request):
        
    return render_to_response('index.html')

def home(request):
    bbs_list = models.BBS.objects.all()
    bbs_category = models.Category.objects.all()
    return render_to_response('home.html',{'bbs_list':bbs_list,
                                           'user':request.user,
                                           'bbs_category':bbs_category})

def bbs_detail(request,bbs_id):
    bbs = models.BBS.objects.get(id = bbs_id)
    
    return render_to_response('bbs_detail.html',{'bbs_obj':bbs,'user':request.user})

def sub_comment(request):
   
    bbs_id = request.POST.get('bbs_id')
    new_comment = request.POST.get('comment_content')
    print new_comment
    
    django_comments.models.Comment.objects.create(
                                   content_type_id =8,
                                   object_pk = bbs_id,
                                   site_id = 1,
                                   user = request.user,
                                   comment = new_comment
                                                                     )
    return HttpResponseRedirect('/detail/%s/' %bbs_id,)

def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    print username,password
    if user is not None:
        auth.login(request, user)
        content = '''
        welcome %s!!!
        <a href='/logout/>logout</a>
        '''%user.username
        return HttpResponseRedirect('/home.html')
    else:
        return render_to_response('login.html',{'login_err':'wrong'''})
    


def logout_view(request):
    user = request.user
    auth.logout(request)
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/'>re-login</a>" %user)
    
def Login(request):
    return render_to_response('login.html')

def bbs_pub(request):
    return render_to_response('bbs_pub.html')
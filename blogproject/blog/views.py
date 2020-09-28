from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
#목록들을 얻어올 때 객체를 못가져오면 404 error를 보여줌, request를 처리하고 보여주는 패키지

from .models import Blog
from django.core.paginator import Paginator
from django.utils import timezone #입력한 시간이 자동으로 넘기기 위해 timezone 패키지 import함.
#model에서 template으로 바로 내용을 보낼 수 x, views.py를 거쳐 보내야 함.
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):#요청이 들어오면 home.html를 내보내는 함수
    blogs = Blog.objects#Blog class에서 객체 목록들(쿼리셋)을 가져와 blogs라는 변수에 대입.
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts':posts})
    #blogs라는 변수를 home.html에 띄우기 위해 
    #3번째 인자로 사전형 객체를 사용해 변수 blogs라는 키 값에 blogs(value값)를 담음.


def detail(request, blog_id):#blog_id:path-converter로 전달 받았음
    details = get_object_or_404(Blog, pk=blog_id) #(model name, pk(=primary key, 구분자) = 게시글 id)
    return render(request, 'detail.html', {'detail':details})


def new(request):
    return render(request, 'new.html')


def create(request):#new.html의 form태그에서 호출
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    #get방식으로 넘어온 값(title)에 접근하기 위해 request.GET객체를 사용하여 blog 객체의 title멤버에 넘겨줌.
    #get방식:주소 표시줄에 입력한 내용이 노출되기 때문에 보안상의 문제가 민감한 경우에는 사용X, 길이 제한O
    
    blog.pub_date = timezone.datetime.now()
    blog.save()#.save(): data가 있으면 수정, 없으면 insert
    return redirect('/blog/'+str(blog.id))
    # '~/blog/1'같이 id가 주소에 보이게 객체(게시글)의 id를 문자열형태로 바꿈.
    # redirect : view 함수 내에서 특정 url로 이동 하고자 할 때 사용


def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':#요청받은 방식이 POST이면 아래문장 수행
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blog/'+str(blog.id))
    return render(request, 'edit.html', {'blog':blog})
    #요청이 들어오면 edit.html을 보냄 +blog라는 변수를 edit.html에 띄우기 위해 사전형 객체를 이용.


def delete(request, blog_id):#각 게시물마다 필요하니까 blog_id를 인자로 받음.
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()#각 Blog 객체 별로 DB에 delete 요청
    return redirect('/')#/(root(=http://127.0.0.1:8000/))주소로 url 요청을 다시함.


@login_required
def comment_add(request, blog_id):
    if request.method == 'POST': 
        post = Blog.objects.get(pk=blog_id)
        comment = Comment()
        comment.user = request.user
        comment.body = request.POST['body']
        comment.post = post
        comment.save()
        return redirect('/blog/'+str(blog_id))
    else:
        return HttpResponse('잘못된 접근')


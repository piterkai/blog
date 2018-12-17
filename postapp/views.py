import math
from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from postapp.models import Post


def index(request,num=1):
    num = int(num)
    # 查询所有帖子信息
    post_list = Post.objects.all().order_by('-created')
    #分页
    page_obj = Paginator(post_list,1)

    # 获取当前页的数据
    post_info_list = page_obj.page(num)
    #获取页码数
    start = num -math.ceil(10.0/2)
    if start<1:
        start=1
    end = start+9
    if end >page_obj.num_pages:
        end = page_obj.num_pages
    if end<10:
        start =1
    else:
        start = end-9
    page_list = range(start,end+1)


    return render(request,'index.html',{'postList':post_info_list,'num':num,'page_list':page_list})


def index_detail(request,postid):
    postid = int(postid)
    # 根据postid查询post详情信息
    post_obj = Post.objects.get(id=postid)
    return render(request,'detail.html',{'post_obj':post_obj})


def index_category(request,categoryid):
    #根据cid查询post
    a_post_list = Post.objects.filter(category_id=categoryid)

    return render(request,'article.html',{'a_post_list':a_post_list})


def index_archive(request,y=-1,m=-1):
    y = int(y)
    m = int(m)
    if y==-1 and m==-1:
        a_post_list = Post.objects.all()
    else:
        #根据年月查询post
        a_post_list = Post.objects.filter(created__year=y,created__month=m)

    return render(request, 'article.html', {'a_post_list': a_post_list})
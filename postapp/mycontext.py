from django.db.models import Count

from postapp.models import Post


def getRightInfo(request):
    #查询分类信息
    r_category_post_list = Post.objects.values('category','category__cname').annotate(c=Count('*'))
    #查询归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("select created,count('*') as c from postapp_post group by DATE_FORMAT(created,'%Y-%b') order by c desc")
    r_date_post_list = cursor.fetchall()
    #查询近期文章
    r_recent_post = Post.objects.order_by('-id')[:3]
    return {'r_category_post_list':r_category_post_list,'r_date_post_list':r_date_post_list,'r_recent_post':r_recent_post}
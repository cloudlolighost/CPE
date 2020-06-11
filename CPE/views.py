from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from CPE import models
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from CPE.models import Cpe


def cpes(request):
    # return HttpResponse(“Hello world ! “)
    # article = models.Blog.objects.get(pk=’41078855')
    # return render(request, ‘blog/index.html’, {“article”: articles})
    # 获取全部博客信息
    limit = 10  # 每页显示的记录数
    topics = Cpe.objects.all()
    paginator = Paginator(topics, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        topics = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        topics = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        topics = paginator.page(paginator.num_pages)  # 取最后一页的记录

    # 返回至前端渲染
    return render(request, "index.html", locals()) # 必须用这个return

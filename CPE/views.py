from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from CPE import models
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from CPE.models import Cpe
from django.shortcuts import render


def cpes(request):
    # return HttpResponse(“Hello world ! “)
    # article = models.Blog.objects.get(pk=’41078855')
    # return render(request, ‘blog/index.html’, {“article”: articles})
    # 获取全部博客信息
    # limit = 10  # 每页显示的记录数
    topics = Cpe.objects.all()
    # paginator = Paginator(topics, limit)  # 实例化一个分页对象
    # page = request.GET.get('page')  # 获取页码
    # try:
    #     topics = paginator.page(page)  # 获取某页对应的记录
    # except PageNotAnInteger:  # 如果页码不是个整数
    #     topics = paginator.page(1)  # 取第一页的记录
    # except EmptyPage:  # 如果页码太大，没有相应的记录
    #     topics = paginator.page(paginator.num_pages)  # 取最后一页的记录

    # 返回至前端渲染
    return render(request, "index.html", locals()) # 必须用这个return






# def cpes_list(request):
#     # 从 URL 中取参数
#     page_num = request.GET.get("page")
#     print(page_num, type(page_num))
#     page_num = int(page_num)
#
#     # 定义两个变量保存数据从哪儿取到哪儿
#     data_start = (page_num - 1) * 10
#     data_end = page_num * 10
#
#     # 书籍总数
#     total_count = Cpe.objects.all().count()
#
#     # 每一页显示多少条数据
#     per_page = 10
#
#     # 总共需要多少页码来显示
#     total_page, m = divmod(total_count, per_page)
#
#     # 页面上最多展示的页码
#     max_page = 11
#     half_max_page = max_page // 2
#
#     # 页面上展示的页码的开始页
#     page_start = page_num - half_max_page
#     # 页面上展示的页码的结束页
#     page_end = page_num + half_max_page
#
#     # 如果当前页减一半比 1 小
#     if page_start <= 1:
#         page_start = 1
#         page_end = max_page
#     # 如果当前页加一半比总页码还大
#     if page_end > total_page:
#         page_end = total_page
#         page_start = total_page - max_page + 1
#
#     # 如果还有数据
#     if m:
#         total_page += 1
#
#     all_book = Cpe.objects.all()[data_start:data_end]
#
#     # 拼接 html 的分页代码
#     html_list = []
#     for i in range(page_start, page_end + 1):
#         tmp = '<li><a href="/index/?page={0}">{0}</a></li>'.format(i)
#         html_list.append(tmp)
#
#     page_html = "".join(html_list)
#
#     return render(request, "index.html", {"books": all_book, "page_html": page_html})
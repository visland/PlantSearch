from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import connection
from django.shortcuts import render

from .forms.forms import QueryUserForm
from .models import Tree

def index(request):
    templateView = 'index.html'
    countNum = -1
    keywords = ''
    time = 0

    if request.method == 'GET':
        form = QueryUserForm(request.GET)
        # 验证表单
        if form.is_valid():
            # 过滤需要的数据
            condition = form.cleaned_data['condition']
            keywords = form.cleaned_data['queryContent']

            print('condition == ' + condition)
            print('keywords == ' + keywords)

            countNum = 0
            # 查询结果
            if condition == 'zname':
                user_list = Tree.objects.filter(zname__icontains=keywords)
            elif condition == 'kname':
                user_list = Tree.objects.filter(kname__icontains=keywords)
                
            countNum = user_list.count()
            # 获取查询耗时
            time = (connection.queries)[0].get('time')
            print('user_list size=== ', user_list.count())
            print('time === ', time)

            # 显示分页操作, 每页显示 20 条
            paginator = Paginator(user_list, 20)
            page = request.GET.get('page')
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                # 如果请求的页数不是整数，返回第一页。
                users = paginator.page(1)
            except EmptyPage:
                # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
                users = paginator.page(paginator.num_pages)

            return render(request, templateView, {
                    'countNum': countNum,
                    'condition': condition,
                    'keywords': keywords,
                    'form': form,
                    'users': users,
                    'time': time,
                })


            # 查询不到数据, 显示没有数据的浮窗
            if countNum == 0:
                return render(request, templateView, {
                    'countNum': countNum,
                    'keywords': keywords,
                    'form': form,
                })
        # 直接访问主页, 显示的内容
        else:
            return render(request, templateView, {'countNum': countNum,  'form': form})
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import connection
from django.shortcuts import render
from django.db.models import Q

from .forms.forms import QueryUserForm
from .models import Tree, Months

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
            keywords = form.cleaned_data['queryContent']
            bloom_color_checked = form.cleaned_data['bloom_color_condition']
            fruit_color_checked = form.cleaned_data['fruit_color_condition']
            leaf_color_checked = form.cleaned_data['leaf_color_condition']
            bloom_date_condition = form.cleaned_data['bloom_date_condition']
            fruit_date_condition = form.cleaned_data['fruit_date_condition']
            tree_type_condition = form.cleaned_data['tree_type_condition']

            user_list = Tree.objects
            
            # 文本输入框查询结果
            if keywords:
                user_list = user_list.filter(Q(kname__icontains=keywords)|Q(sname__icontains=keywords)|Q(zname__icontains=keywords)|Q(ldname__icontains=keywords)|Q(biename__icontains=keywords)|Q(morphology__icontains=keywords))
            if bloom_date_condition != "任意":
                user_list = user_list.filter(bloom_date__name__contains=bloom_date_condition)
            if fruit_date_condition != "任意":
                user_list = user_list.filter(fruit_date__name__contains=fruit_date_condition)
            if tree_type_condition != "任意":
                user_list = user_list.filter(tree_type=tree_type_condition)

            # 高级查询结果
            b = Q()
            for elem in bloom_color_checked:
                b = b | Q(bloom_color__icontains=elem)
            f = Q()
            for elem in fruit_color_checked:
                f = f | Q(fruit_color__icontains=elem)
            l = Q()
            for elem in leaf_color_checked:
                l = l | Q(leaf_color__contains=elem)
            user_list = user_list.filter(b & f & l)

            countNum = 0
            countNum = user_list.count()
            time = (connection.queries)[0].get('time')

            # 显示分页操作, 每页显示 10 条
            paginator = Paginator(user_list, 10)
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
                    # 'condition': condition,
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
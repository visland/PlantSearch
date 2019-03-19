from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.shortcuts import render
from django.db.models import Q

from .forms.forms import QueryUserForm
from .models import Tree, Months

def detail(request, species_name):
    template_name = 'detail.html'
    tree = get_object_or_404(Tree, species_name=species_name)
    return render(request, template_name, {
        'tree': tree,
        })

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
            leaf_type_condition = form.cleaned_data['leaf_type_condition']
            tree_value_condition = form.cleaned_data['tree_value_condition']
            tree_shape_condition = form.cleaned_data['tree_shape_condition']
            soil_condition = form.cleaned_data['soil_condition']
            pollution_condition = form.cleaned_data['pollution_condition']
            
            user_list = Tree.objects
            
            # 文本输入框查询结果
            if keywords:
                user_list = user_list.filter(Q(species_name__icontains=keywords)|Q(family_name__icontains=keywords)|Q(genus_name__icontains=keywords)|Q(latin_name__icontains=keywords)|Q(alternative_name__icontains=keywords)|Q(morphology__icontains=keywords))
            
            if bloom_date_condition != "任意":
                if bloom_date_condition == "1月":
                    user_list = user_list.exclude(bloom_date__name__contains="11月").filter(bloom_date__name__contains=bloom_date_condition)
                if bloom_date_condition == "2月":
                    user_list = user_list.exclude(bloom_date__name__contains="12月").filter(bloom_date__name__contains=bloom_date_condition)
                user_list = user_list.filter(bloom_date__name__contains=bloom_date_condition)
            
            if fruit_date_condition != "任意":
                if fruit_date_condition == "1月":
                    user_list = user_list.exclude(fruit_date__name__contains="11月").filter(fruit_date__name__contains=bloom_date_condition)
                if fruit_date_condition == "2月":
                    user_list = user_list.exclude(fruit_date__name__contains="12月").filter(fruit_date__name__contains=bloom_date_condition)
                user_list = user_list.filter(fruit_date__name__contains=fruit_date_condition)
            
            # if tree_type_condition:
            #     if tree_type_condition == "乔木":
            #         user_list = user_list.exclude(tree_type__contains="小乔木").filter(tree_type__contains=tree_type_condition)
            #     user_list = user_list.filter(tree_type__contains=tree_type_condition)
            
            if leaf_type_condition != "常绿或落叶":
                user_list = user_list.filter(leaf_type__contains=leaf_type_condition)
            if soil_condition != "任意土质":
                user_list = user_list.filter(Q(soil__contains=soil_condition) | Q(soil__contains='不严'))

            # 高级查询结果
            b = Q()
            for elem in bloom_color_checked:
                b = b | Q(bloom_color__icontains=elem)
            f = Q()
            for elem in fruit_color_checked:
                f = f | Q(fruit_color__icontains=elem)
            l = Q()
            for elem in leaf_color_checked:
                l = l | Q(leaf_color__icontains=elem)
            t = Q()
            for elem in tree_type_condition:
                t = t | Q(tree_type__icontains=elem)
            s = Q()
            for elem in tree_shape_condition:
                s = s | Q(tree_shape__icontains=elem)
            v = Q()
            for elem in tree_value_condition:
                v = v | Q(tree_value__icontains=elem)
            p = Q()
            for elem in pollution_condition:
                p = p | Q(pollution_tolerance__icontains=elem)
            user_list = user_list.filter(b & f & l & t & s & v & p)

            countNum = 0
            countNum = user_list.count()
            time = (connection.queries)[0].get('time')

            # 显示分页操作
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
            
            query_params = request.GET.copy()
            return render(request, templateView, {
                    'countNum': countNum,
                    'keywords': keywords,
                    'form': form,
                    'users': users,
                    'time': time,
                    'query_params': query_params,
                    'paginator': paginator,
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
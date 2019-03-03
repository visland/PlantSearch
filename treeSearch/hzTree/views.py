from django.shortcuts import render

from .forms.forms import QueryUserForm
from .models import Tree

# Create your views here.
def index(request):
    templateView = 'index.html'

    if request.method == 'GET':
        form = QueryUserForm(request.GET)
        # 验证表单
        if form.is_valid():
            # 过滤需要的数据, 获取查询条件和查询内容
            condition = form.cleaned_data['condition']
            keywords = form.cleaned_data['queryContent']
            print('condition == ' + condition)
            print('keywords == ' + keywords)

            # 查询数据...
            
            return render(request, templateView, {'form': form})
        # 直接访问主页, 显示的内容
        else:
            return render(request, templateView, {'form': form})
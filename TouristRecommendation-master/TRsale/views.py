from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from TRsale import models


def index(request):
    if request.session.get('is_login', None):
        list_tags = request.session['user_tags']
        list_tags = eval(list_tags)
        if len(list_tags) == 3:
            data_diqu = models.All.objects.filter(Q(cityname=list_tags[0]) | Q(cityname=list_tags[1]) | Q(cityname=list_tags[2])).order_by('?')[:20]
        elif len(list_tags) == 2:
            data_diqu = models.All.objects.filter(Q(cityname=list_tags[0]) | Q(cityname=list_tags[1])).order_by('?')[:20]
        elif len(list_tags) == 1:
            data_diqu = models.All.objects.filter(cityname=list_tags[0]).order_by('?')[:20]
        else:
            data_diqu = models.All.objects.all().order_by('?')[:20]
    else:
        data_diqu=models.All.objects.all().order_by('?')[:20]
    # 查询数据库映射
    # data1~data10是销量前十的数据
    data1 = models.DmSale.objects.get(id=1)
    data2 = models.DmSale.objects.get(id=2)
    data3 = models.DmSale.objects.get(id=3)
    data4 = models.DmSale.objects.get(id=4)
    data5 = models.DmSale.objects.get(id=5)
    data6 = models.DmSale.objects.get(id=6)
    data7 = models.DmSale.objects.get(id=7)
    data8 = models.DmSale.objects.get(id=8)
    data9 = models.DmSale.objects.get(id=9)
    data10 = models.DmSale.objects.get(id=10)
    # 这里是data是免费景点的数据
    # data = models.DmFree.objects.filter(id__range=[25, 49])
    data=models.DmFree.objects.all().order_by('?')[:20]
    return render(request, 'comment.html', locals())


def sale_one(request):
    return render(request,'xiangqingye/one.html')

def sale_two(request):
    return render(request,'xiangqingye/two.html')

def shanghai(request):
    data_shanghai = models.DmShanghai.objects.filter(id__range=[1,35])
    return render(request,'xiangqingye/shanghai.html',{'data_shanghai':data_shanghai})

def yunnan(request):
    data_yunnan = models.DmYunnan.objects.filter(id__range=[1,35])
    return render(request,'xiangqingye/yunnan.html',{'data_yunnan':data_yunnan})

def data(request):
    return render(request,'data.html')


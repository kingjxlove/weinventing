from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from rest_framework import viewsets, mixins, serializers

from goods.models import Notebook


# Create your views here.

class NotebookSerializer(serializers.ModelSerializer):
    class Meta:
        # 序列化模型
        model = Notebook
        fields = ['g_id', 'name', 'shop', 'price', 'img', 'commit_num']


class NotebookView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


def index(request):
    if request.method == 'GET':
        all_goods = Notebook.objects.all()
        paginator = Paginator(all_goods, 10)
        page = request.GET.get('page', 1)
        try:
            page = paginator.page(page)  # contacts为Page对象！
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page = paginator.page(paginator.num_pages)
        return render(request, 'show.html', {'goods': all_goods,
                                             'page': page})

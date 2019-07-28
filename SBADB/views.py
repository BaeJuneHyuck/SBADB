from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from rest_framework.viewsets import ModelViewSet

from SBADB.ecndoers import MyEncoder
from SBADB.forms import HeroForm
from SBADB.models import Hero
from SBADB.serializers import HeroSerializer


class HeroViewSet(ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer


def index(request):
    qs = Hero.objects.all()  # QuerySet 타입 => Lazy

    query = request.GET.get("query")
    if query:
        qs = qs.filter(name__icontains=query)

    format = request.GET.get("format")  # QueryDict
    if format == 'json':
        return JsonResponse(qs, safe=False, encoder=MyEncoder)

    return render(request, 'SBADB/hero_list.html', {
        'hero_list': qs,
    })


# def hero_new(request):
#     #빈폼을 요청하는건지(GET), 폼을 보내는건지(POST) 하나의 뷰에서 처리
#     if request.method == 'GET':
#         form = heroForm()
#     else:
#         form = heroForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('/hero/')
#         else:
#             form.errors
#
#     return render(request, 'hero/hero_form.html', {
#         'form': form,
#     })


#
# def hero_edit(request, pk):
#     # 오브젝트를 가져오지못하면 에러 404
#     hero = get_object_or_404(hero, pk=pk)
#     #       = hero.objects.get(pk = pk) 이거는 hero.doesNotExist 예외가 발생해서 500에러
#
#     if request.method == 'GET':
#         form = heroForm(instance=hero)
#     else:
#         form = heroForm(request.POST, request.FILES, instance=hero)
#         if form.is_valid():
#             form.save()
#             return redirect('/hero/')
#
#     return render(request, 'hero/hero_form.html', {
#         'form': form,
#     })
#
#


hero_new = CreateView.as_view(
    model=Hero,
    form_class=HeroForm,
    success_url='/hero',
)


hero_edit = UpdateView.as_view(
    model=Hero,
    form_class=HeroForm,
    success_url='/hero/',
)



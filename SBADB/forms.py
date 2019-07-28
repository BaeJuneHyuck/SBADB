from django import forms

from SBADB.models import Hero


class HeroForm(forms.ModelForm):
    #모델 폼 사용하면 모델을 사용해서 중복코딩없이
    class Meta:
        model = Hero
        # 리스트 문자열로 참조할 필드 지정할 수 있음
        fields = '__all__'



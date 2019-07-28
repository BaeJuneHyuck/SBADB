from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Hero, Category


class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'page_tag']

    def page_tag(self, hero):
        tag = '<a href="{}" target="_blank">{}</a>'.format(hero.page_url, hero.page_url)
        return mark_safe(tag)


admin.site.register(Hero, HeroAdmin)
admin.site.register(Category)

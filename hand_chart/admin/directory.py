import os

from django.conf import settings
from django.contrib import admin
from django.core.cache import cache
from django.db.models import Q
from django.utils.safestring import mark_safe

import hand_chart.models as models
from hand_chart.admin.filter import StackFilter


@admin.register(models.OptionsAction)
class OptionsActionAdmin(admin.ModelAdmin):
    """Справочник вариантов ответов с цветами"""
    list_display = ('name', 'preview_color', 'stacks', 'description')
    list_filter = (StackFilter,)

    def preview_color(self, obj):
        html = f'<div style="background-color: {obj.color};width: 50%;height: 20px;text-align: center;' \
               f'padding-top: 4px;">{obj.color}</div>'
        return mark_safe(html)

    def stacks(self, obj):
        cache_key = f'stacks_cache_{obj.id}'
        cached_preview = cache.get(cache_key)

        if cached_preview is not None:
            return mark_safe(cached_preview)

        table_ids = models.ContentHandChart.objects.filter(
            Q(utg__in=[obj.id]) |
            Q(utg1__in=[obj.id]) |
            Q(mp__in=[obj.id]) |
            Q(mp1__in=[obj.id]) |
            Q(hj__in=[obj.id]) |
            Q(co__in=[obj.id]) |
            Q(btn__in=[obj.id]) |
            Q(sb__in=[obj.id])
        ).values_list('table__id', flat=True).distinct()

        tables = models.TableHandChart.objects.select_related('stack').filter(id__in=table_ids)
        stacks = [f'<p>{table.stack.name}</p>' for table in tables]
        html = ''.join(stacks)

        cache.set(cache_key, html, timeout=600)  # Кэш ограничения времени жизни 10 минут
        return mark_safe(html)

    preview_color.short_description = "Превью цвета"
    stacks.short_description = "Стеки игры"


@admin.register(models.GameStacks)
class GameStacksAdmin(admin.ModelAdmin):
    """Справочник стеков игры"""
    list_display = ('name', 'sort')


@admin.register(models.PokerChips)
class PokerChipsAdmin(admin.ModelAdmin):
    """Справочник комбинаций для таблицы"""
    list_display = ('name', 'suit', 'position', 'delta_x', 'delta_y', 'preview_chips')
    list_editable = ('delta_x', 'delta_y')
    readonly_fields = ('preview_chips',)
    fields = ('name', 'suit', 'position', 'delta_x', 'delta_y', 'preview_chips')
    list_per_page = 20

    def preview_chips(self, obj):
        cache_key = f'preview_chips_cache_{obj.id}'
        cached_preview = cache.get(cache_key)

        if cached_preview is not None:
            return mark_safe(cached_preview)

        init_x = settings.SVG_X_TEXT
        init_y = settings.SVG_Y_TEXT
        init_str = f'<text id="AT_1_" transform="matrix(1 0 0 1 {init_x} {init_y})"'

        new_x = init_x + obj.delta_x
        nex_y = init_y + obj.delta_y
        new_str = f'<text id="AT_1_" transform="matrix(1 0 0 1 {new_x} {nex_y})"'

        svg = open(os.path.join(settings.BASE_DIR, 'static/hand_chart/img/chip.svg'))
        data_svg = svg.read()
        # Замена координат
        data_svg = data_svg.replace(init_str, new_str, 1)
        # Замена текста комбинации
        data_svg = data_svg.replace('>AA<', f'>{obj.name}<', 1)

        cache.set(cache_key, data_svg, timeout=None)  # Кэш без ограничения времени жизни
        return mark_safe(data_svg)

    preview_chips.short_description = "Превью фишки"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        cache_key = f'preview_chips_cache_{obj.id}'
        cache.delete(cache_key)


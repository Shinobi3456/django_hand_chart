import os

from django.conf import settings
from django.contrib import admin
from django.db import connection
from django.utils.safestring import mark_safe

import hand_chart.models as models
from hand_chart.admin.filter import StackFilter
from hand_chart.sql import SQL_GET_STACKS_BY_ACTION


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
        with connection.cursor() as cursor:
            cursor.execute(SQL_GET_STACKS_BY_ACTION, [obj.id, obj.id, obj.id, obj.id, obj.id, obj.id, obj.id, obj.id])
            table_ids = [row[0] for row in cursor.fetchall()]
        tables = models.TableHandChart.objects.select_related('stack').filter(id__in=table_ids)
        stacks = set()
        for table in tables:
            stacks.add(f'<p>{table.stack.name}</p>')
        html = ''.join(stacks)
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

        return mark_safe(data_svg)

    preview_chips.short_description = "Превью фишки"


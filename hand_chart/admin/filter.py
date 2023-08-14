from django.contrib.admin import SimpleListFilter
from django.db import connection

import hand_chart.models as models


class StackFilter(SimpleListFilter):
    title = 'Стеки игры'
    parameter_name = 'stack2'

    def lookups(self, request, model_admin):
        stacks = models.GameStacks.objects.all()
        return [(s.id, s.name) for s in stacks]

    def queryset(self, request, queryset):
        if self.value() == 'ALL':
            return queryset
        if self.value():
            color_ids = []
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT utg.color_id, utg1.color_id, mp.color_id, mp1.color_id, hl.color_id, co.color_id, btn.color_id, sb.color_id
                FROM ha
                    JOIN rye_range_ryerangecontent on rye_range_ryerangecontent.table_id=rye_range_tableryerange.id
                    JOIN rye_range_ryerangecontent_utg utg on rye_range_ryerangecontent.id = utg.ryerangecontent_id
                    JOIN rye_range_ryerangecontent_utg1 utg1 on rye_range_ryerangecontent.id = utg1.ryerangecontent_id
                    JOIN rye_range_ryerangecontent_mp mp on rye_range_ryerangecontent.id = mp.ryerangecontent_id
                    JOIN rye_range_ryerangecontent_mp1 mp1 on rye_range_ryerangecontent.id = mp1.ryerangecontent_id
                    JOIN rye_range_ryerangecontent_hl hl on rye_range_ryerangecontent.id = hl.ryerangecontent_id
                    JOIN rye_range_ryerangecontent_co co on rye_range_ryerangecontent.id = co.ryerangecontent_id
                    JOIN rye_range_ryerangecontent_btn btn on rye_range_ryerangecontent.id = btn.ryerangecontent_id
                    JOIN rye_range_ryerangecontent_sb sb on rye_range_ryerangecontent.id = sb.ryerangecontent_id
                WHERE rye_range_tableryerange.stack_id=%s
                """, [self.value()])

                for row in cursor.fetchall():
                    color_ids += [row[i] for i in range(0, 8)]
            return queryset.filter(id__in=set(color_ids))

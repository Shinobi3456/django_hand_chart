from django.contrib.admin import SimpleListFilter
from django.db.models import Q

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
            result = models.ContentHandChart.objects.filter(table__stack_id=self.value()).prefetch_related(
                'utg',
                'utg1',
                'mp',
                'mp1',
                'hj',
                'co',
                'btn',
                'sb'
            ).values_list(
                'utg__id',
                'utg1__id',
                'mp__id',
                'mp1__id',
                'hj__id',
                'co__id',
                'btn__id',
                'sb__id'
            )

            actions_ids = []
            for row in result:
                for action_id in row:
                    if action_id:
                        actions_ids.append(action_id)
            return queryset.filter(Q(id__in=set(actions_ids)) | Q(id__isnull=True))

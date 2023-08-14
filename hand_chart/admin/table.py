from urllib.parse import urlparse

from django import forms
from django.contrib import admin
from django.shortcuts import redirect

import hand_chart.models as models
from hand_chart.admin.form import ContentHandChartForm


@admin.register(models.TableHandChart)
class TableRyeRangeAdmin(admin.ModelAdmin):
    list_display = ('name', 'stack', 'is_active')
    list_editable = ('is_active', )


@admin.register(models.PreviewHandChart)
class PreviewRyeRangeAdmin(admin.ModelAdmin):
    form = ContentHandChartForm
    change_list_template = 'admin/preview_hand_chart_change_list.html'

    def get_queryset(self, request):
        queryset = models.ContentHandChart.objects

        if request.method == 'GET':
            table_id = request.GET.get('table_id', None)
        else:
            table_id = request.POST.get('table_id', None)
            if table_id is None:
                table_id = request.GET.get('table_id', None)

        if not table_id:
            table = models.TableHandChart.objects.filter(is_active=True).first()
            if table:
                table_id = table.id

        if table_id:
            queryset = models.ContentHandChart.objects.filter(table_id=table_id)
        return queryset

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        tables = models.TableHandChart.objects.filter(is_active=True).all()
        if len(tables) == 0:
            response.context_data['tables'] = []
            response.context_data['result'] = []
            response.context_data['colors_class'] = []

            return response

        response.context_data['tables'] = tables

        rows = qs.all()

        i = 0
        result = []
        temp = []
        for row in rows:
            if i < 12:
                temp.append(row)
                i += 1
            else:
                temp.append(row)
                result.append(temp)
                i = 0
                temp = []

        response.context_data['result'] = result

        rows = models.OptionsAction.objects.all()
        colors = []
        for row in rows:
            colors.append('.color_'+str(row.id)+'_sector{fill:'+row.color+';}')
        response.context_data['colors_class'] = colors

        return response

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        response = super().changeform_view(request, object_id, form_url, extra_context)
        if response.__class__.__name__ != 'HttpResponseRedirect':
            suits_dict = {}
            suits = models.PokerChips.SUIT_CHOICES
            for suit in suits:
                suits_dict[suit[0]] = suit[1]

            response.context_data['title'] = 'Изменение комбинации '+response.context_data['original'].chip.name + \
                ' ('+response.context_data['original'].chip.get_suit_display()+')'
            response.context_data['has_delete_permission'] = False
            response.context_data['has_add_permission'] = False
            response.context_data['has_view_permission'] = False
            response.context_data['adminform'].form.fields['table'].widget = forms.HiddenInput(
            )
            response.context_data['adminform'].form.fields['chip'].widget = forms.HiddenInput(
            )
        else:
            url = urlparse(request.META.get('HTTP_REFERER'))
            url = response.url+'?'+url.query
            return redirect(url)

        return response

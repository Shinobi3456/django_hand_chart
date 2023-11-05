from django import forms

import hand_chart.models as models


class ContentHandChartForm(forms.ModelForm):
    class Meta:
        model = models.ContentHandChart
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        fields_to_check = ['utg', 'utg1', 'co', 'hl', 'mp', 'mp1', 'btn', 'sb']

        for field_name in fields_to_check:
            field_value = cleaned_data.get(field_name)
            if field_value and len(field_value) > 2:
                raise forms.ValidationError(f"Максимум можно выбрать только 2 варианта для поля {field_name}.")

        return cleaned_data

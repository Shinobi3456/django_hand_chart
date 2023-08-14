from django import forms

import hand_chart.models as models


class ContentHandChartForm(forms.ModelForm):
    class Meta:
        model = models.ContentHandChart
        fields = '__all__'

    def clean_utg(self):
        utg = self.cleaned_data['utg']
        if len(utg) > 2:
            raise forms.ValidationError(
                "Максимум можно выбрать только 2 варианта.")
        return utg

    def clean_utg1(self):
        utg1 = self.cleaned_data['utg1']
        if len(utg1) > 2:
            raise forms.ValidationError(
                "Максимум можно выбрать только 2 варианта.")
        return utg1

    def clean_co(self):
        co = self.cleaned_data['co']
        if len(co) > 2:
            raise forms.ValidationError(
                "Максимум можно выбрать только 2 варианта.")
        return co

    def clean_hl(self):
        hl = self.cleaned_data['hl']
        if len(hl) > 2:
            raise forms.ValidationError(
                "Максимум можно выбрать только 2 варианта.")
        return hl

    def clean_mp(self):
        mp = self.cleaned_data['mp']
        if len(mp) > 2:
            raise forms.ValidationError(
                "Максимум можно выбрать только 2 варианта.")
        return mp

    def clean_mp1(self):
        mp1 = self.cleaned_data['mp1']
        if len(mp1) > 2:
            raise forms.ValidationError(
                "Максимум можно выбрать только 2 варианта.")
        return mp1

    def clean_btn(self):
        btn = self.cleaned_data['btn']
        if len(btn) > 2:
            raise forms.ValidationError(
                "Максимум можно выбрать только 2 варианта.")
        return btn

    def clean_sb(self):
        sb = self.cleaned_data['sb']
        if len(sb) > 2:
            raise forms.ValidationError(
                "Максимум можно выбрать только 2 варианта.")
        return sb

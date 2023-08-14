from colorfield.fields import ColorField
from django.db import models
from django.urls import reverse


class PokerChips(models.Model):
    """Справочник покерных фишек для таблицы."""
    NOT_SUIT = 'NS'
    ONE_SUIT = 'OS'
    TWO_SUIT = 'TS'

    SUIT_CHOICES = [
        (NOT_SUIT, 'Масть не важна'),
        (ONE_SUIT, 'Одномастные'),
        (TWO_SUIT, 'Разная масть'),
    ]

    class Meta:
        verbose_name = 'Комбинация фишек'
        verbose_name_plural = 'Комбинации фишек'
        ordering = ('position', )

    name = models.CharField("Комбинация", max_length=2, default='')
    suit = models.CharField("Масть", max_length=2,
                            choices=SUIT_CHOICES, default=NOT_SUIT)
    position = models.PositiveIntegerField("Позиция в таблице")
    delta_x = models.IntegerField("Смещение текста по X", default=0)
    delta_y = models.IntegerField("Смещение текста по Y", default=0)

    def __str__(self):
        return f'{self.name} {self.suit}'


class GameStacks(models.Model):
    """Справочник стеков игры."""

    class Meta:
        verbose_name = 'Стек игры'
        verbose_name_plural = '1. Стеки игры'
        ordering = ('sort', )

    name = models.CharField("Название", max_length=200)
    sort = models.PositiveIntegerField("Сортировка", default=500)

    def __str__(self):
        return self.name


class OptionsAction(models.Model):
    """Справочник вариантов действий."""

    class Meta:
        verbose_name = 'Вариант действия'
        verbose_name_plural = '2. Варианты действий'

    name = models.CharField("Название", max_length=200)
    color = ColorField("Цвет",  default="#FFFFFF")
    description = models.TextField("Описание", max_length=200, default='', blank=True)

    def __str__(self):
        return f'{self.name} ({self.description})'


class TableHandChart(models.Model):
    """Таблица Нand Chart."""
    class Meta:
        verbose_name = 'Таблица Нand Chart'
        verbose_name_plural = '3. Таблицы Нand Chart'
        ordering = ('id', )

    name = models.CharField("Название таблицы", max_length=200, default='')
    stack = models.ForeignKey(
        GameStacks, on_delete=models.SET_NULL, verbose_name='Стек игры', null=True)
    description = models.TextField("Описание", max_length=2000, default='')
    is_active = models.BooleanField('Активна')

    def __str__(self):
        stack = self.stack.name if self.stack is not None else '__'
        return stack

    def get_absolute_url(self):
        return reverse('hand_chart_detail', args=[self.id])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        rows = ContentHandChart.objects.filter(table_id=self.id).all()
        if len(rows) == 0:
            chips = PokerChips.objects.all()
            for chip in chips:
                ContentHandChart.objects.create(table_id=self.id, chip=chip)


class ContentHandChart(models.Model):
    """Содержимое таблицы Hand Chart."""

    class Meta:
        verbose_name = 'Запись в таблице Hand Chart'
        verbose_name_plural = '4. Записи в таблице Hand Chart'
        ordering = ('id', )

    table = models.ForeignKey(TableHandChart, on_delete=models.CASCADE, verbose_name="Таблица Hand Chart",
                              null=True, related_name="table_content")
    chip = models.ForeignKey(
        PokerChips, on_delete=models.SET_NULL, verbose_name="Комбинация", null=True)
    utg = models.ManyToManyField(
        OptionsAction, blank=True, verbose_name="Позиция UTG", related_name='utg_color')
    utg1 = models.ManyToManyField(
        OptionsAction, blank=True, verbose_name="Позиция UTG1", related_name='utg1_color')
    mp = models.ManyToManyField(
        OptionsAction, blank=True, verbose_name="Позиция MP", related_name='mp_color')
    mp1 = models.ManyToManyField(
        OptionsAction, blank=True, verbose_name="Позиция MP1", related_name='mp1_color')
    hj = models.ManyToManyField(
        OptionsAction, blank=True, verbose_name="Позиция HJ", related_name='hj_color')
    co = models.ManyToManyField(
        OptionsAction, blank=True, verbose_name="Позиция CO", related_name='co_color')
    btn = models.ManyToManyField(
        OptionsAction, blank=True, verbose_name="Позиция BTN", related_name='btn_color')
    sb = models.ManyToManyField(
        OptionsAction, blank=True, verbose_name="Позиция SB", related_name='sb_color')
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chip.name

    def colors_in_chips(self):
        colors = []
        positions = ['utg', 'utg1', 'mp', 'mp1', 'hj', 'co', 'btn', 'sb']

        for i in positions:
            colors_in_position = getattr(self, i).all()

            not_game = OptionsAction.objects.filter(color='#FFFFFF').first()
            if len(colors_in_position) == 0 and not_game not in colors:
                colors.append(not_game)

            for item in colors_in_position:
                if item not in colors:
                    colors.append(item)
        return colors


class PreviewHandChart(ContentHandChart):
    """Отображение таблицы Hand Chart."""

    class Meta:
        proxy = True
        verbose_name = "Hand Chart"
        verbose_name_plural = "Hand Chart"
        ordering = ('id', )

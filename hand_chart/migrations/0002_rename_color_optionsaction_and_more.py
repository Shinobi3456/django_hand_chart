# Generated by Django 4.2.3 on 2023-07-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hand_chart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Color',
            new_name='OptionsAction',
        ),
        migrations.AlterModelOptions(
            name='optionsaction',
            options={'verbose_name': 'Вариант действия', 'verbose_name_plural': '2. Варианты действий'},
        ),
    ]

import os

import cairosvg
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from hand_chart.models import ContentHandChart, Color


@receiver(post_save, sender=ContentHandChart)
def generate_chips_img(sender, instance, created, **kwargs):
    path_file = os.path.join(settings.MEDIA_ROOT, f'chips/small/chips_{instance.id}.png')

    if os.path.exists(path_file):
        os.remove(path_file)

    colors = Color.objects.all()
    context = {'value': instance, 'colors': colors}

    svg_text = render_to_string('hand_chart/chips_small.svg', context=context)
    path_svg = default_storage.save('temp/chips_small.svg', ContentFile(svg_text))
    cairosvg.svg2png(file_obj=open(os.path.join(settings.MEDIA_ROOT, path_svg)), write_to=path_file)
    default_storage.delete(path_svg)

    path_file = os.path.join(settings.MEDIA_ROOT, f'chips/big/chips_{instance.id}.png')
    if os.path.exists(path_file):
        os.remove(path_file)

    svg_text = render_to_string('hand_chart/chips_big.svg', context=context)
    path_svg = default_storage.save('temp/chips_big.svg', ContentFile(svg_text))
    cairosvg.svg2png(file_obj=open(os.path.join(settings.MEDIA_ROOT, path_svg)), write_to=path_file)
    default_storage.delete(path_svg)

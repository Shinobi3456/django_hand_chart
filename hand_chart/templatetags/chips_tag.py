from django import template
from django.utils.safestring import mark_safe

from hand_chart.models import TableHandChart

register = template.Library()


@register.simple_tag()
def get_tables():
    """Вывод всех стеков"""
    return TableHandChart.objects.filter(is_active=True).all()


@register.simple_tag
def selector_color(qs, position):
    """Вывод закраски секторов"""
    # colors = qs.all()

    if position == 'SB':
        data = '<path class="sector_1" d="M200,72.4V36.1c-44.3,0-84.2,19.9-112.3,51.7L112,112C134.1,87.6,165.4,72.4,' \
               '200,72.4z"/><path class="sector_2" d="M200,112.1V72.4c-34.6,0-65.9,15.2-88,39.6l25.8,25.8C153.8,122,' \
               '175.7,112.1,200,112.1z"/>'
    elif position == 'UTG':
        data = '<path class="sector_1" d="M288,112l24.3-24.3c-28.1-31.8-68-51.7-112.3-51.7v36.4C234.6,72.4,' \
               '265.9,87.6,288,112z"/><path class="sector_2" d="M200,72.4v39.7c24.3,0,46.2,9.8,62.2,25.7L288,' \
               '112C265.9,87.6,234.6,72.4,200,72.4z"/>'
    elif position == 'BTN':
        data = '<path class="sector_1" d="M112,112L87.7,87.7C61.8,117.1,45.9,156.6,45.9,200h32.5C78.5,165.9,91.2,' \
               '134.9,112,112z"/><path class="sector_2" d="M137.8,137.8L112,112c-20.8,22.9-33.5,53.9-33.5,88H112C112,' \
               '175.7,121.9,153.7,137.8,137.8z"/>'
    elif position == 'CO':
        data = '<path class="sector_1" d="M78.5,200L78.5,200l-32.5,0v0c0,43.4,15.9,82.9,41.8,112.3L112,' \
               '288C91.2,265.1,78.5,234.1,78.5,200z"/><path class="sector_2" d="M112,200L112,200l-33.6,0v0c0,34.1,' \
               '12.8,65.1,33.5,88l25.8-25.8C121.9,246.3,112,224.3,112,200z"/>'
    elif position == 'HJ':
        data = '<path class="sector_1" d="M112,288l-24.3,24.3c28.1,31.8,68,51.7,112.3,51.7v-36.4C165.4,327.6,134.1,' \
               '312.4,112,288z"/><path class="sector_2" d="M137.8,262.2L112,288c22.1,24.4,53.4,39.6,88,' \
               '39.6v-39.7C175.7,287.9,153.8,278,137.8,262.2z"/>'
    elif position == 'MP1':
        data = '<path class="sector_1" d="M200,327.6v36.4c44.3,0,84.2-19.9,112.3-51.7L288,288C265.9,312.4,' \
               '234.6,327.6,200,327.6z"/><path class="sector_2" d="M200,287.9v39.7c34.6,0,65.9-15.2,' \
               '88-39.6l-25.8-25.8C246.2,278,224.3,287.9,200,287.9z"/>'
    elif position == 'UTG1':
        data = '<path class="sector_1" d="M288,112c20.8,22.9,33.5,53.9,33.5,88h32.5c0-43.4-15.9-82.9-41.' \
               '8-112.3L288,112z"/><path class="sector_2" d="M288,200h33.6c0-34.1-12.8-65.1-33.5-88l-25.8,25.' \
               '8C278.1,153.7,288,175.7,288,200z"/>'
    else:
        data = '<path class="sector_1" d="M321.5,200c0,34.1-12.8,65.1-33.5,88l24.3,24.3c25.9-29.3,41.8-68.8,' \
               '41.8-112.3v0L321.5,200L321.5,200z"/><path class="sector_2" d="M288,200c0,24.3-9.9,46.3-25.8,' \
               '62.2L288,288c20.8-22.9,33.5-53.9,33.5-88v0L288,200L288,200z"/>'

    data = data.replace('sector_1', 'white_sector', 1)
    data = data.replace('sector_2', 'white_sector', 1)
    # if len(colors) == 0:
    #     data = data.replace('sector_1', 'white_sector', 1)
    #     data = data.replace('sector_2', 'white_sector', 1)
    # elif len(colors) == 1:
    #     data = data.replace('sector_1', 'color_' +
    #                         str(colors[0].id)+'_sector', 1)
    #     data = data.replace('sector_2', 'color_' +
    #                         str(colors[0].id)+'_sector', 1)
    # else:
    #     data = data.replace('sector_1', 'color_'+str(colors[0].id)+'_sector')
    #     data = data.replace('sector_2', 'color_'+str(colors[1].id)+'_sector')

    return mark_safe(data)


@register.simple_tag
def selector_color_v2(qs, is_cache=False):
    data = '<g id="full_x5F_colors_1_">' \
           'full_SB_1_' \
           'full_UTG_1_' \
           'full_BTN_1_' \
           'full_CO_1_' \
           'full_HJ_1_' \
           'full_MP1_1_' \
           'full_UTG1_1_' \
           'full_MP_1_' \
           '</g><g id="half_colors_1_">' \
           'half_SB_1_' \
           'half_UTG_1_' \
           'half_BTN_1_' \
           'half_CO_1_' \
           'half_HJ_1_' \
           'half_MP1_1_' \
           'half_UTG1_1_' \
           'half_MP_1_' \
           '</g>'

    sectors = [
        ['sb',
         'full_SB_1_',
         '<path id="full_SB_1_" class="white_sector" d="M200,112.1v-66c-42.5,0-80.9,17.2-108.8,45l46.6,46.6C153.8,122,175.7,112.1,200,112.1z"/>',
         'half_SB_1_',
         '<path id="half_SB_1_" class="white_sector" d="M200,112.1V78.5c-33.6,0-63.9,13.6-85.9,35.6l23.8,23.8C153.8,122,175.7,112.1,200,112.1z"/>'
         ],
        ['utg',
         'full_UTG_1_',
         '<path id="full_UTG_1_" class="white_sector" d="M262.2,137.8l46.6-46.6c-27.8-27.8-66.3-45-108.8-45v66C224.3,112.1,246.2,122,262.2,137.8z"/>',
         'half_UTG_1_',
         '<path id="half_UTG_1_" class="white_sector" d="M262.2,137.8l23.8-23.8c-22-22-52.4-35.6-85.9-35.6v33.7C224.3,112.1,246.2,122,262.2,137.8z"/>'],
        ['btn',
         'full_BTN_1_',
         '<path id="full_BTN_1_" class="white_sector" d="M137.8,137.8L91.2,91.2c-27.8,27.8-45,66.3-45,108.8H112C112,175.7,121.9,153.7,137.8,137.8z"/>',
         'half_BTN_1_',
         '<path id="half_BTN_1_" class="white_sector" d="M137.8,137.8l-23.8-23.8c-22,22-35.6,52.4-35.6,85.9H112C112,175.7,121.9,153.7,137.8,137.8z"/>'],
        ['co',
         'full_CO_1_',
         '<path id="full_CO_1_" class="white_sector" d="M112,200L112,200l-65.9,0v0c0,42.5,17.2,80.9,45,108.8l46.6-46.6C121.9,246.3,112,224.3,112,200z"/>',
         'half_CO_1_',
         '<path id="half_CO_1_" class="white_sector" d="M112,200L112,200l-33.6,0v0c0,33.6,13.6,63.9,35.6,85.9l23.8-23.8C121.9,246.3,112,224.3,112,200z"/>'],
        ['hj',
         'full_HJ_1_',
         '<path id="full_HJ_1_" class="white_sector" d="M137.8,262.2l-46.6,46.6c27.8,27.8,66.3,45,108.8,45v-66C175.7,287.9,153.8,278,137.8,262.2z"/>',
         'half_HJ_1_',
         '<path id="half_HJ_1_" class="white_sector" d="M137.8,262.2l-23.8,23.8c22,22,52.4,35.6,85.9,35.6v-33.7C175.7,287.9,153.8,278,137.8,262.2z"/>'],
        ['mp1',
         'full_MP1_1_',
         '<path id="full_MP1_1_" class="white_sector" d="M200,287.9v66c42.5,0,80.9-17.2,108.8-45l-46.6-46.6C246.2,278,224.3,287.9,200,287.9z"/>',
         'half_MP1_1_',
         '<path id="half_MP1_1_" class="white_sector" d="M200,287.9v33.7c33.6,0,63.9-13.6,85.9-35.6l-23.8-23.8C246.2,278,224.3,287.9,200,287.9z"/>'],
        ['utg1',
         'full_UTG1_1_',
         '<path id="full_UTG1_1_" class="white_sector" d="M308.8,91.2l-46.6,46.6c15.9,15.9,25.8,37.9,25.8,62.2h65.9C353.8,157.5,336.6,119.1,308.8,91.2z"/>',
         'half_UTG1_1_',
         '<path id="half_UTG1_1_" class="white_sector" d="M288,200h33.6c0-33.6-13.6-63.9-35.6-85.9l-23.8,23.8C278.1,153.7,288,175.7,288,200z"/>'],
        ['mp',
         'full_MP_1_',
         '<path id="full_MP_1_" class="white_sector" d="M288,200c0,24.3-9.9,46.3-25.8,62.2l46.6,46.6c27.8-27.8,45-66.3,45-108.8v0L288,200L288,200z"/>',
         'half_MP_1_',
         '<path id="half_MP_1_" class="white_sector" d="M288,200c0,24.3-9.9,46.3-25.8,62.2l23.8,23.8c22-22,35.6-52.4,35.6-85.9v0L288,200L288,200z"/>']
    ]
    if not qs:
        return

    for item in sectors:
        position = getattr(qs, item[0])
        colors = position.all()

        if len(colors) == 0:
            data = data.replace(item[1], item[2], 1)
            data = data.replace(item[3], item[4], 1)
        elif len(colors) == 1:
            item[2] = item[2].replace('white_sector', 'color_' +
                                      str(colors[0].id) + '_sector', 1)
            item[4] = item[4].replace('white_sector', 'color_' +
                                      str(colors[0].id) + '_sector', 1)
            data = data.replace(item[1], item[2], 1)
            data = data.replace(item[3], item[4], 1)
        else:
            item[2] = item[2].replace('white_sector', 'color_' +
                                      str(colors[0].id) + '_sector', 1)
            item[4] = item[4].replace('white_sector', 'color_' +
                                      str(colors[1].id) + '_sector', 1)
            data = data.replace(item[1], item[2], 1)
            data = data.replace(item[3], item[4], 1)
    return mark_safe(data)

from django.template import library

register = library.Library()

temp_list = []
@register.filter
def color_el(value):

    temp_list.append(value)
    try:
        if float(value) < 1000 and len(temp_list) % 14 != 0 :
            if float(value) < 0:

                return 'Green'
            elif float(value) > 1 and float(value) < 2:
                return  'FBC8C9'
            elif float(value) > 2 and float(value) < 5:
                return  'F5767A'
            elif float(value) > 5:
                return  'FB0008'
            else:
                return 'White'
        elif len(temp_list) % 14 == 0:
            return 'Gray'
        else:
            return 'White'
    except:
        return 'White'
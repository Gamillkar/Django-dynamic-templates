import csv

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'
    clear_data = []
    with open('inflation_russia.csv', newline='', encoding='utf-8') as file:
        reader = (csv.reader(file))

        for num, row in enumerate(reader):
            for item in row:
                item_list = item.split(';')
                temp_list = []
                if num == 0:
                    for el in item_list:
                        el = f'<strong>{el}</strong>'
                        temp_list.append(el)
                    clear_data.append(temp_list)
                else:
                    clear_data.append(item_list)

    context = {'data': clear_data}

    return render(request, template_name,
                  context)
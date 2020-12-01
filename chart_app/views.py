from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    # make it through csv or db
    # list_of_dicts_data = [
    #                         {'Date':17,'Day':'Sun','Study_hours': 2 },
    #                         {'Date':18,'Day':'Mon','Study_hours': 3 }
    #                      ]

    header = 'Weeks'
    labels = ['Sun','Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    data_labels = ['week #03', 'week #04']
    week_three = [3,2,2,2,2,2,0]
    week_four = [8,3,2,0,7,7,4]
    data = [week_three, week_four]
    list_of_dicts_data = {'header':header,'labels':labels,'captions':data_labels, 'data':data }


    context = {
                 "header": header,
                 "labels": labels,
                 "data_labels": data_labels,
                 "data": data,
                 "list_of_dicts_data": list_of_dicts_data
              }

    return render(request, 'chart_app/chart.html', context)


def november(request):

    header = 'November study'
    labels = ['awb','huw', 'exr', 'djp','dfd', 'dnr']
    data_labels = ['t1', 'total']
    total = [5,4,1,1,4,4]
    #day_two = [8,3,2,0,7,7,4]
    data = [total,total]
    list_of_dicts_data = {'header':header,'labels':labels,'captions':data_labels, 'data':data }

    context = {
                 "header": header,
                 "labels": labels,
                 "data_labels": data_labels,
                 "data": data,
                 "list_of_dicts_data": list_of_dicts_data
              }

    return render(request, 'chart_app/chart.html', context)



# Safely outputs a Python object as JSON,
#
# {{ value|json_script:"hello-data" }}
# <script id="hello-data" type="application/json">{"hello": "world"}</script>
# const value = JSON.parse(document.getElementById('hello-data').textContent);
#
# <script id="hello-data" type="application/json">{"hello": "world\\u003C/script\\u003E\\u0026amp;"}</script>


def nov_week_01(request):

    header = 'November week 01'

    all_data = {'awb':7, 'huw': 6, 'wlk': 2, 'exr': 4, 'fmr': 1, 'djp': 2, 'cdt': 5, 'dfd': 3,
     'dnr': 5, 'cnl': 1, 'sqz': 5, 'tcp':6, 'sfr': 5, 'hld':7, 'pds': 5, 'fwk': 4,
     'sup': 2, 'cht': 4, 'ato': 4 }

    def avg(alist):
        sum = 0
        for i in alist:
            sum = sum + i

        return sum // len(alist)


    labels = [key for key in all_data]
    data_labels = ['week01', 'middle line']
    data_set_01 = [all_data[key] for key in all_data]
    i_avg = avg(data_set_01)
    data_set_02 = [ i_avg for key in all_data]
    data = [data_set_01,data_set_02]
    list_of_dicts_data = {'header':header,'labels':labels,'captions':data_labels, 'data':data }

    context = {
                 "header": header,
                 "labels": labels,
                 "data_labels": data_labels,
                 "data": data,
                 "list_of_dicts_data": list_of_dicts_data
              }

    return render(request, 'chart_app/chart.html', context)

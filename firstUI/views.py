from django.shortcuts import render
import pandas as pd

# Create your views here.
def index(request):
    confirmedGlobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    totalCount = confirmedGlobal[confirmedGlobal.columns[-1]].sum()

    varA = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    context = {
        'totalCount': totalCount,
        'varA': varA
    }
    return render(request, 'index.html', context)
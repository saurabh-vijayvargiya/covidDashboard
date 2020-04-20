from django.shortcuts import render
import pandas as pd

# Create your views here.
def index(request):
    confirmedGlobal = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    df3 = pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
    
    totalCount = confirmedGlobal[confirmedGlobal.columns[-1]].sum()
    barPlotData = confirmedGlobal[['Country/Region', confirmedGlobal.columns[-1]]].groupby('Country/Region').sum()
    
    barPlotDate = confirmedGlobal.columns[-1]
    
    barPlotData = barPlotData.reset_index()
    barPlotData.columns = ['Country/Region', 'values']
    barPlotData = barPlotData.sort_values(by='values', ascending=False)
    countryNames = barPlotData['Country/Region'].values.tolist()
    barPlotVals = barPlotData['values'].values.tolist()

    dataForMap = []
    for i in countryNames:
        try:
            tempdf = df3[df3['name'] == i]
            temp = {}
            if (i == 'US'):
                tempdf = df3[df3['name'] == 'United States']
                temp['name'] = 'United States'
            elif(i == 'Russia'):
                tempdf = df3[df3['name'] == 'Russian Federation']
                temp['name'] = 'Russian Federation'
            else:
                temp['name'] = i
            temp['code3'] = list(tempdf['code3'].values)[0]
            temp['value'] = barPlotData[barPlotData['Country/Region']==i]['values'].sum()
            temp['code'] = list(tempdf['code'].values)[0]
            dataForMap.append(temp)
        except:
            pass

    context = {
        'totalCount': totalCount,
        'barPlotVals': barPlotVals,
        'countryNames': countryNames,
        'barPlotDate': barPlotDate,
        'dataForMap': dataForMap
    }
    return render(request, 'index.html', context)
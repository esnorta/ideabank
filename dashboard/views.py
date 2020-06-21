from django.shortcuts import render

# Create your views here.

from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
import pandas as pd

def DashView(request):
    data_path = r'C:\Users\Tim\Desktop\django\my_stuff\GPB\dashboard\data\\'
    data_name = 'criteria'
    criteria=pd.read_excel(data_path+data_name+'.xlsx', sheet_name = 'Sheet1')

    fig = px.scatter(criteria, x="deadlines", y="economic_efficiency", size='project_cost',\
                 color='Сложность реализации', trendline="ols", hover_name='paper_id',template='plotly_white',color_continuous_scale=['rgb(18,106,138)','rgb(191,191,191)','rgb(205,0,62)'])
    fig.update_layout(
                    title_text='Экономическая эффективность от времени реализации проекта', # title of plot
                    xaxis_title_text='Сроки проекта, месяцы', # xaxis label
                    yaxis_title_text='Экономическая эффективность, рублей', # yaxis label

    )

    plot_div = plot(fig,  output_type='div')

    data_name3 = 'papers'
    papers=pd.read_excel(data_path+data_name3+'.xlsx', sheet_name = 'Sheet1')
    fig = px.pie(papers, values='paper_id', names='title',color_discrete_sequence=px.colors.sequential.RdBu, hole=.4)
    fig.update_layout( title_text='Распределение идей по Группам')


    plot_div_2 = plot(fig,  output_type='div')
    return render(request, "dashboard.html", context={'plot_div': plot_div,
                                                    'plot_div_2': plot_div_2})


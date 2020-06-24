from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from django.template import RequestContext


def index(request):
    import pandas as pd
    delhi = pd.read_csv('static/DELHI.csv')

    for i in range(9):
        delhi.drop(delhi.columns[len(delhi.columns) - 1], axis=1, inplace=True)
    delhi = delhi.rename(columns={'STORE NAME': 'store_name', 'Executive Name': 'executive_name', 'PHONE 1': 'phone1',
                                  'PHONE 2': 'phone2', 'MOBILE NUMBERS': 'mobile_number',
                                  'WHATSAPP LINK': 'whatsapp_link', 'CALL SUMMARY': 'call_summary'})
    delhi.phone1.duplicated().sum()

    delhi.duplicated().sum()

    dl = delhi.loc[delhi.duplicated(), :]

    de = delhi.drop_duplicates()

    de.phone1.duplicated().sum()

    import numpy as np

    df1 = de.replace(np.nan, '', regex=True)

    df1 = de.replace(np.nan, '', regex=True)

    du_phone = de.loc[de.phone1.duplicated(), :]

    boole = []
    for length in du_phone.phone1:
        boole.append(np.nan)

    aa = pd.DataFrame(data=boole)

    aa = aa.rename(columns={0: 'phone1'})

    du_phone = du_phone.assign(phone1=aa['phone1'])
    df2 = du_phone.replace(np.nan, '', regex=True)

    de1 = df1.drop_duplicates(subset=['phone1'])
    combine = pd.concat([de1, df2])

    combine.groupby('AREA')

    r = combine.groupby('AREA')

    r = pd.value_counts(combine['AREA'])

    df = pd.DataFrame(r, columns=['AREA'])

    df.head()

    df = df.reset_index()

    df = df.rename(columns={'index': 'AREA', 'AREA': 'count'})

    df1 = df.sort_values('AREA')
    # data = df1.to_dict('split')
    # plt.figure(figsize=(16, 12))
    # sns.barplot(x='AREA', y='count', data=df1, palette='viridis')
    # plt.xticks(rotation=45, ha='right')
    # plt.tight_layout()

    # combine['call_summary'].replace('', 'not-ready', inplace=True)
    #
    # combine['call_summary'].replace(
    #     to_replace=['wrong number', 'Wrong number ', 'Not exist number', 'Upyog m nhi h call', 'Doesnot exist',
    #                 'Switched off', 'Hanged up call in middle conversation ',
    #                 'Listened everything but alast said dekhta h', 'Closed his optical work', 'Owner isnt at shop',
    #                 'Mental case waste of time', 'phone number invalid', 'Not reachable', '.',
    #                 'Response is good but atlst said no requirement rightnow', 'not interested', 'Not interested ',
    #                 'Not Interested', 'no invalid', 'number invalid', 'Hanged up call in middle conversation',
    #                 'refused for online ', 'not willing for online',
    #                 'already having online platform and was only interested in wholesale and retail',
    #                 'not interested for online platform', 'store name change'], value='not-ready', inplace=True)
    # combine['call_summary'].replace(
    #     to_replace=['busy', 'tomorrow', 'He ll look into this matter', 'Busy right now', 'Busy right  now', 'Busy',
    #                 'Response is very good and will tell tomorrow after consult with brother', 'pics pending',
    #                 'He ll also look into the matter', 'Response is good update tomorrow ', 'day after tomorrow',
    #                 'Busy right now', 'Send the model agreed with it tell me later',
    #                 'He will also talk to his elder brother and then update me', 'will ask and tell ', 'pics pending',
    #                 'pics pending till tonight', 'He will speak after 30 mins',
    #                 'He will speak after 1 hr stuck in traffic', 'wrong number', 'Will tell till tomorrow',
    #                 'Listen everything and said bta dega aapko', 'Will tell till tomorrow',
    #                 'will discuss with someone and then tell( problem in business planning)', 'will tell later',
    #                 'will confirm later', 'He will check and tell me later', 'will let know later',
    #                 'status shared till evening', 'will confirm later', 'Will tell u later', 'Will tell h after 1 hr',
    #                 'Will look into the model'], value='on-hold', inplace=True)
    # # combine['call_summary'].replace(to_replace=['wrong number,Will tell till tomorrow,Will tell till tomorrow,will discuss with someone and then tell( problem in business planning)'],value='on-hold',inplace=True)
    # combine['call_summary'].replace(
    #     to_replace=['Incoming call not available', 'Didnt pick up my call', 'All lines are closed', 'Didnt reply back',
    #                 'Wrong number', 'Wrong no.', 'Didnt pick up call', 'Switch off', 'not answering, whstapp dropped',
    #                 'did not pickup', 'Didnt pickup call', 'number out of service', 'number out of service',
    #                 'Didnt pick call'], value='no-reply', inplace=True)
    # combine['call_summary'].replace(to_replace=['mail to admin done waiting for reply', 'Very good response',
    #                                             'Very good response ll send photo later',
    #                                             'Good response, ask everything will look', 'Didnt pick up call',
    #                                             'Now donot  have interest in business so only work for 2-3 hours a day ',
    #                                             'He is ready to be on website',
    #                                             'He is interested ask everything and said will upload it later'],
    #                                 value='ready', inplace=True)
    #
    # y = combine
    #
    # pd.value_counts(combine['call_summary'])
    # #
    # # plt.subplots(figsize=(20, 10))
    # # sns.countplot(x="AREA", hue="call_summary", data=combine)
    # # plt.xticks(rotation=45, ha='right')
    # # plt.tight_layout()
    # categories = list(df1.AREA)
    # values = list(df1.count)
    # table_content = df1.to_html(index=None)
    # table_content = table_content.replace("", "")
    # table_content = table_content.replace('class="dataframe"', "class='table table-striped'")
    # table_content = table_content.replace('border="1"', "")
    # context = {"categories": categories, 'values': values, 'table_data': table_content}
    # return render(request, 'index.html', context=context)


    """
    discretebarchart page
    """
    xdata = list(df1.AREA)
    ydata =list(df1.count)

    chartdata = {'x': xdata, 'y1': ydata}
    charttype = "discreteBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render('index.html', data)
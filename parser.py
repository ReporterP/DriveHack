import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime
import pandas as pd  # для создания/дополнения файла отчёта через DataFrames
import re

# Формирование отчёта из данных от парсеров
def update_report(data: dict, report_path = r'./report_data.csv'):
    '''Extend existing report or create a new one'''
    if report_path == "":
        report_data = pd.DataFrame(
            columns=['company_name', 'mentioned_times'])
    else:
        report_data = pd.read_csv(report_path)

    # Дополнение отчёта данными
    # Словарь в DF, а DF + DF
    # print(pd.DataFrame(data.items())) # , ignore_index=True
    report_data = pd.concat([report_data, pd.DataFrame([data.values()],columns=['company_name', 'mentioned_times'] )])

    # TODO:
    # Для оптимизации имеет смысл делать сохранение в csv, только тогда, когда получен итоговый DF
    # Т.е. парсер прекратил свою работу.
    report_data.to_csv('report_data.csv', index=False)


transport_st = []
result = []
other_st = []

# load the list of transport startups
correct_list = 'https://transport.startups-list.com/'

# resourses
url = ['https://techcrunch.com/category/startups/', 'https://techstartups.com/category/latest-technology-news/transportation/', 'https://www.eu-startups.com/?s=transport']

def list_load(url):
    r = req.get(url)
    html = bs(r.text, 'html.parser')
    for new in html.select('.card'):
        name = new.select('h1')[0].text.strip()
        transport_st.append(name)


# parser
def parser(url, transport_st, result, other_st):
    list_load(correct_list)

    for u in url:
        
        # if url.index(u) == 0:
            # r = req.get(u)
            # html = bs(r.text, 'html.parser')
        #     for new in html.select('.post-block'):
        #         title = new.select('h2 > a')[0].text.strip()
        #         date = new.select('time')[0].text.strip()
        #         print(new)
        #         break
        
        if url.index(u) == 1:
            for page in range(1, 100):
                if page >= 2:
                    u = f'https://techstartups.com/category/latest-technology-news/transportation/page/{page}/'
                r = req.get(u)
                html = bs(r.text, 'html.parser')
                for new in html.select('.post'):
                    title = new.select('h5 > a')[0].text.strip()
                    date = new.select('.post_info_date')[0].text.strip()
                    date = date.replace(',', '')
                    date = datetime.strptime('April 25 2022', '%B %d %Y')
                    date = date.strftime("%Y-%m-%d")
                    # for tr in transport_st:
                    #     if tr in title:
                    #         result.append({"company_name": tr, "mentioned_at": date})
                    #         # print({"company_name": tr, "mentioned_at": date})
                    #         break
                    if 'startup' in title:
                        if '$' in title:
                            # print(title)
                            find_str = re.findall(r'startup(.*?)[$]', title)
                            if len(find_str):
                                find_str = find_str[0].replace('\xa0', ' ').strip().split(' ')
                                # print(f'"{find_str}"')
                                w = 0
                                res = ''
                                while find_str[w][0].isupper():
                                    res += f'{find_str[w]} '
                                    w +=1
                            res = res.strip()        
                            update_report({"company_name": res, "mentioned_at": date})

        # if url.index(u) == 2:
        #     for new in html.select('.td-module-meta-info'):
        #         title = new.select('h3 > a')[0].text.strip()
        #         date = new.select('.entry-date')[0].text.strip()
        #         print(title, data)
        #         break
            

# data_parser = parser(url, transport_st, result, other_st)
parser(url, transport_st, result, other_st)
# print(data_parser)
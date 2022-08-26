import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime
import pandas as pd  # для создания/дополнения файла отчёта через DataFrames
import re


transport_st = []

# resourses
url = ['https://techstartups.com/category/latest-technology-news/transportation/', 'https://www.eu-startups.com/?s=transport', 'https://inc42.com/buzz/?s=transport%20startup', 'https://www.geekwire.com/?s=transport&orderby=relevance&order=DESC&post_type=post%2Cpage%2Cdevblog%2Cgeekwire_event%2Cgeekwire_picks%2Cspecial_coverage%2Csponsor_post&category_name=transportation', 'https://startupnews.com.au/?s=transport']
news_selector = ['.post', '.tdb_module_loop ', '.content', 'article', 'item-details']
error_selector = ['.inner_wrapper > .error_box', '.error404', '.ais-Hits--empty', '.error404', '.error404']
title_selector = ['h5 > a', 'h3 > a', 'h2 > a', 'h2 > a', 'h3 > a']
date_selector = ['.post_info_date', '.entry-date', '.date', '.published', '.entry-date']



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

# Парсинг данных в DataFrame с сохранением в csv по завершению
def parser(url, transport_st):
    for u in url:
        ind = url.index(u)
        page = 1
        while True:
            if page >= 2:
                if ind == 0:
                    u = f'https://techstartups.com/category/latest-technology-news/transportation/page/{page}/'
                elif ind == 1:
                    u = f'https://www.eu-startups.com/page/{page}/?s=transport'
                elif ind == 2:
                    u = f'https://inc42.com/buzz/?s=transport%20startup&page={page}'
                elif ind == 3:
                    u = f'https://www.geekwire.com/page/{page}/?s=transport&orderby=relevance&order=DESC&post_type=post%2Cpage%2Cdevblog%2Cgeekwire_event%2Cgeekwire_picks%2Cspecial_coverage%2Csponsor_post&category_name=transportation'
                elif ind == 4:
                    u = f'https://startupnews.com.au/page/{page}/?s=transport'
            r = req.get(u)
            # print()
            # print(u)
            # print()
            html = bs(r.text, 'html.parser')
            if len(html.select(error_selector[ind])) == 0:
                
                for new in html.select(news_selector[ind]):
                    title = new.select(title_selector[ind])[0].text.strip()
                    date = new.select(date_selector[ind])[0].text.strip()
                    date = date.replace(',', '')
                    date = datetime.strptime(date, '%B %d %Y')
                    date = date.strftime("%Y-%m-%d")

                    for tr in transport_st:
                        if tr in title:
                            # print(f't"{title}" tr"{tr}"')
                            update_report({"company_name": tr, "mentioned_at": date})
                    if 'startup' in title:
                        if '$' in title or '€' in title:
                            # print(title)
                            find_str = re.findall(r'startup(.*?)[$€]', title)
                            if len(find_str):
                                # print(title)
                                find_str = find_str[0].replace('\xa0', ' ').strip().split(' ')
                                # print(f'"{find_str}"')
                                w = 0
                                res = ''
                                while find_str[w][0].isupper():
                                    res += f'{find_str[w]} '
                                    w +=1
                                res = res.strip()
                                if len(res):            
                                    update_report({"company_name": res, "mentioned_at": date})
                                    transport_st.append(res)
                page +=1
            else:
                break


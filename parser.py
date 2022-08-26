import requests as req
from bs4 import BeautifulSoup as bs
from datetime import datetime
import pandas as pd  # для создания/дополнения файла отчёта через DataFrames
import re

# load the list of transport startups
# correct_list = 'https://transport.startups-list.com/'
# def list_load(url):
#     r = req.get(url)
#     html = bs(r.text, 'html.parser')
#     for new in html.select('.card'):
#         name = new.select('h1')[0].text.strip()
#         transport_st.append(name)

# Парсинг данных в DataFrame с сохранением в csv по завершению
def parser(url, transport_st):
    # DF заполняемый парсером
    parsed_data = pd.DataFrame(columns=['company_name', 'mentioned_times'])

    # list_load(correct_list)
    for u in url:
        ind = url.index(u)
        page = 1
        while True:
            if page >= 2:
                if ind == 0:
                    u = f'https://techstartups.com/category/latest-technology-news/transportation/page/{page}/'
                elif ind == 1:
                    u = f'https://www.eu-startups.com/page/{page}/?s=transport'
            r = req.get(u)
            print()
            print(u)
            print()
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
                            print(f't"{title}" tr"{tr}"')
                            print({"company_name": tr, "mentioned_at": date})
                    if 'startup' in title:
                        if '$' in title or '€' in title:
                            # print(title)
                            find_str = re.findall(r'startup(.*?)[$€]', title)
                            if len(find_str):
                                print(title)
                                find_str = find_str[0].replace('\xa0', ' ').strip().split(' ')
                                # print(f'"{find_str}"')
                                w = 0
                                res = ''
                                while find_str[w][0].isupper():
                                    res += f'{find_str[w]} '
                                    w += 1
                                res = res.strip()
                                if len(res):
                                    # Дополнение отчёта данными
                                    startup = {"company_name": res, "mentioned_at": date}
                                    parsed_data = pd.concat([parsed_data, pd.DataFrame([startup.values()],
                                                                                       columns=['company_name',
                                                                                                'mentioned_times'])])
                                    transport_st.append(res)
                page += 10
            else:
                break

        # if url.index(u) == 0:
        # r = req.get(u)
        # html = bs(r.text, 'html.parser')
        #     for new in html.select('.post-block'):
        #         title = new.select('h2 > a')[0].text.strip()
        #         date = new.select('time')[0].text.strip()
        #         print(new)
        #         break

    return parsed_data


transport_st = []
other_st = []

# resourses
url = ['https://techstartups.com/category/latest-technology-news/transportation/',
       'https://www.eu-startups.com/?s=transport']
news_selector = ['.post', '.tdb_module_loop ']
error_selector = ['.inner_wrapper > .error_box', '.error404']
title_selector = ['h5 > a', 'h3 > a']
date_selector = ['.post_info_date', '.entry-date']

# Парсер возращает новый DF, что содержит собранные данные.
parsed_data = parser(url, transport_st)

# Загрузка имеющегося отчёта в DF, для дополнения
report_path = r'G:\GitHub repos\DriveHack\report_data.csv'
report_data = pd.read_csv(report_path)

# Дополнение DF отчёта данными из DF с результатами парсинга
report_data = pd.concat([report_data, parsed_data])

# Сохранение результирующего DF в csv
report_data.to_csv('report_data.csv', index=False)

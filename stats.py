import pandas as pd  # для создания/дополнения файла отчёта через DataFrames
from datetime import date #


# Выгрузка топ 10 (словарь + csv)
def get_best(start_date: str, final_date: str, report_path = r'./report_data.csv'):
    '''start_date and final_date are included'''

    start_date = date.fromisoformat(start_date)
    final_date = date.fromisoformat(final_date)
    report_data = pd.read_csv(report_path)


    stats = {}

    for _, row in report_data.iterrows():
        if start_date <= date.fromisoformat(row["mentioned_at"]) <= final_date:
            stats[row['company_name']] = stats.get(row['company_name'], 0) + 1

    stats = sorted(stats.items(), key=lambda x: x[1])


    if len(stats) > 10:
        stats = dict(stats[:10])
    else:
        stats = dict(stats)


    # Формирование csv 10 лучших
    pd.DataFrame(stats.items(), columns=['company_name', 'mentioned_times']).to_csv('most_mentioned.csv', index=False)

    # Словарь 10 лучших, для визуализации на фронтенде
    return stats


# Только для теста get_best
'''

report_path = r'./report_data.csv'

start_date = "2000-01-01"
final_date = "2030-01-01"

print(get_best(start_date, final_date, report_path))
'''

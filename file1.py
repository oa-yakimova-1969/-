def filter_by_state(data_list, state='EXECUTED'):
    """Сортирует список по введенному ключу"""
    filtered_list = []
    for data in data_list:
        if data.get('state') == state:
            filtered_list.append(data)
            return filtered_list
        else:
            return "Некорректный ввод"





import sqlite3
import pprint



def get_result(sql):
    """
    Установить соединение с БД. Получить данные, исходя из запроса
    :param sql: запрос
    :return: данные
    """
    with sqlite3.connect("netflix.db") as con:
        con.row_factory = sqlite3.Row
        result = []
        for item in con.execute(sql).fetchall():
            s = dict(item)

            result.append(s)

        return result


def search_by_cast(name1, name2):
    """
    Получить выборку исходя из имен 2 актеров
    :param name1: имя 1 актера
    :param name2: имя 2 актера
    :return:
    """
    sql = '''
    SELECT *
    FROM netflix n 
    WHERE "cast" LIKE '%Rose McIver%' and "cast" LIKE '%Ben Lamb%'
    AND (
    SELECT COUNT(1)
    FROM netflix n
    WHERE "cast" LIKE '%Rose McIver%' and "cast" LIKE '%Ben Lamb%') >= 2 '''

    cast = []
    result = get_result(sql)
    for item in result:
        if name1 in item.get("cast") and name2 in item.get("cast"):
            cast.append(item.get("cast"))
    if len(cast) >= 2:
        return cast



def search_by_parameters(_type, release_year, genre):
    """
    Получить выборку из указанных параметров
    :param _type: тип произведения, фильм или сериал
    :param release_year: год выхода на экраны
    :param genre: жанр
    :return: выборка
    """
    sql = f'''
        SELECT *
        FROM netflix n
        WHERE "type" = "{_type}" 
        and "release_year" = "{release_year}" 
        and listed_in = "{genre}" '''

    return get_result(sql)




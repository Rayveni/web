# параметры
передаются в словаре c ключами:
* host
* port
* db_name all_tables
# методы
* **drop_db** -удаляет базу
* **all_tables** -список таблиц 
* **dbstats**- статиска базы данных
* **table_exists**(*table_name*) -проверка наличия таблицы
* **get_table**(*table*,*condition*,*query*-подзапрос к таблице,*columns*-список возвращаемых колонок) -возвращает курсор на таблицу
* **agg**(*table_name*,*group*-группируемые поля,*agg_functions_list*-список агрегирующих функций -возвращает курсор на таблицу
* **merge**
* **find_one**


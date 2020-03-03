from sys import path
path.append("...")
from attributes import sec_history_manager,fond_index_history

def job_world_fond_indexes(db_manager)->tuple:
    alphavantage_token=db_manager.find_one('api_tokens',
                                           query={ 'key': { '$eq': 'alphavantage' } },
                                           return_fields=['value'])['value']
    r=db_manager.insert_into_table_from_attr(table_name='upload_info',data_attr=row,update_criteria={"sys_name":sys_name} )
    return r

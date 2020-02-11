from .config_manager import config_manager

from sys import path
path.append("...")
from db_drivers import mongo_manager


def init_db_manager():
    cfm=config_manager()	
    err,config=cfm.read_config()
    return mongo_manager(config)
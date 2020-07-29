from sys import path
path.append("...")

#from db_drivers import mongo_manager
from attributes import securities_short
from external_sources import mosex
from .upload_info import update_upload_table_info
from datetime import datetime



def job_mosex_securities(db_manager)->tuple:
    columns= ['DATESTAMP', 'INSTRUMENT_ID', 'LIST_SECTION','SUPERTYPE', 'INSTRUMENT_TYPE', 'INSTRUMENT_CATEGORY', 'TRADE_CODE', 'ISIN', 'REGISTRY_NUMBER', 'REGISTRY_DATE', 'EMITENT_FULL_NAME', 'INN', 'NOMINAL', 'CURRENCY', 'ISSUE_AMOUNT', 'DECISION_DATE', 'OKSM_EDR', 'ONLY_EMITENT_FULL_NAME', 'REG_COUNTRY', 'QUALIFIED_INVESTOR', 'HAS_PROSPECTUS', 'IS_CONCESSION_AGREEMENT', 'IS_MORTGAGE_AGENT', 'INCLUDED_DURING_CREATION', 'SECURITY_HAS_DEFAULT', 'SECURITY_HAS_TECH_DEFAULT', 'INCLUDED_WITHOUT_COMPLIANCE', 'RETAINED_WITHOUT_COMPLIANCE', 'HAS_RESTRICTION_CIRCULATION', 'LISTING_LEVEL_HIST', 'OBLIGATION_PROGRAM_RN', 'COUPON_PERCENT', 'EARLY_REPAYMENT', 'EARLY_REDEMPTION', 'ISS_BOARDS', 'OTHER_SECURITIES', 'DISCLOSURE_PART_PAGE', 'DISCLOSURE_RF_INFO_PAGE']
    df=mosex().securities_list()
    upload_arr=[securities_short(*v.values) for i,v in df[columns].iterrows()]	
    res=db_manager.insert_into_table_from_attr('mosex_securities',upload_arr,bulk=True,rewrite=True)
    res2=update_upload_table_info(db_manager,'mosex_securities',res[1])
    return res





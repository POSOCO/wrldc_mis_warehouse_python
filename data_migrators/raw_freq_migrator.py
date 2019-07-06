# -*- coding: utf-8 -*-
'''
[(20180222, '09:57:20', 49.921), (20180222, '09:57:30', 49.9292), (20180222, '09:57:40', 49.9311), (20180222, '09:57:50', 49.9327), (20180222, '09:58:00', 49.9296)]
'''
import cx_Oracle
import datetime as dt

from data_helpers.raw_freq_data_helper import RawFreqDataHelper
from data_models.mis_db_helper import getDbConfig
from data_models.raw_freq_model import RawFreq
from uat_data_source_config import getUATDataSourceConnString

from_dt = dt.datetime(2019, 7, 2, 1, 2, 3)
to_dt = dt.datetime(2019, 7, 3, 4, 5, 6)

def migrateRawFreqData(from_dt, to_dt):
    from_date_key = int(from_dt.strftime('%Y%m%d'))
    #from_time_key = from_dt.strftime('%H:%M:%S')
    to_date_key = int(to_dt.strftime('%Y%m%d'))
    #to_time_key = to_dt.strftime('%H:%M:%S')
    
    oracle_connection_string = getUATDataSourceConnString()
    con = cx_Oracle.connect(oracle_connection_string)
    cur = con.cursor()
    
    cur.prepare('SELECT DATE_KEY, TIME_KEY, FREQ_VAL FROM STG_SCADA_FREQUENCY_NLDC where DATE_KEY between :from_date_key and :to_date_key and ISDELETED = :isdeleted order by DATE_KEY, TIME_KEY')
    
    cur.execute(None, {'isdeleted': 0, 'from_date_key': from_date_key, 'to_date_key':to_date_key})
    res = cur.fetchall()
    # print(res)  
        
    cur.close()
    
    rawFreqDataHelper = RawFreqDataHelper(getDbConfig())
    for freqRow in res:
        rawFreq = RawFreq(data_time=dt.datetime.strptime(str(freqRow[0])+' '+freqRow[1], '%Y%m%d %H:%M:%S'), freq= freqRow[2])
        rawFreqDataHelper.AddRawFreqData(rawFreq)

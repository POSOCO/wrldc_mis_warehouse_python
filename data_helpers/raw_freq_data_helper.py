# -*- coding: utf-8 -*-
"""
Created on Thu Jul 4 22:55:25 2019

@author: Nagasudhir
"""
from data_models.mis_db_helper import MISDBHelper
from data_models.raw_freq_model import RawFreq
from sqlalchemy.orm import sessionmaker

class RawFreqDataHelper:
    db_config_dict = None
    db_helper = None
    session= None
    
    # constructor
    def __init__(self, db_config_dict):
        self.db_config_dict = db_config_dict
        self.db_helper = MISDBHelper(db_config_dict)
        # create db if not present
        self.db_helper.create_db()
        # create session
        Session = sessionmaker()
        Session.configure(bind=self.db_helper.get_engine())
        # open session
        self.session = Session()
    
    def AddRawFreqData(self, raw_freq, updateExisting=True):
        if(raw_freq != None):
            # check if event_log is already present
            queriedEvent = self.session.query(RawFreq).filter(RawFreq.data_time==raw_freq.data_time).first()
            if not queriedEvent:
                # add the event_log and commit
                self.session.add(raw_freq)
                self.session.commit()
            else:
                # The event_log is already present
                if(updateExisting == True):
                    # update the deviceType only if desired else donot add the event_log
                    queriedEvent.freq = raw_freq.freq
                    self.session.commit()
    
    def GetRawFreqData(self, args_obj):
        from_time = args_obj['from_time']
        to_time = args_obj['to_time']
        queriedEvents = self.session.query(RawFreq).filter(RawFreq.data_time.between(from_time, to_time)).order_by(RawFreq.data_time.desc())
        return queriedEvents
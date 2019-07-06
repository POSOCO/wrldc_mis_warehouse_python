# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 22:25:25 2019

@author: Nagasudhir
# 23.5141 has a precision of 6 and a scale of 4. - https://www.postgresql.org/docs/9.6/datatype-numeric.html
"""

from sqlalchemy import Column, Integer, Numeric, String, DateTime, UniqueConstraint
# from sqlalchemy.orm import relationship
# from sqlalchemy.exc import SQLAlchemyError
from data_models.mis_db_helper import Base
# Base = declarative_base()


class RawFreq(Base):
    __tablename__ = 'raw_freq'
    id = Column(Integer, primary_key=True)
    freq = Column(Numeric(precision=5, scale=3), nullable=False)
    data_time = Column(DateTime, nullable=False, unique=True)

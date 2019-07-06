# -*- coding: utf-8 -*-
import datetime as dt
from data_migrators.raw_freq_migrator import migrateRawFreqData

from_dt = dt.datetime(2019, 7, 2, 1, 2, 3)
to_dt = dt.datetime(2019, 7, 3, 4, 5, 6)
migrateRawFreqData(from_dt, to_dt)
__author__ = 'jay'


import task.util
from task.util import *
import os

"""
    Device ykk task
"""

@app.task
@use_db
def get_checkRecord_list_task():
    line_list_dicts = []
    line_lists = db.query_by_filename("CHECK_RECORD", {"fileName": "ykk_record_A_01_2017-08-05"})
    if len(line_list_dicts) != 0:
         return line_list_dicts
    else:
        return None


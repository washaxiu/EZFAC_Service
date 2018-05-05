__author__ = 'jay'


import task.util
from task.util import *
import os

"""
    Device ykk task
"""

@app.task
@use_db
def get_checkRecord_list_task(table_name):
    line_list_dicts = []
    line_lists = db.query_by_filename(table_name, {"fileName": "ykk_record_A_01_2017-08-05"})
    if len(line_list_dicts) != 0:
         return line_list_dicts
    else:
        return None

@app.task
@use_db
def add_checkRecord_task(cfg):
    ret = False
    if len(cfg) !=0:
        ret = db.insertOrUpdate("CHECK_RECORD",{'fileName': cfg['fileName'], 'type': cfg['type'],
                                        'group1': cfg['group1'], 'number': cfg['number'],
                                        'temp1': cfg['temp1'], 'temp2': cfg['temp2'],
                                        'temp3': cfg['temp3'], 'loop1': cfg['loop1'],
                                        'loop2': cfg['loop2'], 'loop3': cfg['loop3'],
                                        'select1': cfg['select1'], 'plat1': cfg['plat1'],
										'edit': cfg['edit']})
    return ret

@app.task
@use_db
def get_userInfo_task():
    line_lists = db.query_all("USER")
    if len(line_lists) != 0:
         return line_lists
    else:
        return None


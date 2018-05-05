__author__ = 'jay'


import task.util
from task.util import *
import os

"""
    Device ykk task
"""

@app.task
@use_db
def get_checkRecord_list_task(cfg):
    table_name = cfg['table_name']
    level = cfg['level']
    line_lists = db.query_dataInfo(table_name, level)
    return line_lists

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
def add_checkerInfo_task(cfg):
    ret = False
    if len(cfg) !=0:
        ret = db.insertOrUpdate("CHECKER_INFO",{'fileName': cfg['fileName'], 'edit': cfg['edit'], 'isCheck': cfg['isCheck'],'level': cfg['level'],
                                 'name1': cfg['name1'], 'name2': cfg['name2'], 'name3': cfg['name3'], 'name4': cfg['name4'],'name5': cfg['name5'],
			         'date1': cfg['date1'], 'date2': cfg['date2'], 'date3': cfg['date3'], 'date4': cfg['date4'],'date5': cfg['date5'],
			         'comments1': cfg['comments1'], 'comments2': cfg['comments2'], 'comments3': cfg['comments3'],
			         'comments4': cfg['comments4'],'comments5': cfg['comments5']})
    return ret

@app.task
@use_db
def get_userInfo_task():
    line_lists = db.query_all("USER")
    if len(line_lists) != 0:
         return line_lists
    else:
        return None


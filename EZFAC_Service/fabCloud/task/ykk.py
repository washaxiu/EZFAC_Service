__author__ = 'Spring'


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
    #line_lists = db.query_by_filename("check_record", {"file_name": file_name})
    # if line_lists:
    #     for line_list in line_lists:
    #         line_dict = {}
    #         line_dict['id'] = line_list['id']
    #         line_dict['line_name'] = line_list['line_name']
    #         line_dict['line_type_id'] = line_list['line_type_id']
    #         line_dict['current_status'] = line_list['current_status']
    #         line_dict['description'] = line_list['description']
    #         line_dict['enable'] = line_list['enable']
    #         line_dict['threshold'] = line_list['threshold']
    #         line_dict['timeout'] = line_list['timeout']
    #         line_dict['worktime'] = line_list['worktime']
    #         line_list_dicts.append(line_dict)
    line_dict = {}
    line_dict['type'] = 'DieCasting'
    line_dict['group'] = 'A'
    line_dict['number'] = '01'
    line_list_dicts.append(line_dict)
    if len(line_list_dicts) != 0:
         return line_list_dicts
    else:
        return None


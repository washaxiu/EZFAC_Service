__author__ = 'Spring'


import task.util
from task.util import *
import os

"""
    Device ykk task
"""

@app.task
@use_db
def get_maintenanceLog_task():
    line_list_dicts = []
    line_lists = db.query_by_filename("MAINTENANCE_LOG", {"file_name": file_name})
     if line_lists:
         for line_list in line_lists:
             line_dict = {}
             line_dict['fileName'] = line_list['fileName']
             line_dict['MachineGroup'] = line_list['MachineGroup']
             line_dict['machineNo'] = line_list['machineNo']
             line_dict['item'] = line_list['item']
             line_dict['personInCharge'] = line_list['personInCharge']
             line_dict['separateStatus'] = line_list['separateStatus']
             line_dict['gneck'] = line_list['gneck']
             line_dict['HS_Num'] = line_list['HS_Num']
             line_dict['remark'] = line_list['remark']
			 line_dict['surface'] = line_list['surface']
             line_dict['damage_SB171'] = line_list['damage_SB171']
             line_dict['PINDamage'] = line_list['PINDamage']
             line_dict['damage_SB251'] = line_list['damage_SB251']
			 line_dict['filling'] = line_list['filling']
             line_dict['xingpian'] = line_list['xingpian']
             line_dict['b3_b4_b5_b7'] = line_list['b3_b4_b5_b7']
             line_dict['b6'] = line_list['b6']
		     line_dict['c8_c9_c10'] = line_list['c8_c9_c10']
             line_dict['coreWash'] = line_list['coreWash']
             line_list_dicts.append(line_dict)
    line_dict = {}

    line_list_dicts.append(line_dict)
    if len(line_list_dicts) != 0:
         return line_list_dicts
    else:
        return None

@app.task
@use_db
def get_semiFinishedCheck_task():
    line_list_dicts = []
    line_lists = db.query_by_filename("SEMI_FINISHED_CHECK", {"file_name": file_name})
     if line_lists:
         for line_list in line_lists:
             line_dict = {}
             line_dict['fileName'] = line_list['fileName']
             line_dict['MachineGroup'] = line_list['MachineGroup']
             line_dict['MachineId'] = line_list['MachineId']
             line_dict['Temp1'] = line_list['Temp1']
             line_dict['Temp2'] = line_list['Temp2']
             line_dict['Temp3'] = line_list['Temp3']
             line_dict['Temp4'] = line_list['Temp4']
             line_dict['Temp5'] = line_list['Temp5']
             line_dict['Temp6'] = line_list['Temp6']
			 line_dict['Temp7'] = line_list['Temp7']
             line_dict['Temp8'] = line_list['Temp8']
             line_dict['reviewInfor'] = line_list['reviewInfor']
             line_list_dicts.append(line_dict)
    line_dict = {}

    line_list_dicts.append(line_dict)
    if len(line_list_dicts) != 0:
         return line_list_dicts
    else:
        return None

@app.task
@use_db
def get_YZGCMonthRecord_task():
    line_list_dicts = []
    line_lists = db.query_by_filename("YZGC_MONTH_RECORD", {"file_name": file_name})
     if line_lists:
         for line_list in line_lists:
             line_dict = {}
             line_dict['fileName'] = line_list['fileName']
             line_dict['jiFan'] = line_list['jiFan']
             line_dict['pinMing'] = line_list['pinMing']
             line_dict['SHOT'] = line_list['SHOT']
             line_dict['element1'] = line_list['element1']
             line_dict['element2'] = line_list['element2']
             line_dict['element3'] = line_list['element3']
             line_dict['element4'] = line_list['element4']
             line_dict['element5'] = line_list['element5']
			 line_dict['element6'] = line_list['element6']
             line_dict['element7'] = line_list['element7']
             line_dict['element8'] = line_list['element8']
             line_dict['element9'] = line_list['element9']
			 line_dict['element10'] = line_list['element10']
             line_dict['element11'] = line_list['element11']
             line_dict['element12'] = line_list['element12']
             line_dict['maintainReason'] = line_list['maintainReason']
		     line_dict['reviewInfor'] = line_list['reviewInfor']
             line_dict['MaintenResult'] = line_list['MaintenResult']
             line_dict['createDate'] = line_list['createDate']
             line_list_dicts.append(line_dict)
    line_dict = {}

    line_list_dicts.append(line_dict)
    if len(line_list_dicts) != 0:
         return line_list_dicts
    else:
        return None


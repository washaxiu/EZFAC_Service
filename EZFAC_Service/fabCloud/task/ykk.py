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
def add_dailyCheckMorning_task(cfg):
    ret = False
    if len(cfg) !=0:
        ret = db.insertOrUpdate("DAILY_CHECK_MORNING",{'fileName': cfg['fileName'], 'type': cfg['type'],
                                'group1': cfg['group1'], 'number': cfg['number'],'work':cfg['work'],'first':cfg['first'],
                                'two':cfg['two'],'three':cfg['three'],'five':cfg['five'],'six':cfg['six'],
                                'seven':cfg['seven'],'eight':cfg['eight'],'fourteen':cfg['fourteen'],'fifteen':cfg['fifteen'],
                                'sixteen':cfg['sixteen'],'seventeen':cfg['seventeen'],'eighteen':cfg['eighteen'],'four':cfg['four'],
                                'zhouqi':cfg['zhouqi'],'nozzleTemp':cfg['nozzleTemp'],'GOOSENECKTemp':cfg['GOOSENECKTemp'],
                                'fuTemp1':cfg['fuTemp1'],'fuTemp2':cfg['fuTemp2'],
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
    return line_lists

@app.task
@use_db
def add_dailyCheckNoon_task(cfg):
    ret = False
    if len(cfg) !=0:
        ret = db.insertOrUpdate("DAILY_CHECK_NOON",{'fileName': cfg['fileName'], 'type': cfg['type'],
                                'group1': cfg['group1'], 'number': cfg['number'],'machineModel':cfg['machineModel'],
								'work':cfg['work'],'first':cfg['first'],'two':cfg['two'],'three':cfg['three'],'five':cfg['five'],
								'six':cfg['six'],'seven':cfg['seven'],'eight':cfg['eight'],'nine':cfg['nine'],'fourteen':cfg['fourteen'],
								'fifteen':cfg['fifteen'],'sixteen':cfg['sixteen'],'seventeen':cfg['seventeen'],'four':cfg['four'],
                                'ten':cfg['ten'],'eleven':cfg['eleven'],'twelve':cfg['twelve'],'checkEdit':cfg['checkEdit']})
    return ret

@app.task
@use_db
def add_SemiFinishCheck_task(cfg):
    ret = False
    if len(cfg) !=0:
        ret = db.insertOrUpdate("SEMI_FINISHED_CHECK",{'fileName':cfg['fileName'],'type':cfg['type'],'group1':cfg['group1'],
        'number':cfg['number'],'item':cfg['item'],'personInCharge':cfg['personInCharge'],'separateStatus':cfg['separateStatus'],
        'gneck':cfg['gneck'],'HS_Num':cfg['HS_Num'],'remark':cfg['remark'],'surface':cfg['surface'],'damage_SB171':cfg['damage_SB171'],
        'PINDamage':cfg['PINDamage'],'damage_SB251':cfg['damage_SB251'],'filling':cfg['filling'],'xingpian':cfg['xingpian'],'b3_b4_b5_b7':cfg['b3_b4_b5_b7'],
        'b6':cfg['b6'],'c8_c9_c10':cfg['c8_c9_c10'],'coreWash':cfg['coreWash'],'checkEdit':cfg['checkEdit']})
    return ret
    
@app.task
@use_db
def add_YZGCMonthRecord_task(cfg):
    ret = False
    if len(cfg) !=0:
        ret = db.insertOrUpdate("YZGC_MONTH_RECORD",{'fileName':cfg['fileName'],'type':cfg['type'],'group1':cfg['group1'],'number':cfg['number'],'Temp1':cfg['Temp1'],'Temp2':cfg['Temp2'],
        'Temp3':cfg['Temp3'],'Temp4':cfg['Temp4'],'Temp5':cfg['Temp5'],'Temp6':cfg['Temp6'],'Temp7':cfg['Temp7'],'Temp8':cfg['Temp8'],'checkEdit':cfg['checkEdit']})
    return ret

@app.task
@use_db
def add_maintenanceLog_task(cfg):
    ret = False
    if len(cfg) !=0:
        ret = db.insertOrUpdate("MAINTENANCE_LOG",{'fileName': cfg['fileName'], 'type': cfg['type'],
                                'lineName': cfg['lineName'], 'elementName': cfg['elementName'],'SHOTNumber':cfg['SHOTNumber'],
								'SB171':cfg['SB171'],'SB172':cfg['SB172'],'SB241':cfg['SB241'],'SB242':cfg['SB242'],'SB243':cfg['SB243'],
								'SB244':cfg['SB244'],'SB245':cfg['SB245'],'SB251':cfg['SB251'],'SB252':cfg['SB252'],'SB253':cfg['SB253'],
								'SB254':cfg['SB254'],'SB255':cfg['SB255'],'maintainReason':cfg['maintainReason'],'reviewInfor':cfg['reviewInfor'],
                                'MaintenResult':cfg['MaintenResult'],'checkEdit':cfg['checkEdit']})
    return ret
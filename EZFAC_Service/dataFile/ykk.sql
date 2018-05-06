DROP SCHEMA IF EXISTS `ykk` ;
CREATE SCHEMA IF NOT EXISTS `ykk` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `ykk` ;

/* 审批信息表 */
DROP TABLE IF EXISTS `ykk`.`CHECKER_INFO` ;
CREATE TABLE IF NOT EXISTS  `ykk`.`CHECKER_INFO`(
       `fileName`         VARCHAR(255) not null PRIMARY KEY comment '文件名',
       `name1`            VARCHAR(255) comment '审批人名称',
	   `name2`            VARCHAR(255) comment '审批人名称',
	   `name3`            VARCHAR(255) comment '审批人名称',
	   `name4`            VARCHAR(255) comment '审批人名称',
	   `name5`            VARCHAR(255) comment '审批人名称',
       `level`            VARCHAR(255) comment '审批人等级',
       `isCheck`          VARCHAR(255) comment '是否审批',
       `edit`             VARCHAR(255) comment '是否编辑',
       `date1`            VARCHAR(255) comment '审批时间',
	   `date2`            VARCHAR(255) comment '审批时间',
	   `date3`            VARCHAR(255) comment '审批时间',
	   `date4`            VARCHAR(255) comment '审批时间',
	   `date5`            VARCHAR(255) comment '审批时间',
       `comments1`        VARCHAR(255) comment '备注',
	   `comments2`        VARCHAR(255) comment '备注',
	   `comments3`        VARCHAR(255) comment '备注',
	   `comments4`        VARCHAR(255) comment '备注',
	   `comments5`        VARCHAR(255) comment '备注',
       `createDate`      VARCHAR(255) comment '创建日期'
);

/*  点检记录表 */
DROP TABLE IF EXISTS `ykk`.`CHECK_RECORD` ;
CREATE TABLE IF NOT EXISTS `ykk`.`CHECK_RECORD` (
       `fileName`        VARCHAR(255) not null comment '文件名',
       `type`            VARCHAR(255) comment '点检类型',
       `group1`          VARCHAR(255) comment '机组',
       `number`          VARCHAR(255) comment '机番',
       `temp1`           VARCHAR(255),
       `temp2`           VARCHAR(255),
       `temp3`           VARCHAR(255),
       `loop1`           VARCHAR(255),
       `loop2`           VARCHAR(255),
       `loop3`           VARCHAR(255),
       `select1`         VARCHAR(255),
       `plat1`           VARCHAR(255),
       `edit`            VARCHAR(255) comment '是否编辑 0否 1是',
       `createDate`      VARCHAR(255) comment '创建时间',
		PRIMARY KEY (`fileName`)
);


/*  早班点检记录表 */
DROP TABLE IF EXISTS `ykk`.`DAILY_CHECK_MORNING` ;
CREATE TABLE IF NOT EXISTS  `ykk`.`DAILY_CHECK_MORNING`(
       `fileName`        VARCHAR(255) not null comment '文件名',
       `type`            VARCHAR(255) comment '点检类型',
       `group`           VARCHAR(255) comment '机组',
       `number`          VARCHAR(255) comment '机番 0否 1是',
       `machineModel`    VARCHAR(255),
       `work`            VARCHAR(255),
       `first`           VARCHAR(255),
       `two`             VARCHAR(255),
       `three`           VARCHAR(255),
       `five`            VARCHAR(255),
       `six`             VARCHAR(255),
       `seven`           VARCHAR(255),
       `eight`           VARCHAR(255),
       `fourteen`        VARCHAR(255),
       `fifteen`         VARCHAR(255),
       `sixteen`         VARCHAR(255),
       `seventeen`       VARCHAR(255),
       `eighteen`        VARCHAR(255),
       `four`            VARCHAR(255),
       `zhouqi`          VARCHAR(255),
       `nozzleTemp`      VARCHAR(255),
       `GOOSENECKTemp`   VARCHAR(255),
       `fuTemp1`         VARCHAR(255),
       `fuTemp2`         VARCHAR(255),
       `createDate`      VARCHAR(255),
	   PRIMARY KEY (`fileName`)
);

/* 午班点检记录表 */
DROP TABLE IF EXISTS `ykk`.`DAILY_CHECK_NOON` ;
CREATE TABLE IF NOT EXISTS  `ykk`.`DAILY_CHECK_NOON`(
       `fileName`        VARCHAR(255) not null comment '文件名',
       `machineModel`    VARCHAR(255),
       `work`            VARCHAR(255),
       `first`           VARCHAR(255),
       `two`             VARCHAR(255),
       `three`           VARCHAR(255),
       `five`            VARCHAR(255),
       `six`             VARCHAR(255),
       `seven`           VARCHAR(255),
       `eight`           VARCHAR(255),
       `nine`            VARCHAR(255),
       `fourteen`        VARCHAR(255),
       `fifteen`         VARCHAR(255),
       `sixteen`         VARCHAR(255),
       `seventeen`       VARCHAR(255),
       `four`            VARCHAR(255),
       `ten`             VARCHAR(255),
       `eleven`          VARCHAR(255),
       `twelve`          VARCHAR(255),
       `createDate`      VARCHAR(255),
	   PRIMARY KEY (`fileName`) 
);

/* 压铸工程月度机械漏油点检记录表 */
DROP TABLE IF EXISTS `ykk`.`YZGC_MONTH_RECORD` ;
CREATE TABLE IF NOT EXISTS  `ykk`.`YZGC_MONTH_RECORD`(
       `fileName`        VARCHAR(255) not null comment '文件名',
       `MachineGroup`    VARCHAR(255) comment '机组',
       `MachineId`       VARCHAR(255) comment '机番',
       `Temp1`           VARCHAR(255) comment '机械可动侧LC部位漏油否',
       `Temp2`           VARCHAR(255) comment '作动油油量表（1/2上否）',
       `Temp3`           VARCHAR(255) comment '压动系统的PC装置漏油否',
       `Temp4`           VARCHAR(255) comment '机械油温（50℃以上否）',
       `Temp5`           VARCHAR(255) comment '中心顶轴的EC部位漏油否',
       `Temp6`           VARCHAR(255) comment '排序号',
       `Temp7`           VARCHAR(255) comment '齿轮传动的CP部位漏油否',
       `Temp8`           VARCHAR(255) comment '其他油、水配管情况',
       `reviewInfor`     VARCHAR(255) comment '备注',
	   PRIMARY KEY (`fileName`)
);

/* 压铸工程 DC研磨前半制品检查表 */
DROP TABLE IF EXISTS `ykk`.`SEMI_FINISHED_CHECK` ;
CREATE TABLE IF NOT EXISTS  `ykk`.`SEMI_FINISHED_CHECK`(
       `fileName`        VARCHAR(255) not null comment '文件名',
       `MachineGroup`    VARCHAR(255) comment '机组',
       `machineNo`       VARCHAR(255) comment '机番',
       `item`            VARCHAR(255) comment 'ITEM',
       `personInCharge`  VARCHAR(255) comment '担当者',
       `separateStatus`  VARCHAR(255) comment '分离状态',
       `gneck`           VARCHAR(255) comment 'G.NECK',
       `HS_Num`          VARCHAR(255) comment '回数',
       `remark`          VARCHAR(255) comment '备注',
       `surface`         VARCHAR(255) comment '外观',
       `damage_SB171`    VARCHAR(255) comment '型破损SB171/172',
       `PINDamage`       VARCHAR(255) comment 'PIN沟破损/PIN断',
       `damage_SB251`    VARCHAR(255) comment '型破损（加缔部/SB251）',
       `filling`         VARCHAR(255) comment '充型不良',
       `xingpian`        VARCHAR(255) comment '型偏',
       `b3_b4_b5_b7`     VARCHAR(255) comment '分离机异物混入',
       `b6`              VARCHAR(255) comment '排出管道异物混入',
       `c8_c9_c10`       VARCHAR(255) comment '升降机异物混入',
       `coreWash`        VARCHAR(255) comment 'CORE洗净',
	   PRIMARY KEY (`fileName`) 
);

/* 压轴工程型维修记录表 */
DROP TABLE IF EXISTS `ykk`.`MAINTENANCE_LOG` ;
CREATE TABLE IF NOT EXISTS  `ykk`.`MAINTENANCE_LOG`(
       `fileName`        VARCHAR(255) not null comment '文件名',
       `jiFan`           VARCHAR(255) comment '机番',
       `pinMing`         VARCHAR(255) comment '品名',
       `SHOT`            VARCHAR(255) comment '生产shot数',
       `element1`        VARCHAR(255) comment 'SB171',
       `element2`        VARCHAR(255) comment 'SB172',
       `element3`        VARCHAR(255) comment 'SB241',
       `element4`        VARCHAR(255) comment 'SB242',
       `element5`        VARCHAR(255) comment 'SB243',
       `element6`        VARCHAR(255) comment 'SB244',
       `element7`        VARCHAR(255) comment 'SB245',
       `element8`        VARCHAR(255) comment 'SB251',
       `element9`        VARCHAR(255) comment 'SB252',
       `element10`       VARCHAR(255) comment 'SB253',
       `element11`       VARCHAR(255) comment 'SB254',
       `element12`       VARCHAR(255) comment 'SB255',
       `maintainReason`  VARCHAR(255) comment '维修原因',
       `reviewInfor`     VARCHAR(255) comment '维修内容',
       `MaintenResult`   VARCHAR(255) comment '维修结果',
       `createDate`      VARCHAR(255) comment '创建时间',
	   PRIMARY KEY (`fileName`) 
);

/* 用户表 */
DROP TABLE IF EXISTS `ykk`.`USER` ;
CREATE TABLE IF NOT EXISTS  `ykk`.`USER`(
       `userName`        VARCHAR(255) not null comment '用户名',
       `Password`           VARCHAR(255) comment '密码',
       `level`         VARCHAR(255) comment '等级',
       `authority`            VARCHAR(255) comment '权限',
	   PRIMARY KEY (`userName`) 
);
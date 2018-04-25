-- MySQL Script generated by MySQL Workbench
-- 07/28/15 11:26:40
-- Model: New Model    Version: 1.04
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema cigfmsdb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `cigfmsdb` ;
CREATE SCHEMA IF NOT EXISTS `cigfmsdb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `cigfmsdb` ;

-- -----------------------------------------------------
-- Table `cigfmsdb`.`line_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`line_type` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`line_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `line_type` VARCHAR(45) NOT NULL,
  `icon` MEDIUMBLOB NULL,
  `description` VARCHAR(128) NULL,
  `worktime` BIGINT(8) NOT NULL DEFAULT 24 COMMENT '有效工作时长，单位小时',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`line_config`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`line_config` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`line_config` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `enable` TINYINT(1) NOT NULL DEFAULT 1 COMMENT '产线是否被启用',
  `line_name` VARCHAR(45) NOT NULL,
  `line_type_id` INT NOT NULL,
  `current_status` VARCHAR(2) NOT NULL DEFAULT 'o' COMMENT 'R-错�' /* comment truncated */ /*/红灯
Y-告警/黄灯
G-正常/恢复/绿灯
O-离线*/,
  `description` VARCHAR(64) NULL,
  `threshold` VARCHAR(2) NULL COMMENT '当状态变化时向其他系统�' /* comment truncated */ /*�post消息，或者发邮件，发短消息的门限值。
R-错误/红灯
Y-告警/黄灯
G-正常/恢复/绿灯
O-离线
*/,
  `timeout` BIGINT NULL COMMENT '超时多久，就判断该设备离线。',
  `worktime` BIGINT(8) NULL COMMENT '从line_type继承，可以基于每条产线修改',
  `contact_group_id` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `line_name_UNIQUE` (`line_name` ASC),
  INDEX `line_type_id_idx` (`line_type_id` ASC),
  CONSTRAINT `config_line_type_id`
    FOREIGN KEY (`line_type_id`)
    REFERENCES `cigfmsdb`.`line_type` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`device_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`device_type` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`device_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `device_type` VARCHAR(45) NOT NULL,
  `icon` MEDIUMBLOB NOT NULL,
  `description` VARCHAR(128) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`device_config`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`device_config` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`device_config` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `enable` TINYINT(1) NOT NULL DEFAULT 1 COMMENT '设备是否被启用',
  `equipment_id` VARCHAR(45) NOT NULL COMMENT '设备ID，唯一标示设备',
  `device_name` VARCHAR(45) NOT NULL,
  `device_type_id` INT NOT NULL,
  `current_status` VARCHAR(2) NOT NULL DEFAULT 'o' COMMENT 'R-错�' /* comment truncated */ /*/红灯
Y-告警/黄灯
G-正常/恢复/绿灯
O-离线*/,
  `threshold` VARCHAR(2) NULL COMMENT '当状态变化时向其他系统�' /* comment truncated */ /*�post消息，或者发邮件，发短消息的门限值。
R-错误/红灯
Y-告警/黄灯
G-正常/恢复/绿灯
O-离线
*/,
  `timeout` BIGINT NULL,
  `description` VARCHAR(64) NULL,
  `contact_group_id` INT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `config_device_type_id_idx` (`device_type_id` ASC),
  UNIQUE INDEX `equipment_id_UNIQUE` (`equipment_id` ASC),
  CONSTRAINT `config_device_type_id`
    FOREIGN KEY (`device_type_id`)
    REFERENCES `cigfmsdb`.`device_type` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`line2device`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`line2device` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`line2device` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `line_id` INT NOT NULL,
  `dev_id` INT NOT NULL,
  `location_id` INT NOT NULL DEFAULT 0 COMMENT '标明设备在产线中所处的位置',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `map_line_id_idx` (`line_id` ASC),
  INDEX `map_dev_id_idx` (`dev_id` ASC),
  CONSTRAINT `map_line_id`
    FOREIGN KEY (`line_id`)
    REFERENCES `cigfmsdb`.`line_config` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
  CONSTRAINT `map_dev_id`
    FOREIGN KEY (`dev_id`)
    REFERENCES `cigfmsdb`.`device_config` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`line_alarm`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`line_alarm` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`line_alarm` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `line_id` INT NOT NULL,
  `time_stamp` DATETIME NOT NULL,
  `severity` VARCHAR(2) NULL COMMENT '事件本' /* comment truncated */ /*��的严重等级
R-错误
Y-告警
G-正常*/,
  `status_after_event` VARCHAR(2) NULL COMMENT '事件发�' /* comment truncated */ /*�后设备的状态
R-错误
Y-告警
G-正常*/,
  `event_type` VARCHAR(64) NULL COMMENT '事件简短描述',
  `event_description` TEXT NULL COMMENT '事件的详细描述',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `alarm_line_id_idx` (`line_id` ASC),
  CONSTRAINT `alarm_line_id`
    FOREIGN KEY (`line_id`)
    REFERENCES `cigfmsdb`.`line_config` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`device_alarm`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`device_alarm` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`device_alarm` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `device_id` INT NOT NULL,
  `line_id` INT NOT NULL,
  `time_stamp` DATETIME NOT NULL,
  `severity` VARCHAR(2) NULL,
  `status_after_event` VARCHAR(2) NULL,
  `event_type` VARCHAR(64) NULL,
  `event_description` TEXT NULL,
  PRIMARY KEY (`id`),
  INDEX `alarm_dev_id_idx` (`device_id` ASC),
  CONSTRAINT `alarm_dev_id`
    FOREIGN KEY (`device_id`)
    REFERENCES `cigfmsdb`.`device_config` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`line_day_status`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`line_day_status` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`line_day_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `line_id` INT NOT NULL,
  `start_time` DATETIME NOT NULL,
  `status` VARCHAR(2) NOT NULL COMMENT '从start_time进' /* comment truncated */ /*��此状态
R-错误/红灯
Y-告警/黄灯
G-正常/恢复/绿灯
O-离线*/,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `status_line_id_idx` (`line_id` ASC),
  CONSTRAINT `status_line_id`
    FOREIGN KEY (`line_id`)
    REFERENCES `cigfmsdb`.`line_config` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`device_day_status`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`device_day_status` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`device_day_status` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `device_id` INT NOT NULL,
  `start_time` DATETIME NOT NULL,
  `status` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `status_dev_id_idx` (`device_id` ASC),
  CONSTRAINT `status_dev_id`
    FOREIGN KEY (`device_id`)
    REFERENCES `cigfmsdb`.`device_config` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`line_usage_ratio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`line_usage_ratio` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`line_usage_ratio` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `line_id` INT NOT NULL,
  `date` DATE NOT NULL,
  `usage_ratio` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `line_id_idx` (`line_id` ASC),
  CONSTRAINT `ratio_line_id`
    FOREIGN KEY (`line_id`)
    REFERENCES `cigfmsdb`.`line_config` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`device_usage_ratio`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`device_usage_ratio` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`device_usage_ratio` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `device_id` INT NOT NULL,
  `date` DATE NOT NULL,
  `usage_ratio` VARCHAR(45) NOT NULL COMMENT '设备利用率根据产线设置工作时长计算',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `ratio_idx` (`device_id` ASC),
  CONSTRAINT `ratio`
    FOREIGN KEY (`device_id`)
    REFERENCES `cigfmsdb`.`device_config` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`address_book`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`address_book` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`address_book` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` VARCHAR(45) NOT NULL,
  `name` VARCHAR(32) NULL,
  `department` VARCHAR(32) NULL,
  `title` VARCHAR(64) NULL,
  `mail` VARCHAR(128) NULL,
  `mobile` VARCHAR(16) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `employee_id_UNIQUE` (`employee_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`system_user_group`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`system_user_group` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`system_user_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_group_type` VARCHAR(45) NOT NULL COMMENT 'root/administrator/operater/monitor',
  `device_dashboard` TINYINT(1) NULL,
  `device_monitor` TINYINT(1) NULL,
  `device_config` TINYINT(1) NULL,
  `management_user` TINYINT(1) NULL,
  `management_system` TINYINT(1) NULL,
  `management_notification` TINYINT(1) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`system_uri_auth`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`system_uri_auth` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`system_uri_auth` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `uri` VARCHAR(128) NOT NULL,
  `administrator` TINYINT(1) NOT NULL,
  `operator` TINYINT(1) NOT NULL,
  `monitor` TINYINT(1) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`system_user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`system_user` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`system_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(64) NOT NULL,
  `user_password` VARCHAR(64) NULL,
  `user_group_id` INT NULL,
  `user_description` VARCHAR(128) NULL,
  `email` VARCHAR(128) NULL,
  `telephone` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `user_group_id_idx` (`user_group_id` ASC),
  CONSTRAINT `user_group_id`
    FOREIGN KEY (`user_group_id`)
    REFERENCES `cigfmsdb`.`system_user_group` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`address2contact_mapping`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`address2contact_mapping` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`address2contact_mapping` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `address_list_id` INT NOT NULL COMMENT 'address_list表索引',
  `contact_group_id` INT NOT NULL COMMENT 'contact_group表索引',
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cigfmsdb`.`contact_group`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cigfmsdb`.`contact_group` ;

CREATE TABLE IF NOT EXISTS `cigfmsdb`.`contact_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_name` VARCHAR(32) NOT NULL COMMENT '用来在产线和设备中引用，可以是产线和缩略信息。如SMT1_LIST，也可以是设备缩略信息：SPI1_LIST',
  `description` VARCHAR(128) NULL COMMENT '联系人分组功能的描述信息：比如对于STM1_LIST,描述信息可以为：这是SMT产线1的联系人列表',
  `first_contact_id` INT NULL COMMENT '指向address_list，表示这个分组的第一联系人',
  `first_contact_sms` TINYINT(1) NULL DEFAULT 1,
  `first_contact_voice` TINYINT(1) NULL DEFAULT 1,
  `fisrt_contact_mail` TINYINT(1) NULL DEFAULT 1,
  `normal_contact_sms` TINYINT(1) NULL DEFAULT 0,
  `normal_contact_voice` TINYINT(1) NULL DEFAULT 0,
  `normal_contact_mail` TINYINT(1) NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `notification_name_UNIQUE` (`group_name` ASC))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
USE `cigfmsdb`;

DELIMITER $$

USE `cigfmsdb`$$
DROP TRIGGER IF EXISTS `cigfmsdb`.`line_config_AINS` $$
USE `cigfmsdb`$$
CREATE TRIGGER `line_config_AINS` AFTER INSERT ON `line_config` FOR EACH ROW
begin
insert into line_day_status(line_id, start_time, status) values(new.id, current_time, new.current_status);
end$$


USE `cigfmsdb`$$
DROP TRIGGER IF EXISTS `cigfmsdb`.`line_config_AUPD` $$
USE `cigfmsdb`$$
CREATE TRIGGER `line_config_AUPD` AFTER UPDATE ON `line_config` FOR EACH ROW
begin
if old.current_status != new.current_status then
insert into line_day_status(line_id, start_time, status) values(new.id, current_time, new.current_status);
end if;
end$$


USE `cigfmsdb`$$
DROP TRIGGER IF EXISTS `cigfmsdb`.`device_config_AINS` $$
USE `cigfmsdb`$$
CREATE TRIGGER `device_config_AINS` AFTER INSERT ON `device_config` FOR EACH ROW
begin
insert into device_day_status(device_id, start_time, status) values(new.id, current_time, new.current_status);
end$$


USE `cigfmsdb`$$
DROP TRIGGER IF EXISTS `cigfmsdb`.`device_config_AUPD` $$
USE `cigfmsdb`$$
CREATE TRIGGER `device_config_AUPD` AFTER UPDATE ON `device_config` FOR EACH ROW
begin
if old.current_status != new.current_status then
insert into device_day_status(device_id, start_time, status) values(new.id, current_time, new.current_status);
end if;
end$$


DELIMITER ;

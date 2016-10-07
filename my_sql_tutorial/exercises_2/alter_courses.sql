
ALTER TABLE `bootcamp`.`courses` 
CHANGE COLUMN `courses id` `CID` INT(11) NOT NULL ,
CHANGE COLUMN `name` `Name` VARCHAR(45) NULL DEFAULT NULL ,
CHANGE COLUMN `name of the lecturer` `Lecturer` VARCHAR(45) NULL DEFAULT NULL ,
CHANGE COLUMN `name of the assisstant` `Assistant` VARCHAR(45) NULL DEFAULT NULL ,
CHANGE COLUMN `duration of the course` `Duration` INT(11) NULL DEFAULT NULL ,
CHANGE COLUMN `starting date` `StartDate` DATE NULL DEFAULT NULL ;
CREATE TABLE `bootcamp`.`students_has_courses` (
  `students_StID` INT(11) NOT NULL,
  `courses_CID` INT(11) NOT NULL,
  `grade` INT(2) NULL,
  PRIMARY KEY (`students_StID`, `courses_CID`),
  INDEX `CID_idx` (`courses_CID` ASC),
  CONSTRAINT `StID`
    FOREIGN KEY (`students_StID`)
    REFERENCES `bootcamp`.`students` (`StID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `CID`
    FOREIGN KEY (`courses_CID`)
    REFERENCES `bootcamp`.`courses` (`CID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

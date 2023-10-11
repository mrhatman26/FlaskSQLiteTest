DROP TABLE IF EXISTS table_staff;
CREATE TABLE table_staff(
	staff_id INT NOT NULL,
	staff_forename TEXT,
	staff_surname TEXT,
	staff_age INT,
	staff_role TEXT,
	staff_available BOOLEAN NOT NULL
);
DROP TABLE IF EXISTS table_recruitees;
CREATE TABLE table_recruitees(
	recruitee_id INT NOT NULL,
	recruitee_forename TEXT,
	recruitee_surname TEXT,
	recruitee_age INT,
	recruitee_applied_role TEXT,
	recruitee_application_successful BOOLEAN NOT NULL
);
DROP TABLE IF EXISTS link_staff_recruitee;
CREATE TABLE link_staff_recruitee(
	staff_id INT NOT NULL,
	recruitee_id INT NOT NULL,
	FOREIGN KEY(staff_id) REFERENCES table_staff(staff_id),
	FOREIGN KEY(recruitee_id) REFERENCES table_recruitees(recruitee_id)
);
INSERT INTO table_staff VALUES(0, "James", "Smith", 32, "Recruiter", true);
INSERT INTO table_recruitees VALUES(0, "Robert", "Haulington", 28, "S1A-02 Store Manager", true);
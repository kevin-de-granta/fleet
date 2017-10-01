/*
File name:      Fleet_Core_Table_Init.sql
Function:       To create tables for database FleetCore
Created by:     W. Wang(Kevin), ww288@cantab.net
Created on:     2017/10/01
Revised hist:   revised by ____ on ____/__/__(Ver1.XX.XX)(changes:__)
Revised hist:   revised by ____ on ____/__/__(Ver1.XX.XX)(changes:__)
*/

/*
DB Engine:      InnoDB (not MyISAM)
Encode:         UTF8
*/

/*
Notes:
- Identifier: most identifier should be UUID instead of numbered ID, especially those for web service.
- Index: all UUIDs/IDs would be indexed.
- Table names: "flt_", abbreviation of string "fleet", would be used as prefix of most FleetCore tables; similarly, "wf_" means web fleet.
*/


-- use core database of Fleet
USE FleetCore;

/*
System Variables
*/
CREATE TABLE flt_sys_vars (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    section VARCHAR(400) NOT NULL,
    name VARCHAR(400) NOT NULL, -- equivalent to "option" in .ini files
    value VARCHAR(800),
    create_time DATETIME NOT NULL,
    descp TEXT,
    PRIMARY KEY (id)
) ENGINE=INNODB DEFAULT CHARSET=utf8;
INSERT INTO flt_sys_vars (create_time, name, section, value) VALUES (now(), 'charset', 'database', 'utf8'); -- a test line
SELECT * FROM flt_sys_vars;
-- DROP TABLE flt_sys_vars;

/*
Users of Web Fleet
For simplicity, current database does not hold personal details or apply authorization based on groups/roles.
*/
CREATE TABLE wf_users (
    uuid CHAR(32) NOT NULL,
    name VARCHAR(40) NOT NULL, -- unique
    passwd VARCHAR(50) NOT NULL, -- at least 32bit in md5
    email VARCHAR(60) NOT NULL, -- unique
    state VARCHAR(40) NOT NULL, -- status: invited, registered, verified, normal, frozen, deleted, misc
    descp TEXT,
    create_time DATETIME NOT NULL,
    PRIMARY KEY (uuid)
)ENGINE=INNODB DEFAULT CHARSET=utf8;
INSERT INTO wf_users (uuid, name, passwd, email, state, create_time) VALUES (replace(UUID(),'-',''), 'ww288', 'e68604f7fed54f64a63e6eecd2519747', 'ww288@cantab.net', 'normal', now());
SELECT * FROM wf_users;
-- DROP TABLE wf_users;















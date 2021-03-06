-- with debug if and if not
drop database if exists crewmen;
create database crewmen character set utf8 collate utf8_general_ci;
use crewmen;

drop table if exists users;

drop table if exists schedule_maker;
drop table if exists paid_by;
drop table if exists schedule;
drop table if exists fee_log;

drop table if exists record_in_plan;
drop table if exists requirement_in_plan;
drop table if exists status_in_record;

drop table if exists attr_in_item; -- referenced by requirement and status

drop table if exists training_record; -- by status by record_in_plan
drop table if exists training_plan; -- by requirment by record_in_plan
drop table if exists item_attribute; -- referenced by attr_in_item
drop table if exists training_item; -- referenced by attr_in_item
drop table if exists member; -- referenced by item plan record paid_by schedule_maker users
drop table if exists ship;
drop table if exists ship_type_table;


create table if not exists member
       (name varchar(20) not null,
       -- big chunk for information
       sex enum('男', '女') default '男',
       enter_club date, -- the crew
       enter_school date, -- school
       birth date,
       height smallint unsigned,
       weight smallint unsigned,
       ID int unsigned,
       -- big chunk for information
       job enum('couch', 'crew leader', 'crew member') default 'crew member',
       training_level enum('newbie', 'medium', 'old bird') default 'newbie',
       primary key(ID)
       );-- character set utf8 collate utf8_general_ci;

create table if not exists users
       (username varchar(20) not null,
       password binary(128) not null, -- half byte each, so 128 * 0.5 * 8 is 512 using sha2('pass', 512)
       -- priority tinyint unsigned not null defalut 2, -- the lower the better
       ID int unsigned, -- don't have to be unique, since it's PK for member
       email varchar(50) not null unique,
       primary key(username),
       foreign key(ID) references member(ID) on delete cascade
       );

-- how to enforce constraint on full participation, every schedule should have at least a maker...
create table if not exists schedule
       (add_time datetime default current_timestamp,
       happen_at datetime, -- time could be unsure of
       event_ID int unsigned auto_increment,
       event varchar(100) not null,
       spec varchar(1000),
       length time,
       primary key(event_ID)
       );

create table if not exists schedule_maker
       (event_ID int unsigned,
       ID int unsigned,
       primary key(event_ID, ID),
       foreign key(event_ID) references schedule(event_ID),
       foreign key(ID) references member(ID) on delete cascade
       );


-- same question as schedule, every fee should have a payer
create table if not exists fee_log
       (cost decimal(13,2), -- cost could range from cent to 10^13 which is 10^4 billion yuan, should be enough
        used_at datetime,
        cause varchar(200),
        fee_ID int unsigned,
        primary key(fee_ID)
       );

create table if not exists paid_by
       (ID int unsigned,
       fee_ID int unsigned,
       primary key(ID, fee_ID),
       foreign key(ID) references member(ID) on delete cascade,
       foreign key(fee_ID) references fee_log(fee_ID)
       );

-- plan and record session!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- plan and record session!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- plan and record session!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- plan and record session!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

-- It's divided into three main parts:
-- The plan and record are symmetrical
-- ignore! no longer supported (although plan can have multiple makes?? weird functionality though)


-- The main similarity lies in the relation of (record, item, attribute, status/requirement)
-- when it indicates that a record can have multiple items
-- when an item can have multiple attributes
-- Therefore this relation can be able to indicate a collection of status of a collection of training items in a plan or record

-- notice how attr_in_item is referenced by (requirement_in_plan and status_in_record)
-- may need to define training item
create table if not exists training_item
       (item_name varchar(100),
       item_ID int unsigned auto_increment,
       is_strength enum('y', 'n'), -- strength or aerobic
       is_test enum('y', 'n'),     -- test or regular
       primary key(item_ID)
       );

create table if not exists training_record
       (record_ID int unsigned auto_increment,
       train_at datetime,
       training_last time,
       ID int unsigned,
       primary key(record_ID),
       foreign key(ID) references member(ID)
       );

create table if not exists training_plan
       (
       plan_ID int unsigned auto_increment,
       train_at datetime,
       training_last time,
       ID int unsigned,
       training_level enum('newbie', 'medium', 'old bird', 'all') default 'all',
       primary key(plan_ID),
       foreign key(ID) references member(ID)
       );

create table if not exists item_attribute
       (attr_ID int unsigned,
       attr_name varchar(100) unique,
       primary key(attr_ID)
       );

create table if not exists attr_in_item
       (attr_ID int unsigned,
       item_ID int unsigned,
       primary key(attr_ID, item_ID),
       foreign key(attr_ID) references item_attribute(attr_ID),
       foreign key(item_ID) references training_item(item_ID)
       );

create table if not exists requirement_in_plan
       (
       plan_ID int unsigned,
       item_ID int unsigned,
       attr_ID int unsigned,
       comp enum('larger', 'smaller', 'no requirement') not null default 'no requirement',
       requirement int unsigned,
       primary key(plan_ID, item_ID, attr_ID),
       foreign key(item_ID, attr_ID) references attr_in_item(item_ID, attr_ID),
       foreign key(plan_ID) references training_plan(plan_ID)
       );

create table if not exists status_in_record
       (record_ID int unsigned,
       item_ID int unsigned,
       attr_ID int unsigned,
       status int unsigned,
       primary key(record_ID, item_ID, attr_ID),
       foreign key (item_ID, attr_ID) references attr_in_item(item_ID, attr_ID),
       foreign key (record_ID) references training_record(record_ID)
       );

-- below is record and plan relation
create table if not exists record_in_plan
       (plan_ID int unsigned,
       record_ID int unsigned,
       primary key(plan_ID, record_ID),
       foreign key(plan_ID) references training_plan(plan_ID),
       foreign key(record_ID) references training_record(record_ID)
       );

-- Obsoleted
-- create table if not exists plan_maker
--        (ID int unsigned,
--        plan_ID int unsigned,
--        primary key(ID, plan_ID),
--        foreign key(ID) references member(ID) on delete cascade,
--        foreign key(plan_ID) references training_plan(plan_ID)
--        );

-- plan and record session!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- plan and record session!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- plan and record session!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
-- plan and record session!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

create table if not exists ship_type_table
       (ship_type_ID tinyint unsigned,
       ship_type_name varchar(100),
       primary key(ship_type_ID)
       );

create table if not exists ship
       (ship_name varchar(100),
       ship_type_ID tinyint unsigned,
       condition_description varchar(1000),
       primary key(ship_name),
       foreign key(ship_type_ID) references ship_type_table(ship_type_ID)
       );







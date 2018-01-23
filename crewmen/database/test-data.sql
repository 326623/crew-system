-- executed with crew-leader
use crewmen;
insert into member(name, ID, training_level) values
('于H', '0', 'old bird'),
('郭D胜', '1', 'old bird'),
('X德昊', '2', 'old bird'),
('S炜焜', '3', 'old bird'),
('happygirlzt', '520', 'old bird'),
('normal','1997','newbie');

insert into member(name, ID, training_level, job) values
('胡泽Q', '4', 'old bird', 'crew leader'),
('admin', '1996', 'old bird', 'couch');

insert into users(username, password, ID, email) values
('yuH', sha2('hello-world', 512), '0', '123@happygirlzt.com'),
('guoD', sha2('hello-world', 512), '1', '124@happygirlzt.com'),
('Xde', sha2('hello-world', 512), '2', '125@happygirlzt.com'),
('Swei', sha2('hello-world', 512), '3', '126@happygirlzt.com'),
('Huze', sha2('hello-world', 512), '4', '128@happygirlzt.com');

-- for test --
insert into users(username, password, ID, email) values
('admin', sha2('admin', 512), '1996', '122@happygirlzt.com'),
('normal', sha2('normal', 512), '1997', '11@happygirlzt.com');


insert into training_item(item_ID, item_name, is_strength, is_test) values
(1, '卧拉', 'y', 'n'),
(2, '平板支撑','y', 'n'),
(3, '仰卧两头起', 'y', 'n'),
(4, '深蹲', 'y', 'n'),
(5, '卧推', 'y', 'n'),
(6, '跑步', 'n', 'n'),
(7, '测功仪', 'n', 'n'),
(8, '游泳', 'n', 'n');

insert into item_attribute(attr_ID, attr_name) values
('1', '重量'),
('2', '距离'),
('3', '时间'),
('4', '次数'),
('5', '组数'),
('6', '桨频'),
('7', '风阻');

insert into attr_in_item(item_ID, attr_ID) values
(1, 1), (1, 3), (1, 4), (1, 5),
(2, 3), (2, 5),
(3, 4), (3, 5),
(4, 1), (4, 3), (4, 4), (4, 5),
(5, 1), (5, 3), (5, 4), (5, 5),
(6, 2), (6, 3), (6, 5),
(7, 2), (7, 3), (7, 5), (7, 6), (7, 7),
(8, 2), (8, 3), (8, 5);

insert into training_plan(plan_ID, train_at, training_last, ID) values
(1, '2017-12-29 12:00:00', 30, '1996'),
(2, '2017-12-30 00:00:00', 30, '1996'),
(3, '2018-1-1 12:00:00', 30, '1996'),
(4, '2018-1-2 12:00:00', 30, '1996'),
(5, '2018-1-3 12:00:00', 30, '1996'),
(6, '2018-1-4 12:00:00', 30, '1996');

insert into requirement_in_plan(plan_ID, item_ID, attr_ID, comp, requirement) values
(1, 1, 1, 'larger', 30), (1, 1, 4, 'larger', 30), (1, 1, 5, 'larger', 5),
(1, 2, 3, 'larger', 120), (1, 2, 5, 'larger', 2),
(1, 3, 4, 'larger', 30), (1, 3, 5, 'larger', 2),

(2, 1, 1, 'larger', 30), (2, 1, 4, 'larger', 30), (2, 1, 5, 'larger', 5),
(2, 2, 3, 'larger', 120), (2, 2, 5, 'larger', 2),
(2, 3, 4, 'larger', 30), (2, 3, 5, 'larger', 2),

(3, 1, 1, 'larger', 30), (3, 1, 4, 'larger', 30), (3, 1, 5, 'larger', 5),
(3, 2, 3, 'larger', 120), (3, 2, 5, 'larger', 2),
(3, 3, 4, 'larger', 30), (3, 3, 5, 'larger', 2),

(4, 1, 1, 'larger', 30), (4, 1, 4, 'larger', 30), (4, 1, 5, 'larger', 5),
(4, 2, 3, 'larger', 120), (4, 2, 5, 'larger', 2),
(4, 3, 4, 'larger', 30), (4, 3, 5, 'larger', 2),

(5, 1, 1, 'larger', 30), (5, 1, 4, 'larger', 30), (5, 1, 5, 'larger', 5),
(5, 2, 3, 'larger', 120), (5, 2, 5, 'larger', 2),
(5, 3, 4, 'larger', 30), (5, 3, 5, 'larger', 2),

(6, 1, 1, 'larger', 30), (6, 1, 4, 'larger', 30), (6, 1, 5, 'larger', 5),
(6, 2, 3, 'larger', 120), (6, 2, 5, 'larger', 2),
(6, 3, 4, 'larger', 30), (6, 3, 5, 'larger', 2);


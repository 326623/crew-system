-- executed with crew-leader
insert into member(name, ID, training_level) values
('于H', '0', 'old bird'),
('郭D胜', '1', 'old bird'),
('X德昊', '2', 'old bird'),
('S炜焜', '3', 'old bird'),
('happygirlzt', '520', 'old bird'),
('admin', '1996', 'newbie'),
('normal','1997','newbie');

insert into member(name, ID, training_level, job) values ('胡泽Q', '4', 'old bird', 'crew leader');

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
(4, '深蹲', 'y', 'n');

insert into item_attribute(attr_ID, attr_name, comp) values
('1', '重量', 'larger'),
('2', '距离', 'larger'),
('3', '时间', 'smaller'),
('4', '次数', 'larger'),
('5', '组数', 'larger'),
('6', '桨频', 'larger'),
('7', '桨频', 'smaller');

insert into training_plan(train_at, training_last) values
('2017-12-29 12:00:00', 30),
('2017-12-30 00:00:00', 30);

insert into item_in_plan(plan_ID, item_ID) values
('1', '1'),
('1', '2'),
('1', '3'),
('2', '1');

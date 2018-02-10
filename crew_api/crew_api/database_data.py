from crew_api.models import *
from crew_api import bcrypt

"""
SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO'
would prevent MySQL wrongly insert 0 into integer
"""

"""
Because member values have some inconsistency in data, not using sqlalchemy core but orm
"""

###################
### old fashion ###
###################

insert_member=[
    Member(name='于H', ID='1', training_level='old bird'),
    Member(name='郭D胜', ID='2', training_level='old bird'),
    Member(name='X德昊', ID='3', training_level='old bird'),
    Member(name='S炜焜', ID='4', training_level='old bird'),
    Member(name='happygirlzt', ID='520', training_level='old bird'),
    Member(name='normal', ID='1997', training_level='newbie'),
    Member(name='胡泽Q', ID='5', training_level='old bird', job='crew leader'),
    Member(name='admin', ID='1996', training_level='old bird', job='couch')
]

hashing= lambda x : bcrypt.generate_password_hash(x)

# this is the slow part
insert_users=[
    User(username='yuH', password=hashing('hello-world'), ID='1', email='123@happygirlzt.com'),
    User(username='guoD', password=hashing('hello-world'), ID='2', email='124@happygirlzt.com'),
    User(username='Xde', password=hashing('hello-world'), ID='3', email='125@happygirlzt.com'),
    User(username='Swei', password=hashing('hello-world'), ID='4', email='126@happygirlzt.com'),
    User(username='Huze', password=hashing('hello-world'), ID='5', email='128@happygirlzt.com'),
    User(username='admin', password=hashing('admin'), ID='1996', email='122@happygirlzt.com'),
    User(username='normal', password=hashing('normal'), ID='1997', email='11@happygirlzt.com')
]

insert_training_items=[
    TrainingItem(item_ID=1, item_name='卧拉', is_strength='y', is_test='n'),
    TrainingItem(item_ID=2, item_name='平板支撑', is_strength='y', is_test='n'),
    TrainingItem(item_ID=3, item_name='仰卧两头起', is_strength='y', is_test='n'),
    TrainingItem(item_ID=4, item_name='深蹲', is_strength='y', is_test='n'),
    TrainingItem(item_ID=5, item_name='卧推', is_strength='y', is_test='n'),
    TrainingItem(item_ID=6, item_name='跑步', is_strength='n', is_test='n'),
    TrainingItem(item_ID=7, item_name='测功仪', is_strength='n', is_test='n'),
    TrainingItem(item_ID=8, item_name='游泳', is_strength='n', is_test='n')
]

###################
### new fashion ###
###################

x=[
    ('1', '重量'),
    ('2', '距离'),
    ('3', '时间'),
    ('4', '次数'),
    ('5', '组数'),
    ('6', '桨频'),
    ('7', '风阻')
]

insert_item_attr=[{'attr_ID': x1, 'attr_name': x2} for x1, x2 in x]

x = [
    (1, 1), (1, 3), (1, 4), (1, 5),
    (2, 3), (2, 5),
    (3, 4), (3, 5),
    (4, 1), (4, 3), (4, 4), (4, 5),
    (5, 1), (5, 3), (5, 4), (5, 5),
    (6, 2), (6, 3), (6, 5),
    (7, 2), (7, 3), (7, 5), (7, 6), (7, 7),
    (8, 2), (8, 3), (8, 5)
]

insert_attr_in_item = [{'item_ID': i, 'attr_ID': j} for (i,j) in x]

x = [
    (1, '2017-12-29 12:00:00', 30, '1996'),
    (2, '2017-12-30 00:00:00', 30, '1996'),
    (3, '2018-1-1 12:00:00', 30, '1996'),
    (4, '2018-1-2 12:00:00', 30, '1996'),
    (5, '2018-1-3 12:00:00', 30, '1996'),
    (6, '2018-1-4 12:00:00', 30, '1996')
]

insert_training_plan = [
    {'plan_ID': x, 'train_at': y, 'training_last': z, 'ID': q}\
     for x, y, z, q in x
]

x = [
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
    (6, 3, 4, 'larger', 30), (6, 3, 5, 'larger', 2)
]

insert_requirement_in_plan = [
    {'plan_ID': x1, 'item_ID': x2, 'attr_ID': x3, 'comp': x4, 'requirement': x5}\
     for x1, x2, x3, x4, x5 in x
]

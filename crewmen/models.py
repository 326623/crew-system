from crewmen import db
from sqlalchemy.orm import relationship
from sqlalchemy import Table, MetaData, func


meta = MetaData(bind=db.engine)

##############################################
##### Take note of the naming convention ##### no underscore for models' name
##############################################

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'autoload':True,
                      'autoload_with': db.engine}

    member = relationship("Member", backref="user")

class Member(db.Model):
    __tablename__ = 'member'
    __table_args__ = {'autoload':True,
                      'autoload_with': db.engine}

class ItemAttribute(db.Model):
    __tablename__ = 'item_attribute'
    __table_args__ = {'autoload':True,
                      'autoload_with': db.engine}

class AttrInItem(db.Model):
    __tablename__ = 'attr_in_item'
    __table_args__ = {'autoload':True,
                      'autoload_with': db.engine}


class TrainingPlan(db.Model):
    __tablename__ = 'training_plan'
    __table_args__ = {'autoload':True,
                      'autoload_with': db.engine}

    # cannot pass in the class
    requirement = relationship("RequirementInPlan",
                               backref='training_plan')

    maker = relationship("Member", backref='training_plan')

class TrainingItem(db.Model):
    __tablename__ = 'training_item'
    __table_args__ = {'autoload':True,
                      'autoload_with': db.engine}

    attr = relationship("ItemAttribute",
                        secondary=AttrInItem.__table__)

class RequirementInPlan(db.Model):
    __tablename__ = 'requirement_in_plan'
    __table_args__ = {'autoload':True,
                      'autoload_with': db.engine}

    item = relationship("TrainingItem",
                        secondary=AttrInItem.__table__)

    attr = relationship("ItemAttribute",
                        secondary=AttrInItem.__table__)

class PaidBy(db.Model):
    __tablename__ = 'paid_by'
    __table_args__ = {'autoload':True,
                      'autoload_with': db.engine}

class FeeLog(db.Model):
    __tablename__ = 'fee_log'
    __table_args__ = {'autoload':True,
                      'autoload_with': db.engine}

    payer = relationship("Member",
                         secondary=PaidBy.__table__)

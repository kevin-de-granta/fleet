# -*- coding:utf-8 -*-

#
# File Name:    map.py
# Function:     To map between sql tables and python classes.
# Created by:   Wenkai Wang (Kevin), ww288@cantab.net
# Created on:   2017/10/01
# Revised hist: revised by _____ on ____/__/__
#

#
# Please be noted that this file is only to map Fleet Core DB. For financial database info, please refer to: fleet.finance.db.map. 
#


from __future__ import unicode_literals
import uuid
from datetime import datetime

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

def GetUUID():
    uuidAsString = uuid.uuid1()
    sstr = uuidAsString.__str__().split('-') # splitted string which is actually a list.
    return '%s%s%s%s%s' % (sstr[4], sstr[2], sstr[1], sstr[0], sstr[3])


class FltSysVars(Base):
    __tablename__ = 'flt_sys_vars'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    section = Column('section', String(400))
    name = Column('name', String(400))
    value = Column('value', String(800))
    createTime = Column('create_time', DateTime, default=datetime.now)
    descp = Column('descp', Text)


# users of web fleet
class WfUsers(Base):
    __tablename__ = 'wf_users'

    uuid = Column('uuid', String(32), primary_key=True, default=GetUUID)
    name = Column('name', String(40)) # TODO: make it unique
    passwd = Column('passwd', String(50))
    email = Column('email', String(60))
    state = Column('state', String(40))
    descp = Column('descp', Text)
    createTime = Column('create_time', DateTime, default=datetime.now)
















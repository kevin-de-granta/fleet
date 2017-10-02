# -*- coding:utf-8 -*-

#
# File Name:    adapter.py
# Function:     To provide an adapter for DB connection. It is for SQL connection only.
# Descp:        This file has been named adapter.py instead of mysql_adapter.py, beacuse for Fleet Core, the database is organized as a relational database (RDB).
# Created by:   Wenkai Wang (Kevin), ww288@cantab.net
# Created on:   2017/10/01
# Revised hist: revised by _____ on ____/__/__
#



import threading

from sqlalchemy import *
from sqlalchemy.pool import NullPool
from sqlalchemy.orm import sessionmaker

# TODO: change FleetEnv into singleton.
from fleet.core.env_fleet import FleetCoreEnv

class DbAdapter:
    pass




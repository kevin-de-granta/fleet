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
from sqlalchemy.ext.declarative import declarative_base

from fleet.core.env_fleet import FleetCoreEnv

Base = declarative_base()

class DbAdapter:
    instance = None
    mutex = threading.Lock()

    def __init__(self):
        self.__init_engines__();
        self._readSess = None
        self._writeSess = None

    def __del__(self):
        if self._readSess is not None:
            self._readSess.close()
        if self._writeSess is not None:
            self._writeSess.close()

    def __init_engines__(self):
        env = FleetCoreEnv.GetInstance()
        master = env.get(section='database', option='master-host')
        slave = env.get(section='database',option='slave-host')
        port = env.get('database', 'port')
        database = env.get('database', 'dbname')
        user = env.get('database', 'username')
        passwd = env.get('database', 'passwd')
        charset = env.get('database', 'charset')
        bDebug = (env.get('default', 'debug')=='true')
        # engine for writing
        engInfo = 'mysql://' + user + ':' + passwd + '@' + master + ':' + port + '/' + database + '?charset=' + charset
        if bDebug:
            self._writeEng = create_engine(engInfo, echo=True, poolclass=NullPool)
        else:
            self._writeEng = create_engine(engInfo, echo=False, poolclass=NullPool) 
        # engine for reading
        engInfo = 'mysql://' + user + ':' + passwd + '@' + slave + ':' + port + '/' + database + '?charset=' + charset
        if bDebug:
            self._readEng = create_engine(engInfo, echo=True, poolclass=NullPool)
        else:
            self._readEng = create_engine(engInfo, echo=False, poolclass=NullPool)
        return True

    def reinitEngines(self):
        return self.__init_engines__()

    def getReadEngine(self):
        return self._readEng

    def getWriteEngine(self):
        return self._writeEng

    def createTables(self):
        writeEng = getWriteEngine()
        Base = declarative_base()
        Base.metadata.create_all(writeEng)

    # please do NOT close this session after using it
    def getReadSession(self):
        if self._readSess is None:
            ReadSession = sessionmaker(bind=self.getReadEngine())
            self._readSess = ReadSession()
        return self._readSess

    # please do NOT close this session after using it
    def getWriteSession(self):
        if self._writeSess is None:
            WriteSession = sessionmaker(bind=self.getWriteEngine())
            self._writeSess = WriteSession()
        return self._writeSess

    @staticmethod
    def GetInstance():
        if(DbAdapter.instance==None):
            DbAdapter.mutex.acquire()
            if(DbAdapter.instance==None):
                DbAdapter.instance = DbAdapter()
            DbAdapter.mutex.release()
        return DbAdapter.instance



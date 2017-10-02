# -*- coding:utf-8 -*-

#
# File Name:    env_fleet.py
# Function:     Singleton for Env of Fleet Core.
# Created by:   Wenkai Wang (Kevin), ww288@cantab.net
# Created on:   2017/09/30
# Revised hist: revised by _____ on ____/__/__
#


import os
import threading # TODO: chagne FleetEnv into singleton

from  fleet.core.env import Env


class FleetCoreEnv(Env):
    # static variables for singleton
    instance = None
    mutex = threading.Lock()
    # stataic variables for config
    HOME_KEY = 'FLEET_HOME'
    CONF_FILE = 'conf/fleet.ini'

    def __init__(self):
        super(FleetCoreEnv, self).__init__(homeKey=FleetCoreEnv.HOME_KEY)
        self.load_config_files();
        self.load_config_table();

    def load_config_files(self):
        # global config
        self.load(file=FleetCoreEnv.CONF_FILE, relative=True)
        # user-specified config
        userConfFile = self.getConfItem(section='misc', option='user_conf')
        userHome = os.environ.get('HOME')
        userConfFile = userHome + '/' + userConfFile
        #print 'Path of user conf file: ' + userConfFile # test
        self.load(file=userConfFile, relative=False)
        # optional: file-system config
        #sizeMarkerFile = self.getConfItem(section='files', option='size_marker')
        #self.load(file=sizeMarkerFile, relative=True)

    def load_config_table(self):
        # TODO: config from db
        pass

    @staticmethod
    def GetInstance():
        if(FleetCoreEnv.instance==None):
            FleetCoreEnv.mutex.acquire()
            if(FleetCoreEnv.instance==None):
                FleetCoreEnv.instance = FleetCoreEnv()
            FleetCoreEnv.mutex.release()
        return FleetCoreEnv.instance






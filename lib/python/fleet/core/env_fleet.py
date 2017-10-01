# -*- coding:utf-8 -*-

#
# File Name:    env_fleet.py
# Function:     To xxxxx.
# Created by:   Wenkai Wang (Kevin), ww288@cantab.net
# Created on:   2017/09/30
# Revised hist: revised by _____ on ____/__/__
#


import os
from  fleet.core.env import Env


# conf/fleet.ini
class FleetEnv(Env):
    HOME_KEY = 'FLEET_HOME'
    CONF_FILE = 'conf/fleet.ini'

    def __init__(self):
        super(FleetEnv, self).__init__(homeKey=FleetEnv.HOME_KEY)
        # global config
        self.load(file=FleetEnv.CONF_FILE, relative=True)
        # user-specified config
        userConfFile = self.getConfItem(section='misc', option='user_conf')
        userHome = os.environ.get('HOME')
        userConfFile = userHome + '/' + userConfFile
        #print 'Path of user conf file: ' + userConfFile # test
        self.load(file=userConfFile, relative=False)
        # optional: file-system config
        #sizeMarkerFile = self.getConfItem(section='files', option='size_marker')
        #self.load(file=sizeMarkerFile, relative=True)
        # TODO: config from db




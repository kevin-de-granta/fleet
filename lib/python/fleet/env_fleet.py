# -*- coding:utf-8 -*-

#
# File Name:    xxxx.py
# Function:     To xxxxx.
# Created by:   Wenkai Wang (Kevin), ww288@cantab.net
# Created on:   20xx/xx/xx
# Revised hist: revised by _____ on ____/__/__
#


import os
from  zminer.env import Env


# conf/zhi_miner.ini
class ZMinerEnv(Env):
    HOME_KEY = 'ZHIMINER_HOME'
    CONF_FILE = 'conf/zhi_miner.ini'

    def __init__(self):
        super(ZMinerEnv, self).__init__(homeKey=ZMinerEnv.HOME_KEY)
        self.load(file=ZMinerEnv.CONF_FILE, relative=True)
        userConfFile = self.getConfItem(section='misc', option='user_conf')
        userHome = os.environ.get('HOME')
        userConfFile = userHome + '/' + userConfFile
        #print 'Path of user conf file: ' + userConfFile
        self.load(file=userConfFile, relative=False)
        sizeMarkerFile = self.getConfItem(section='files', option='size_marker')
        self.load(file=sizeMarkerFile, relative=True)





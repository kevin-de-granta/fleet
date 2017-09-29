# -*- coding:utf-8 -*-

#
# File Name:    env.py
# Function:     To build env from conf for further use.
# Created by:   Wenkai Wang (Kevin), ww288@cantab.net
# Created on:   2017/08/12
# Revised hist: revised by _____ on ____/__/__
#


import os
import sys
import threading
import ConfigParser
import __future__

from .exception import ArgumentError, ArgError


reload(sys)
sys.setdefaultencoding("utf-8")


class Env(object):
    instance = None
    mutex = threading.Lock()

    def __init__(self, homeKey=None, appHome=None):
        self.appHome = None
        if (homeKey is not None) or (appHome is not None):
            self.setAppHome(homeKey=homeKey, appHome=appHome)
        self.conf = {}

    def getAppHome(self):
        return self.appHome

    def setAppHome(self, homeKey=None, appHome=None):
        if appHome is not None:
            self.appHome = appHome
        elif homeKey is not None:
            appHome = os.environ.get(homeKey)
            self.appHome = appHome
        else:
            raise ArgError('Error: application home cannot be specified.')

    def load(self, file, relative=True):
        """
        Existing configurations can be overwritten by calling this function multiple times with different configuration files.
        """
        fullPath = file
        if relative is True:
            fullPath = self.appHome + '/' + file
        parser = ConfigParser.ConfigParser()
        parser.read(fullPath)
        for sectionName in parser.sections():
            sectionDict = dict(parser.items(sectionName))
            #print sectionName
            #print sectionDict
            # method 1
            #self.conf[sectionName] = sectionDict # but this method  cannot overwrite item-by-item.
            # method 2: correct.
            for (opt, val) in sectionDict.items():
                if sectionName in self.conf:
                    self.conf[sectionName][opt] = val
                else:
                    newDict = {}
                    newDict[opt] = val
                    self.conf[sectionName] = newDict

    def get(self, section, option):
        return self.getConfItem(section=section, option=option)

    def getConfItem(self, section, option):
        return self.conf[section][option]

    def set(self, section, option, value):
        return self.setConfItem(section=section, option=option, value=value)

    def setConfItem(self, section, option, value):
        self.conf[section][option] = value

    def showAllConf(self):
        for (k, v) in self.conf.items():
            print "[" + k + "]"
            for k2 in v.keys():
                print k2 + "=" + v[k2]




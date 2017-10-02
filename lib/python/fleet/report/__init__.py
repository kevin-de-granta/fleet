# -*- coding:utf-8 -*-

#
# File Name:    __init__.py
# Function:     To initialize a package.
# Created by:   Wenkai Wang (Kevin), ww288@cantab.net
# Created on:   2017/08/12
# Revised hist: revised by _____ on ____/__/__
#


from __future__ import unicode_literals
VERSION = "(1, 00, 0, 'final', 1)"
__version__ = VERSION


import sys
reload(sys)
sys.setdefaultencoding("utf-8")


#
# sys.dont_write_byte_code = True: for development only
# Otherwise, lots of .pyc files generated may possibly be automatically 
# uploaded to remote server by command 'git add <folder-name[not-file-name]>'.
# FINAL RELEASE: when finally released, this value should be False.
#
# sys.dont_write_byte_code = True


# import basic classes from within this packege
#from .env import Env



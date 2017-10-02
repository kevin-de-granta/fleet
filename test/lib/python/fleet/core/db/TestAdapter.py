# -*- coding:utf-8 -*-

#
# File Name:    TestAdapter.py
# Function:     To test class DbAdapter.
# Created by:   Wenkai Wang (Kevin), ww288@cantab.net
# Created on:   2017/10/02
# Revised hist: revised by _____ on ____/__/__
#


import unittest
from fleet.core.env_fleet import FleetCoreEnv
from fleet.core.db.adapter import DbAdapter
from fleet.core.db.map import FltSysVars, WfUsers


class TestDbAdapter(unittest.TestCase):
    def setUp(self):
        self.env = FleetCoreEnv.GetInstance()
        self.adapter = DbAdapter.GetInstance()

    def test_sys_vars(self):
        print "Listing system variable(s) from database:"
        sess = self.adapter.getReadSession()
        query = sess.query(FltSysVars).all()
        for row in query:
            print row.section + ": " + row.name + "=" + row.value + " [" + str(row.createTime) + "]"
        return True 

    def test_users(self):
        print "Listing user info:"
        sess = self.adapter.getReadSession()
        query = sess.query(WfUsers).all()
        for row in query:
            print row.uuid + ": " + row.name + ", " + row.email
        return True

    def tearDown(self):
        pass

if __name__ == '__main__':
    print "Testing database adapter:"
    env = FleetCoreEnv.GetInstance()
    adapter = DbAdapter.GetInstance()
    unittest.main()






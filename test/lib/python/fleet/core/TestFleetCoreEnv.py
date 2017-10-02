# -*- coding:utf-8 -*-

#
# File Name:    TestFleetEnv.py
# Function:     To test Env of Fleet Core
# Created by:   W. Wang (Kevin), ww288@cantab.net
# Created on:   2017/10/01
# Revised hist: revised by _____ on ____/__/__
#


import unittest
from fleet.core.env_fleet import FleetCoreEnv


class TestFleetCoreEnv(unittest.TestCase):
    def setUp(self):
        self.env = FleetCoreEnv.GetInstance()
        self.env.showAllConf()

    def test_db_name(self):
        dbName = self.env.get('database','dbname')
        self.assertEqual(dbName, 'FleetCore')

    def test_user_conf(self):
        userConf = self.env.get('misc', 'user_conf')
        self.assertEqual(userConf, '.fleet.ini')

    def tearDown(self):
        pass

if __name__ == '__main__':
    print "Testing env of Fleet Core:"
    unittest.main()
    #env = FleetCoreEnv.GetInstance()
    #env.showAllConf()





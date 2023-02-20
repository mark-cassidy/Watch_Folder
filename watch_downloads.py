# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:01:08 2022

@author: Mark Cassidy
"""

import os, time
path_to_watch = os.environ['USERPROFILE']+"/Downloads/"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (10)
  change = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in change if not f in before]
  removed = [f for f in before if not f in change]
  print(change.items())
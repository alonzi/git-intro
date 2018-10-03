#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:28:03 2018

@author: ep9k
"""

from datetime import datetime


serverlog = open('serverlog.txt', 'r')
initiated = []
complete = []
for line in serverlog:
    if 'Shutdown initiated.' in line:
        initiated.append(line)
    elif 'Shutdown complete.' in line:
        complete.append(line)

initiatedlist = []
for item in initiated:
    initiatedlist.append(item[5:24])

completedlist = []
for item in complete:
    completedlist.append(item[5:24])

#formats first item in initiatedlist with datetime.strptime(string, format)
#format is in regular expression syntax
beginning = datetime.strptime(initiatedlist[0], "%Y-%m-%dT%H:%M:%S" )

#formats last item in completedlist with datetime.striptime(string, format)
#format is in regular expression syntax
end = datetime.strptime(completedlist[-1],"%Y-%m-%dT%H:%M:%S")

print ("First shutdown initiated at:", initiatedlist[0])
print ("Last shutdown completed at:", completedlist[-1])
print ("Time elapsed:", end - beginning)




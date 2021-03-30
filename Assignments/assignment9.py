#!/usr/bin/env python

import os
from datetime import datetime as dt

date = []
time = []
size = []
name = []

for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        name.append(file)
        date.append(dt.fromtimestamp(os.stat(file).st_mtime).date())
        size.append(os.stat(file).st_size)
        time.append(dt.strptime(str(dt.fromtimestamp(os.stat(file).st_mtime).time())[
                    :5:], '%H:%M').strftime("%I:%M %P"))

for i in range(len(name)):
    print(date[i], "\t", time[i], "\t", size[i], "\t",
          name[i], "\t", 'Empty' if size[i] == 0 else '')

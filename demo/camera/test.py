# -*- coding: UTF-8 -*-
import os
str=os.popen('raspistill -w 100 -h 100 -q 10  -t 1 -o -').read()
print(str)
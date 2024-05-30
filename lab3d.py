#!/usr/bin/env python3
#Author: Ched Duloy
#Author ID: 185662210
#Date Created: 2024/05/30

import os
import subprocess

def free_space():
    com = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(com, stdout=subprocess.PIPE, shell=True)
    output, error=process.communicate()

#p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    return output.decode('utf-8').strip()


print(free_space())
#-*- coding:utf-8 -*-
#!/usr/bin/python
import os
from subprocess import call, check_output


def rm_dir(dir_name):
    cmd = "ls '{0}'".format(dir_name)
    call(cmd, shell=True)
    files_to_del = "'{0}'/*".format(dir_name)
    x = raw_input("Delete {0}? (y/n)".format(files_to_del))
    if x.upper() in ["Y", "YES"]:
        cmd = "rm -rf {0}".format(files_to_del)
        out = call(cmd, shell=True)
        if out != 0:
            print("Some error occurs when deleting {0}".format(files_to_del))


def cln_cmd(cmd):
    x = raw_input("Run {0}? (y/n)".format(cmd))
    if x.upper() in ["Y", "YES"]:
        out = call(cmd, shell=True)
        if out != 0:
            print("Some error occurs when running {0}".format(cmd))


USERNAME = os.getenv('USER')
if not USERNAME:
    raise ValueError('Username not found.')

garbage_dirs = [
    "Library/Application Support/法语助手",
    ".gradle/caches",
    ".electron",
    # https://stackoverflow.com/questions/29930198/can-i-delete-data-from-ios-devicesupport
    "Library/Developer/Xcode/iOS DeviceSupport",
    "Library/Containers/com.tencent.tenvideo/Data/Library/Caches",
    "Library/Containers/com.iqiyi.player/Data/Library/Application Support/com.iqiyi.player/Puma/Cache"
]

clean_cmds = [
    "brew cleanup -prune 1",
    # https://stackoverflow.com/questions/34910383/xcode-free-to-clear-devices-folder/34914591#34914591
    "xcrun simctl delete unavailable"
]

for dir_name in garbage_dirs:
    rm_dir("/Users/{0}/{1}".format(USERNAME, dir_name))
for cmd in clean_cmds:
    cln_cmd(cmd)

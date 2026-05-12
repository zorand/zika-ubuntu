#!/usr/bin/env python3
#
# signal-call-raiser.py
#
# Monitors DBus notifications and raises the Signal Desktop window
# when an incoming call is detected. Workaround for Signal/Electron
# not properly implementing xdg-activation on Linux/Wayland.
#
# Copyright (c) 2026 Zoran Dimitrijevic and Claude (Anthropic)
# SPDX-License-Identifier: BSD-3-Clause
#
# Part of zika-ubuntu: https://github.com/zorand/zika-ubuntu

import subprocess
import os

# DBus session bus address - derived from current user's runtime dir
uid = os.getuid()
os.environ['DBUS_SESSION_BUS_ADDRESS'] = f'unix:path=/run/user/{uid}/bus'

# Keywords to match incoming call notifications.
# Add your locale's translation of "Incoming call" here.
# English and Serbian (sr) included by default.
keywords = [
    'Incoming video call',
    'Incoming call',
    'Долазни видео позив',
    'Долазни позив',
]

LOG_FILE = '/tmp/signal-raiser.log'
SIGNAL_BIN = '/usr/bin/signal-desktop'

proc = subprocess.Popen(
    ['dbus-monitor', '--session', "interface='org.freedesktop.Notifications'"],
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,
    text=True,
    bufsize=1  # line buffered
)

for line in proc.stdout:
    for keyword in keywords:
        if keyword in line:
            with open(LOG_FILE, 'a') as f:
                f.write(f'Call detected: {line.strip()}\n')
            subprocess.Popen([SIGNAL_BIN])
            break

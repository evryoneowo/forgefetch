# standard instance. edit only renderer

import json

import psutil
import time
import os
import platform
import cpuinfo

import fetch
from renderer import renderer

with open('config.json') as f:
    parsed = json.loads(f.read())

ACCENT = parsed['accent_color']
RESET = parsed['reset_color']
SECONDARY = parsed['secondary_color']

boot_time = psutil.boot_time()
uptime_seconds = int(time.time() - boot_time)

days, remainder = divmod(uptime_seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

parts = list()

parts += [f'{days} days'] if days else []
parts += [f'{hours} hours'] if hours else []
parts += [f'{minutes} minutes'] if minutes else []
parts += [f'{seconds} seconds'] if seconds else []

shell_env = os.environ.get('SHELL').split('/')[-1]

user = os.getlogin()

fos = platform.uname().node

info = cpuinfo.get_cpu_info()
cpu = cpuinfo.get_cpu_info()['brand_raw']

fetchmain = fetch.Fetch(ACCENT, SECONDARY, RESET)

fetchmain.add('user', user)
fetchmain.add('os', fos)
fetchmain.add('cpu', cpu)
fetchmain.add('uptime', ', '.join(parts))
fetchmain.add('shell', shell_env)

def run():
    fetchmain.print()
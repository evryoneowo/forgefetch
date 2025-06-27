# standard instance. edit only renderer

import json

import psutil
import time
import os
import platform
import cpuinfo

import fetch

VERSION = '1.0'

with open('config.json') as f:
    parsed = json.loads(f.read())

ACCENT = parsed['accent_color']
RESET = parsed['reset_color']
SECONDARY = parsed['secondary_color']


if parsed['clear']:
    os.system('clear')

print(f'{ACCENT}\uf013{RESET} forgefetch v{VERSION}\nrenderer: {ACCENT}{parsed['renderer']}{RESET}\n')

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

fetchmain.add('uptime', ', '.join(parts))
fetchmain.add('shell', shell_env)
fetchmain.add('user', user)
fetchmain.add('os', fos)
fetchmain.add('cpu', cpu)

if __name__ == '__main__':
    fetchmain.print()
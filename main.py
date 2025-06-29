import json
import importlib
import os

VERSION = '1.2'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

home_dir = os.path.expanduser("~")
with open(os.path.join(home_dir, '.forgefetch')) as f:
    cfg = json.loads(f.read())

ACCENT = cfg['accent_color']
RESET = cfg['reset_color']
SECONDARY = cfg['secondary_color']

if cfg['clear']:
    os.system("clear")

print(f'{ACCENT}\uf013{RESET} forgefetch v{VERSION}')

ren = False
ins = False
renderer = cfg['renderer']
instance = cfg['instance']
if not os.path.exists('renderers/' + renderer+'.py'):
    print(f'renderer: \033[9m\x1b[1m{ACCENT}{renderer}\x1b[0m\033[9m{RESET}')

    ren = True
else:
    print(f'renderer: {ACCENT}\x1b[1m{renderer}\x1b[0m')

if not os.path.exists('instances/' + instance+'.py'):
    print(f'instance: \033[9m{ACCENT}\x1b[1m{instance}\x1b[0m\033[9m{RESET}\n')

    ins = True
else:
    print(f'instance: {ACCENT}\x1b[1m{instance}\x1b[0m{RESET}\n')

if ren:
    print(f'{ACCENT}\x1b[1m{renderer}\x1b[0m{RESET} renderer does not exist!')

if ins:
    print(f'{ACCENT}\x1b[1m{instance}\x1b[0m{RESET} instance does not exist!')

if ren or ins: exit(1)

instance_module = importlib.import_module(f'instances.{instance}')

instance_module.run()

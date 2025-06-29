import importlib
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

home_dir = os.path.expanduser("~")
with open(os.path.join(home_dir, '.forgefetch')) as f:
    parsed = json.loads(f.read())

def get_renderer(renderer_name):
    module = importlib.import_module(f'renderers.{renderer_name}')
    return getattr(module, renderer_name)

renderer = get_renderer(parsed['renderer'])

import importlib
import json

with open('config.json') as f:
    parsed = json.loads(f.read())

def get_renderer(renderer_name):
    module = importlib.import_module(renderer_name)
    return getattr(module, renderer_name)

renderer = get_renderer(parsed['renderer'])
import yaml

CONFIG = {}

def init(path):
    global CONFIG
    f = open(path)
    # use safe_load instead load
    CONFIG = yaml.safe_load(f)
    f.close()

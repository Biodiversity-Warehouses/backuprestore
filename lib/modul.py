import sys


def _get_modul(modulname):
    modul = None
    try:
        modules = __import__('modules.%s' % modulname)
        modul = getattr(modules, modulname)
    except:
        print("[%s] error finding module" % modulname, file=sys.stderr)
    return modul

def run(config,direction,time=None):
    if 'remote' not in config:
        print("error no destination defined")
        return
    remote = config['remote']

    if 'modules' not in config:
        print("error no modules defined")
        return

    print("start backup")

    for key in config['modules']:
        print("[%s] start backup" % key)
        params = config['modules'][key]
        modul = _get_modul(key)
        if modul is not None:
            dirFunc = getattr(modul, direction)
            if time is not None:
                dirFunc(remote,params,time)
            else:
                dirFunc(remote,params)
        print("[%s] end backup" % key)

    print("end backup")

def backup(config):
    run(config,'backup')

def restore(config,time):
    run(config,'restore',time)

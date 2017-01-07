
def log(args):
    print("[%s]"% __name__.split(".")[-1],args)

def backup(to, params):
    log("backup")

def restore(src,params,time):
    log("restore backup from %s" % time)

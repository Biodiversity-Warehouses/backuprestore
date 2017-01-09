
def log(*args, **kwargs):
    print("[%s]"% __name__.split(".")[-1],*args,**kwargs)

def backup(to, timemode, params):
    log("backup")
    log(params)

def restore(src,timemode, params,time):
    log("restore backup from %s" % time)
    log(params)

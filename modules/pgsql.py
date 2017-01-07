
def log(*args, **kwargs):
    print("[%s]"% __name__.split(".")[-1],*args,**kwargs)

def backup(to, params):
    log("backup")
    log(params)

def restore(src,params,time):
    log("restore backup from %s" % time)
    log(params)

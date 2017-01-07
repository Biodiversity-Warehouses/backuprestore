import os
import logging

def syncfile(host_from,path_from,host_to,path_to):
	cmd = "rsync root@%s:%s root@%s:%s" % (host_from,path_from,host_to,path_to)
	logging.debug("cmd: %s"%cmd)
	result = os.system(cmd)
	if result != 0:
		error("")


if __name__ == "__main__":
	import sys
	logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
	syncfile("localhost","~/b","localhost","~/d")

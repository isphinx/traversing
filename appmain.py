# coding:utf8

from gevent import monkey;

monkey.patch_os()
import json, sys
from gfirefly.server.server import FFServer

if __name__ == "__main__":
    args = sys.argv
    servername = None
    config = None
    if len(args) > 2:
        servername = args[1]
        config = json.load(open(args[2], 'r'))
    else:
        raise ValueError
    dbconf = config.get('db')
    memconf = config.get('memcached')
    sersconf = config.get('servers', {})
    masterconf = config.get('master', {})

    model_default_config = config.get('model_default', {})
    model_config = config.get('models', {})

    serconfig = sersconf.get(servername)
    ser = FFServer()
    ser.config(serconfig, servername=servername, dbconfig=dbconf, memconfig=memconf, masterconf=masterconf,
               model_default_config=model_default_config, model_config=model_config)
    ser.start()

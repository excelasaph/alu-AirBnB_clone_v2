#!/usr/bin/python3
from fabric.api import env, execute


do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    archive_path = do_pack()
    results = execute(do_deploy, archive_path=archive_path)
    return results

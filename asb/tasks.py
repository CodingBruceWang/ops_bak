# -*- coding: utf-8 -*-
import time
from celery import Celery
from celery import task
import commands
import os
import logging
from django.http.response import HttpResponse

# Create your views here.
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@task
def test_add(x, y):
    time.sleep(10)
    print '===================' + str(x + y)
    return x + y


def check_result(output):
    msg_success = 'failed=0'
    # result = "0" if msg_success in output else result = "-1"
    if msg_success in output:
        return True
    else:
        return False


def test():
    dir_base = 'base_path===%s' % base_path
    dir_inventory = base_path + '/asb/inventory'
    dir_playbook = base_path + '/asb/playbook'
    asb_web_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapache2.yml' % (dir_inventory, dir_playbook)
    logging.info('asb_cmd===%s' % asb_web_cmd)
    status_web, output_web = commands.getstatusoutput('bash -c %s' % asb_web_cmd)
    logging.info('status===%s, output===%s' % (status_web, output_web))
    logging.info('================================================================================================')
    if check_result(output_web):
        asb_app_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapp.yml' % (dir_inventory, dir_playbook)
        logging.info('asb_app_cmd===%s' % asb_app_cmd)
        status_app, output_app = commands.getstatusoutput('bash -c %s' % asb_app_cmd)
        if check_result(output_app):
            asb_cm_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/start_cm.yml' % (dir_inventory, dir_playbook)
            logging.info('asb_cm_cmd===%s' % asb_cm_cmd)
            status_cm, output_cm = commands.getstatusoutput('bash -c %s' % asb_cm_cmd)
    return HttpResponse('status===%s, output===%s' % (status_cm, output_cm))


@task
def start_mis1c10():
    logging.info('=================================enter start_mis1c10=================================')
    dir_inventory = base_path + '/asb/inventory'
    dir_playbook = base_path + '/asb/playbook'
    # 1. start web
    asb_web_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapache2.yml' % (dir_inventory, dir_playbook)
    status_web, output_web = commands.getstatusoutput('bash -c %s' % asb_web_cmd)
    # 2. start app
    if check_result(output_web):
        asb_app_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/startapp.yml' % (dir_inventory, dir_playbook)
        status_app, output_app = commands.getstatusoutput('bash -c %s' % asb_app_cmd)
    # 3. start cm
    if check_result(output_app):
        asb_cm_cmd = 'set -o pipfail;ansible-playbook -i %s/hosts %s/start_cm.yml' % (dir_inventory, dir_playbook)
        status_cm, output_cm = commands.getstatusoutput('bash -c %s' % asb_cm_cmd)
    logging.info('=================================out start_mis1c10=================================')
    return ''

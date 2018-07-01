from django.shortcuts import render
import logging
from django.http.response import HttpResponse

# Create your views here.

def test_vbs(request):
    logging.info('============================== vbs test ==============================')
    return HttpResponse('test')


def ansible_playbook(request):
    '''
    :param hosts list
    :param username
    :return: execute result
    '''
    

    return ''

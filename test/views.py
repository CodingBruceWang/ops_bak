from django.shortcuts import render
import logging
import os
import commands
from django.http.response import HttpResponse

from tools.mail_tool import MailTool

def test_mail(request):
    mail_tool = MailTool()
    # mail_tool.send_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'testing', 'smtp.163.com', '725wdmxksl163')
    mail_tool.send_mail('wangfoqing25@163.com', 'wangfoqing25@163.com', 'testing', 'smtp.163.com', 'wangfoqing25')
    return HttpResponse('testing...')

def angular(request):
    print("Bubble Sort: ")
    myList = [1, 4, 5, 0, 6]
    bubbleSort(myList)
    return render(request, "html/test.html")


def bubbleSort(myList):
    length = len(myList)
    for i in range(0, length - 1):
        for j in range(0, length - 1 - i):
            if myList[j] > myList[j + 1]:
                tmp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = tmp
        for item in myList:
            print(item)
            print("=============================")

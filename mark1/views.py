from django.shortcuts import render
from django.http import JsonResponse
import json
import MySQLdb
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def connectTodb(request):
    data = request.POST
    print(data)
    talkTdbServer(data['username'], data['password'], data['host'])
    dbcur.execute('show databases')
    dbs = dbcur.fetchall()
    resp = {'status': 'success', 'data': dbs}
    return JsonResponse(resp)


def  talkTdbServer(username, password, host):
    try:
        global dbfrom
        dbfrom = MySQLdb.connect(host, username, password)
        print("database connected ..")
        global dbcur
        dbcur = dbfrom.cursor()
    except:
        print("failed")


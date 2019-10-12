from django.shortcuts import render
from django.http import JsonResponse
import json
import MySQLdb
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def connectTodb(request):
    data = request.POST
    talkTdbServer(data['username'], data['password'], data['host'], data['dbname']) if 'dbname' in data else talkTdbServer(data['username'], data['password'], data['host'])
    sql  = 'show tables' if 'dbname' in data else 'show databases'
    dbcur.execute(sql)
    dbs = dbcur.fetchall()
    resp = {'status': 'success', 'data': dbs}
    return JsonResponse(resp)


def  talkTdbServer(username, password, host, dbname = False):
    try:
        global dbfrom
        if not dbname:
            dbfrom = MySQLdb.connect(host, username, password)
        else:
            dbfrom = MySQLdb.connect(host, username, password, dbname)
        print("database connected ..")
        global dbcur
        dbcur = dbfrom.cursor()
    except:
        print("failed")
    
@csrf_exempt
def tableDescribe(request):
    data = request.POST
    pass

def talkTotable(data):
    pass


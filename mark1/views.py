from django.shortcuts import render
from django.http import JsonResponse
import json
import MySQLdb
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def connectTodb(request):
    data = request.POST
    if 'username' not in data or 'password' not in data or 'host' not in data:
        return JsonResponse({'status': 'error', 'data': data, 'msg': 'data is missing'})
    talkTdbServer(data['username'], data['password'], data['host'], data['dbname']) if 'dbname' in data else talkTdbServer(data['username'], data['password'], data['host'])
    sql  = 'show tables' if 'dbname' in data else 'show databases'
    dbcur.execute(sql)
    dbs = dbcur.fetchall()
    newlist = []
    for val in dbs:
        # print(val[0]) 
        newlist.append(val[0])
    resp = {'status': 'success', 'data': newlist}
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
    talkTdbServer(data['username'], data['password'], data['host'], data['dbname'])
    resp = talkTotable(data)
    return JsonResponse({'status': 'success', 'data': resp})

def talkTotable(data):
    sql = 'desc ' + str(data['tableName'])
    dbcur.execute(sql)
    tbDetail = dbcur.fetchall()
    print(tbDetail)
    tblist = []
    for val in tbDetail:
        tblist.append(val[0])
    print(tblist)
    return tblist

'''
Api Params: {
                ['s1'] = 'server 1 credential',
                ['s2'] = 'server 2 credential',
                ['data'] = {    
                                {   
                                    'name' : 'username',
                                    'val': 'Anuj Singh'
                            }
            }
'''
@csrf_exempt
def startMyMigrations(request):
    data = request.POST
    print(data)
    pass


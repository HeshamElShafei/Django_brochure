#-*:utf-8 -*-
import string
#from coreapp.models import Tasklist
def findall(db_object):
    try:
       res = db_object.objects.all()
    except:
       res = None
    return res
def findallif(db_object,data):
    try:
       res = db_object.objects.filter(**data).order_by('id')
    except:
       res = None
    return res
def findallexcept(db_object,data):
    try:
       res = db_object.objects.all().exclude(**data).order_by('id')
    except:
       res = None
    return res
def finddata(db_object,data):
    try:
       res = db_object.objects.get(**data)
    except:
       res = None 
    return res
def savedata(db_object,name1,number1,club1,membership1,option1):
    try:
       print 'hello'
       db_object.objects.create(name= name1, number= number1, club_name=club1, membership=membership1, option=option1)
       res = 1
    except:
       res = 0
    return res
def updatedata(db_object,data,storedata):
    db_object.objects.filter(**data).update(**storedata)
    #return data
def deldata(db_object,data):
    res = False
    try:
       db_object.objects.get(**data).delete()
       res = True
    except:
       pass
    return res
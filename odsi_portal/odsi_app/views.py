from django.shortcuts import render
from urllib import urlencode
from django.http import *
from django.conf import settings
import pdb

import urllib2
import simplejson as json
import time
import json
import ast

def odsi_portal_homepage(request):
    return render(request,'homepage.html')
 
def loginbutton_openstack(request):
   # pdb.set_trace()
    openstack_username=request.POST.get('openstack_username')
    openstack_password=request.POST.get('openstack_password')
    service_id=request.POST.get('os_form_serviceid')
    product_id=request.POST.get('os_form_productid')
    productname=request.POST.get('os_form_productname')
    os=request.POST.get('os_form_os')
    version=request.POST.get('os_form_version')
    architecture=request.POST.get('os_form_architecture')    
    dic={"openstack_username":openstack_username,"openstack_password":openstack_password}
    url=settings.AUTHENTICATE_URL
    jsondata = json.dumps(dic)
    req = urllib2.Request(url, \
                         headers = {

                                     "Content-Type": "application/json",
                                   },                        \
                         data = jsondata)
    f = urllib2.urlopen(req)
    response = f.read()
    res = json.loads(response)

    return render(request,"total_details.html",locals())

def final_form_submit(request):
    pdb.set_trace()
    service_id=request.POST.get('final_form_serviceid')
    product_id=request.POST.get('final_form_productid')
    productname=request.POST.get('final_form_productname')
    version=request.POST.get('final_form_version')
    architecture=request.POST.get('final_form_architecture')
    openstack_username=request.POST.get('final_form_openstack_username')
    openstack_password=request.POST.get('final_form_openstack_password')

    type="cloud" 
    username="odsiportaluser"
    url=settings.REQUEST_BOOT_VM_URL
    dictionary_boot_vm={"username":username,"service_id":service_id,"product_id":product_id,"machine_details":{"ip_address":"","machine_username":"","machine_password":""},"openstack_details":{"openstack_username":openstack_username,"openstack_password":openstack_password},"parameters":{},"machine_availability":"","request_type":"Software","os":"linux"}
    jsondata = json.dumps(dictionary_boot_vm)
    req = urllib2.Request(url, \
                         headers = {

                                     "Content-Type": "application/json",
                                   },                        \
                         data = jsondata)
    f = urllib2.urlopen(req)
    response = f.read()
    res = json.loads(response)
    return render(request,"page.html",locals())


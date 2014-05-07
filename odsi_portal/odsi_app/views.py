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
 
def login_button_openstack(request):
 #   pdb.set_trace()
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
def login_button_available(request):
    #pdb.set_trace();
    available_username=request.POST.get('available_username')
    available_password=request.POST.get('available_password')
    available_ipaddress=request.POST.get('available_ipaddress')
    service_id=request.POST.get('available_form_serviceid')
    product_id=request.POST.get('available_form_productid')
    productname=request.POST.get('available_form_productname')
    os=request.POST.get('available_form_os')
    version=request.POST.get('available_form_version')
    architecture=request.POST.get('available_form_architecture')
  #  dic={"openstack_username":available_username,"openstack_password":available_password}
    dic={"ip_address":available_ipaddress,"os":os,"architecture":"x86_64","user_name":available_username,"user_password":available_password}
    url=settings.VALIDATE_AVAILABLE_URL
    jsondata = json.dumps(dic)
    req = urllib2.Request(url, \
                         headers = {

                                     "Content-Type": "application/json",
                                   },                        \
                         data = jsondata)
    f = urllib2.urlopen(req)
    response = f.read()
    res = json.loads(response)
    if res[0]=='true':
          url=settings.REQUEST_BOOT_VM_URL
          dictionary_boot_vm={"username":"odsiUSER","service_id":service_id,"product_id":product_id,"machine_details":{"ip_address":available_ipaddress,"machine_username":available_username,"machine_password":available_password},"openstack_details":{"openstack_username":"","openstack_password":""},"parameters":{},"machine_availability":"Available","request_type":"Software","os":"linux"}
          jsondata = json.dumps(dictionary_boot_vm)
          req = urllib2.Request(url, \
                         headers = {

                                     "Content-Type": "application/json",
                                   },                        \
                         data = jsondata)
          f = urllib2.urlopen(req)
          response = f.read()
          res = json.loads(response)         
          return render(request,"submission_available_page.html",locals())
    else : 
          return render(request,"submission_available_fail.html",locals())
 




def final_form_submit(request):
    #pdb.set_trace()
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


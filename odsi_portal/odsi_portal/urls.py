from django.conf.urls import patterns, include, url
from odsi_app.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'odsi_portal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^odsiportal/',odsi_portal_homepage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^loginbutton_openstack/',login_button_openstack),
    url(r'^final_form_submit/',final_form_submit),
    url(r'^availablemachine_button/',login_button_available),

)

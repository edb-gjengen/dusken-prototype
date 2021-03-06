from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api

from dusken.api.address import AddressResource
from dusken.api.division import DivisionResource
from dusken.api.me import MeResource
from dusken.api.member import MemberResource, MemberCreateResource
from dusken.api.membership import MembershipResource
from dusken.api.group import GroupResource
from dusken.api.institution import InstitutionResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(AddressResource())
v1_api.register(DivisionResource())
v1_api.register(GroupResource())
v1_api.register(InstitutionResource())
v1_api.register(MemberResource())
v1_api.register(MembershipResource())
v1_api.register(MeResource())

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)

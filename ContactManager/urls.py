from django.urls import include, path
from .views import create_contact , home ,contact_detail,sn ,download_vcard,get_contacts,edit_serial_number ,edit_contact
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('contacts/create/', create_contact, name='create_contact'),
    path('contact/edit/<str:serial_number>/', edit_contact, name='edit_contact'),
    path('contacts/<str:serial_number>/', contact_detail, name='contact_detail'),
    path('contacts/', get_contacts, name='contacts'),
    path('edit/<str:serial_number>/', edit_serial_number, name='edit_serial_number'),
    path('SN/<str:serial_number>/', edit_contact, name='edit_contact_SN'),
    path('SN/', sn, name='edit_contact_SN'),
    path('', home, name='home'),

    path('download-vcard/<str:serial_number>/', download_vcard, name='download_vcard')



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


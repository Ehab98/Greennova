from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
import qrcode
from django.utils import translation
from django.contrib import messages
import logging
from django.conf import settings
from django.urls import reverse
from django.utils.translation import get_language, activate, gettext
from django.utils.translation import activate

def set_language_from_url(request, user_language):
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # I use HTTP_REFERER to direct them back to previous path 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(cur_language)
    return text



logger = logging.getLogger(__name__)

import random

def home(request):


    return render(request, 'ContactManager/index.html')

def edit_serial_number(request, serial_number):
    try:
        obj = Contact.objects.get(serial_number=serial_number)
    except Contact.DoesNotExist:
        return redirect('home') # replace 'home' with the name of your home page URL
    return render(request, 'ContactManager/edit_contact.html', {'obj': obj})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Check if a Contact with the same serial number already exists
            serial_number = form.cleaned_data['serial_number']
            existing_contact = Contact.objects.filter(serial_number=serial_number).first()
            if existing_contact:
                # Check if the existing contact needs to be updated
                if form_has_changes(form, existing_contact):
                    form = ContactForm(request.POST, instance=existing_contact)
                    contact = form.save()
                    messages.success(request, ("Contact with serial number %(serial_number)s has been updated.") % {'serial_number': serial_number})
                else:
                    contact = existing_contact
                    messages.info(request, ("No changes were made to contact with serial number %(serial_number)s.") % {'serial_number': serial_number})
            else:
                # Create a new Contact instance with the form data
                contact = form.save()
                messages.success(request, ("Contact with serial number %(serial_number)s has been created.") % {'serial_number': serial_number})
            logger.info('Contact saved: %s', contact.full_name)
            return redirect('contact_detail', pk=contact.pk, serial_number=serial_number)
        else:
            logger.error('Form is invalid: %s', form.errors)
    else:
        form = ContactForm()
    return render(request, 'ContactManager/add_contact.html', {'form': form})

def form_has_changes(form, instance):
    """
    Check if the form data has any changes compared to the existing instance.
    """
    for field in form.fields:
        if form.cleaned_data.get(field) != getattr(instance, field):
            return True
    return False


import vobject
from django.http import HttpResponse

def download_vcard(request, serial_number):
    contact = get_object_or_404(Contact, serial_number=serial_number)
    contact.full_name = request.POST.get('full_name')
    contact.company = request.POST.get('company')
    contact.branch = request.POST.get('branch')
    contact.department = request.POST.get('department')
    contact.title = request.POST.get('title')
    contact.ext_number = request.POST.get('ext_number')
    contact.phone = request.POST.get('phone')
    contact.phone1 = request.POST.get('phone1')
    contact.phone2 = request.POST.get('phone2')
    contact.email = request.POST.get('email')
    contact.website_link = request.POST.get('website_link')
    contact.whatsapp_link = request.POST.get('whatsapp_link')
    contact.facebook_link = request.POST.get('facebook_link')
    contact.twitter_link = request.POST.get('twitter_link')
    contact.tiktok_link = request.POST.get('tiktok_link')
    contact.instagram_link = request.POST.get('instagram_link')
    contact.zoom_link = request.POST.get('zoom_link')
    contact.teams_link = request.POST.get('teams_link')
    contact.telegram_link = request.POST.get('telegram_link')
    contact.gmail_link = request.POST.get('gmail_link')
    contact.outlook_link = request.POST.get('outlook_link')
    contact.linkedIn_link = request.POST.get('linkedIn_link')
    contact.Messaanger_link = request.POST.get('Messaanger_link')
    contact.address = request.POST.get('address')
    # Get contact information from request
    # name = request.POST.get('name')
    # email = request.POST.get('email')
    # phone = request.POST.get('phone')
    
    # Create vCard object
    vcard = vobject.vCard()
    vcard.add('FN').value = contact.full_name
    vcard.add('EMAIL').value = contact.email
    vcard.add('TEL').value = contact.phone
    # vcard.add('Location').value = contact.address
    vcard.add('ORG').value = ('' + contact.company + '',)
    vcard.add('TITLE').value = contact.title
    vcard.add('URL').value = contact.website_link
    
    # Set response content type and headers
    response = HttpResponse(vcard.serialize(), content_type='text/x-vcard')
    response['Content-Disposition'] = 'attachment; filename="contact.vcf"'
    return response

from django.utils import timezone
from django.utils.translation import get_language

def edit_contact(request, serial_number):
    print('serial_number:', serial_number)  # Add this line to print out the serial_number parameter

    language_code = get_language()

    contact = get_object_or_404(Contact, serial_number=serial_number)


    if request.method == 'POST':
        # Update the contact fields with the submitted form data
        contact.full_name = request.POST.get('full_name')
        contact.company = request.POST.get('company')
        contact.branch = request.POST.get('branch')
        contact.department = request.POST.get('department')
        contact.title = request.POST.get('title')
        contact.ext_number = request.POST.get('ext_number')
        contact.phone = request.POST.get('phone')
        contact.phone1 = request.POST.get('phone1')
        contact.phone2 = request.POST.get('phone2')
        contact.email = request.POST.get('email')
        contact.website_link = request.POST.get('website_link')
        contact.whatsapp_link = request.POST.get('whatsapp_link')
        contact.facebook_link = request.POST.get('facebook_link')
        contact.twitter_link = request.POST.get('twitter_link')
        contact.tiktok_link = request.POST.get('tiktok_link')
        contact.instagram_link = request.POST.get('instagram_link')
        contact.zoom_link = request.POST.get('zoom_link')
        contact.teams_link = request.POST.get('teams_link')
        contact.telegram_link = request.POST.get('telegram_link')
        contact.gmail_link = request.POST.get('gmail_link')
        contact.outlook_link = request.POST.get('outlook_link')
        contact.linkedIn_link = request.POST.get('linkedIn_link')
        contact.Messaanger_link = request.POST.get('Messaanger_link')
        contact.address = request.POST.get('address')


        # Update the date_updated field to the current time
        contact.date_updated = timezone.now()
        
        # Save the updated contact object to the database
        contact.save()
        # Construct the redirect URL
        redirect_url = reverse('contact_detail', kwargs={'serial_number': contact.serial_number})

        # Add a success message
        success_message = 'Contact updated successfully. You will be redirected to the contact detail page at {}.'.format(redirect_url)
        messages.success(request, success_message)

        return redirect(redirect_url)
    else:
            # If the user cancels the save action, return the edit page again
        return render(request, 'ContactManager/edit_contact.html', {'contact':contact , 'LANGUAGE_CODE': language_code})

def get_contacts(request):
    contacts = Contact.objects.all()
    
    context = {
        'contacts':contacts
    }
    return render(request,'ContactManager/all_contacts.html',context)
def sn(request):
    if request.method == 'POST':
        serial_number = request.POST.get('serial_number', '')
        if serial_number:
            url = reverse('edit_contact_SN', kwargs={'serial_number': str(serial_number)})
            return redirect(url)
    return render(request, 'ContactManager/SN.html')



def contact_detail(request, serial_number):
    contact = get_object_or_404(Contact, serial_number=serial_number)
    language_code = get_language()

    return render(request, 'ContactManager/contact_detail.html', {'contact': contact , 'LANGUAGE_CODE': language_code})


    # # Generate a QR code for the contact's phone number
    # qr = qrcode.QRCode(version=1, box_size=10, border=5)
    # qr.add_data(contact.phone1)
    # qr.make(fit=True)
    # img = qr.make_image(fill='black', back_color='white')
    # # Render the contact detail page with the QR code image
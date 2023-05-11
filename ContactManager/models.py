from io import BytesIO
from django.db import models
import qrcode
class Contact(models.Model):
    serial_number = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=255,null=True,blank=True)
    company = models.CharField(max_length=255,null=True,blank=True)
    branch = models.CharField(max_length=255,null=True,blank=True)
    department = models.CharField(max_length=255,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    ext_number = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=14,null=True,blank=True)
    phone1 = models.CharField(max_length=14,null=True,blank=True)
    phone2 = models.CharField(max_length=14,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    website_link = models.CharField(max_length=255,null=True,blank=True)
    whatsapp_link = models.CharField(max_length=255,null=True,blank=True)
    facebook_link = models.CharField(max_length=255,null=True,blank=True)
    twitter_link = models.CharField(max_length=255,null=True,blank=True)
    tiktok_link = models.CharField(max_length=255,null=True,blank=True)
    instagram_link = models.CharField(max_length=255,null=True,blank=True)
    zoom_link = models.CharField(max_length=255,null=True,blank=True)
    teams_link = models.CharField(max_length=255,null=True,blank=True)
    telegram_link = models.CharField(max_length=255,null=True,blank=True)
    gmail_link = models.CharField(max_length=255,null=True,blank=True)
    outlook_link = models.CharField(max_length=255,null=True,blank=True)
    linkedIn_link = models.CharField(max_length=255,null=True,blank=True)
    Messaanger_link = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)

    date_updated = models.DateTimeField(auto_now=True)
    qr_code = models.BinaryField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate QR code image and store as binary data in qr_code field
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        data = ""
        if self.full_name:
            data += f"Name: {self.full_name}\n"
        if self.company:
            data += f"Company: {self.company}\n"
        if self.branch:
            data += f"branch: {self.branch}\n"
        if self.department:
            data += f"department: {self.department}\n"
        if self.title:
            data += f"title: {self.title}\n"
        if self.ext_number:
            data += f"ext_number: {self.ext_number}\n"
        if self.phone:
            data += f"phone: {self.phone}\n"
        if self.phone1:
            data += f"phone1: {self.phone1}\n"
        if self.phone2:
            data += f"phone2: {self.phone2}\n"
        if self.email:
            data += f"email: {self.email}\n"
        if self.website_link:
            data += f"website_link: {self.website_link}\n"
        if self.whatsapp_link:
            data += f"whatsapp_link: {self.whatsapp_link}\n"
        if self.facebook_link:
            data += f"facebook_link: {self.facebook_link}\n"
        if self.twitter_link:
            data += f"twitter_link: {self.twitter_link}\n"
        if self.tiktok_link:
            data += f"tiktok_link: {self.tiktok_link}\n"
        if self.instagram_link:
            data += f"instagram_link: {self.instagram_link}\n"
        if self.zoom_link:
            data += f"zoom_link: {self.zoom_link}\n"
        if self.teams_link:
            data += f"teams_link: {self.teams_link}\n"
        if self.telegram_link:
            data += f"telegram_link: {self.telegram_link}\n"
        if self.gmail_link:
            data += f"gmail_link: {self.gmail_link}\n"
        if self.outlook_link:
            data += f"outlook_link: {self.outlook_link}\n"
        if self.linkedIn_link:
            data += f"linkedIn_link: {self.linkedIn_link}\n"
        if self.Messaanger_link:
            data += f"Messaanger_link: {self.Messaanger_link}\n"
        if self.address:
            data += f"address: {self.address}\n"

        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='#0d6c3f', back_color='white')
        output = BytesIO()
        img.save(output, format='PNG')
        self.qr_code = output.getvalue()
        output.close()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.serial_number
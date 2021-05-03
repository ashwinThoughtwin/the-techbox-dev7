from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from Tech_Box_Project.settings import EMAIL_HOST_USER
from .models import TechBox


@receiver(post_save, sender=TechBox)
def send_new_gadget_add_notification_email(sender, instance, created, **kwargs):

    # if a new gadget is created, compose and send the email
    if created:
        name = instance.name
        subject = "New Gadget Added To TechBox"
        message = f"{name} has been added to TechBox."
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            ['mvaibhav002@gmail.com'],
            fail_silently=False,
        )
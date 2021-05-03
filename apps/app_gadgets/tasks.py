from __future__ import absolute_import, unicode_literals

from celery import shared_task

from celery.utils.log import get_task_logger

from django.core.mail import send_mail
from Tech_Box_Project.settings import EMAIL_HOST_USER

from datetime import datetime, timedelta

logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    return x + y

@shared_task()
def send_confirm_email_task(subject, message, recipient):
    logger.info("Confirmation Email Sent.")
    send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)


@shared_task()
def send_remember_email_task(subject, message, recipient, expire_date):
    logger.info("returning Email Sent.")
    send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)






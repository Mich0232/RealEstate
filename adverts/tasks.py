""" Insert your Celery tasks here
"""
from celery.task import task

from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

# celery -A <appname> worker -l info - run command

@task
def advert_add_mail(data, receiver='superuser'):
    """
        If AdvertReportForm is valid,
        Task sends mail with form data, to predefined receiver (superuser)

        :argument receiver: e-mail adress of receiver, if default: import from settings
        :argument data: form clean data
    """
    mail_receiver = settings.EMAIL_RECEIVER if receiver is 'superuser' else receiver

    msg_html = render_to_string('adverts/mail/advert_report_message.html', data)
    msg_text = render_to_string('adverts/mail/advert_report_message.txt', data)
    mail = send_mail('Zgłoszono nową ofertę', msg_text, settings.EMAIL_HOST_USER, [mail_receiver],
                     html_message=msg_html, fail_silently=False)
    return mail

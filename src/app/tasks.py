from flask_mail import Message
from flask import current_app
from app import mail
from celery import shared_task


@shared_task
def send_async_newsletter(subject, recipients, html_body):
    msg = Message(subject, recipients=recipients)
    msg.html = html_body
    mail.send(msg)


def send_newsletter(subject, recipients, html_body):
    send_async_newsletter.delay(subject, recipients, html_body)

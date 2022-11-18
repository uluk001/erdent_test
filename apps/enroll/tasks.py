# from erdent.celery import app

from django.core.mail import send_mail


# @app.task
def send_to_email(email,full_name,doctor):
    send_mail(
        f'Привет,{full_name} ',
        f'Вы записались на Филиал {doctor},\nНаш оператор скоро свяжется с вами насчет даты и времени записи',
        'erdent_client@mail.ru',
        [email],
        fail_silently=False,
        )
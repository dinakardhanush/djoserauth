from djoser import email


class ActivationEmail(email.ActivationEmail):
    template_name = 'djoser/email/activation_email.txt'

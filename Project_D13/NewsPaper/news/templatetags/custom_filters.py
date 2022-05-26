import random
from django import template

register = template.Library()

CENSURE = ['путь', 'скроллом', 'доклад', 'санкции']


@register.filter(name='censor')
def censor(value):
    chars = ["*","*","*","*","*","*","*","*","*","*","*","*"]
    primary_text = value.split(' ')
    text = value.lower().split(' ')
    for i in range(len(text)):
        if text[i] in CENSURE:
            primary_text[i] = ''.join(random.sample(chars, len(text[i])))

    return ' '.join(primary_text)
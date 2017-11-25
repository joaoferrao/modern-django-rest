from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='lba85^w6*j#h-$fi1@r*z717!iu%6o&5i&0^gq2hfv6fa1qg8a')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

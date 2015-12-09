import os

from django.http import HttpResponse

import xxtea

key = os.urandom(16)
data = os.urandom(19)
enchex = xxtea.encrypt_hex(data, key)

def index(request):
    a = xxtea.encrypt_hex(data, key)
    b = xxtea.decrypt_hex(enchex, key)
    return HttpResponse(a + " " + b)

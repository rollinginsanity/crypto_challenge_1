import hashlib
import sys
from cryptography.fernet import Fernet
import base64





def main():
    global enc1
    global enc2
    enc1 = "Z0FBQUFBQmRhZTB5RTZ0S1ZBRml6cjk4bU1nYUpzaWtPUVp2VmtrQjFjdGxzaDRBZ18xV1A5MUNXc0ZxMEQybzJULVBSbS1LUFl4eGNuRFZDQlBnQkpzRTRXeU45WGJzVGNjQ3hQcmxmZWJtR05sdUdnQzN2WGM9"

    key = input("Type in the password homes: ")
    salty = "chefs_salty_chocolate_ballz"
    alpha = "ZnVuY3Rpb242"
    key = key + salty
    for _ in range(1000):
        key = hashlib.sha3_256(key.encode()).hexdigest()
    key = key[:32]
    key = base64.urlsafe_b64encode(key.encode())
    enc2 = "cGFzc3dvcmRzYXJlc2hpdHQtLWJ1dC0taGF2ZWloaWRkZW4tLWFwYXNzd29yZGluLWhlcmVzb21ld2hlcmVteWJveS0tdGhhdHN1cGZvcnlvdXRvZmluZC0tZ2V0cmVhbHNvbi0ta2VlcGl0dXAtLWhhaGFoYWgw"
    todecrypt = enc2
    arg = ""
    val = ""
    try:
        arg = sys.argv[1]
        val = sys.argv[2]
    except Exception:
        print("Meh")
        print(key)
    cryptinator = Fernet(key)

    if arg == "enc":
        to_enc = val
        print("Encrypting "+to_enc+" with key")

        enc_output = cryptinator.encrypt(to_enc.encode())
        print(enc_output)
        print(base64.b64encode(enc_output))
    else:
        todecrypt = enc1
        for i in range(4000):
            if i % 4 == 0:
                todecrypt = enc1
            if i % 33 == 0:
                todecrypt = enc2
        print("enc1 "+enc1)
        print("enc2 "+enc2)
        print(todecrypt)
        print(cryptinator.decrypt(globals()[base64.b64decode(alpha.encode()).decode("utf-8")](todecrypt)))



def function1(var):
    var = ""
    var = 1
    var= 1+1
    return var

def function2(var):
    return var

def function3(var):
    var = ""
    var = 1
    var= 1+1
    return var

def function4(var):
    return var


def function5(var):
    var = ""
    var = 1
    var= 1+1
    return var

def function6(var):
    print(enc1)
    return base64.b64decode(enc1.encode())
def function7(var):
    return var


def function8(var):
    var = ""
    var = 1
    var= 1+1
    return var

def function9(var):
    return var


def function10(var):
    var = ""
    var = 1
    var= 1+1
    return var

main()
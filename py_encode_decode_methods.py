import base64

suma = "ashok123"
# usha = suma.encode("UTF-8")
ashok = base64.b64decode(suma)
vishwa = ashok.decode("UTF-8")
print(f"decoded string: {vishwa}")




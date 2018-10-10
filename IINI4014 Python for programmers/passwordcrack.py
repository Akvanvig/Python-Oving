import hashlib
import binascii
import time

teksten = ''
salt = 'Saltet til Ola'
solved = False
start = time.time()

for a in range(0, 52):
    if solved:
        break
    for b in range(0,52):
        if solved:
            break
        for c in range(0,52):
            if solved:
                break
            if a < 26:
                teksten = chr(97 + a)
            else:
                teksten = chr(65 + a - 26)
            if b < 26:
                teksten += chr(97 + b)
            else:
                teksten += chr(65 + b - 26)
            if c < 26:
                teksten += chr(97 + c)
            else:
                teksten += chr(65 + c - 26)

            derived_key = hashlib.pbkdf2_hmac("sha1", teksten.encode(), salt.encode(), 2048)
            derived_key = binascii.hexlify(derived_key).decode()
            print (teksten + ' : ' + derived_key)
            if derived_key == 'ab29d7b5c589e18b52261ecba1d3a7e7cbf212c6':
                print ('passordet er: ' + teksten)
                solved = True
slutt = time.time()
print('{0:.3f} seconds'.format((slutt - start)))

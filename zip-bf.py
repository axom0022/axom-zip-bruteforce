import zipfile
import itertools
import string

input("Press Enter to start...")

def bruteforcezip(zippath, maxlength=4):
    chars = string.ascii_lowercase + string.digits
    zf = zipfile.ZipFile(zippath)
    for length in range(1, maxlength + 1):
        for guess in itertools.product(chars, repeat=length):
            password = ''.join(guess)
            print("Trying: " + password)
            try:
                zf.extractall(pwd=password.encode())
                print("Found: " + password)
                return password
            except:
                pass
    print("Not found | the password might be longer than 4 letters/numbers")
    return None

zippath = input("Enter zip path: ")
bruteforcezip(zippath)

import re
import requests

username = ""
passwort = ""

moodledomain = "https://lernplattform.gfn.de/"
loginpath = "/login/index.php"

#---------pip install requests im terminal vorher installieren------#

def main():
    mysession = requests.session()
    r1 = mysession.get(url=moodledomain+loginpath)
    haystack = r1.text

    regex = '"logintoken" value="([^"]+)"'
    logintoken_match = re.search(regex, haystack)

    if logintoken_match:
        logintoken = logintoken_match.group(1)
        print("Token found:", logintoken)
        data = {
            'anchor': '',
            'logintoken': logintoken,
            'username': "X-hier eingabe-X",
            'password': "X-hier eingabe-X"
        }
        r2 = mysession.post(url=moodledomain+loginpath, data=data)
        haystack = r2.text

        regex = "Ungültige Anmeldedaten. Versuchen Sie es noch einmal!"
        fail_string = re.search(regex, haystack)

        if not fail_string:
            print("Login Successful")
            r3 = mysession.get(moodledomain, params={"stoppen": 1})
            print(r3.text)
        else:
            print("Login failed")
    else:
        print("Token not found")


main()

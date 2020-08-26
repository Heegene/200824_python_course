#password-locker

import pyperclip

PASSWORDS = {
    'gmail' : 'kkk',
    'naver' : 'kongE',
    'daum' : 'asdfasfdf'
}

def main():
    site = input('input your site \n')
    password = PASSWORDS[site]

    if password:
        pyperclip.copy(password)
        print('Your password is copied')
    else:
        print("not valid site")

main()



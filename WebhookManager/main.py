###################################
#     Encording: UTF-8            #
#     Author: BuRaPotE(Start-P)   #
#     Editor: Visual Studio Code  #
###################################


import requests
from sys import exit as endscript
def main():
  s = requests.Session() # define session
  url = input('Put your webhook url \n')
  check = input('Do u more infomation in config.json?' [y/n] \n)
  if check != 'y':
    print('Please put more infomation to config.json!')
    endscript()
  else:
    send()
def send():
  data = open('config.json',mode='r')
  try:
    content = data['content']
    icon = data['content']
    name = data['content']
  except KeyError:
    print('Maybe config.json is in invalid character or null.')
    endscript()
  try:
    data2 = {
      'content':content,
      'avatar_url':icon,
      'username':name
    }
    r = s.post(url,data=data2)
    if r.status_code == 200:
      print('Success Send!')
      check2 = input('Do you need send more? [y/n] \n')
      if check == y:
        main()
      else:
        print('Okay! Thanks for using!')
        endscript()
    else:
      print(f'Error! Status code is {str(r.status_code)}! TRy again :)') 
      main()
  except Exception as error:
    print('Sorry! We have some errors... \n Here is error code!\n')
    print(error)
    endscript()
 
if __name__ == '__main__':
  main()

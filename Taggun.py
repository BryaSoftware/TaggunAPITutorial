import requests

url = 'https://api.taggun.io/api/receipt/v1/simple/file'

headers = {'apikey': 'yourapikey'}

files = {
  'file': (
    '1_Dinner.jpg', # set a filename for the file
    open('1_Dinner.jpg', 'rb'), # the actual file
    'image/jpg'), # content-type for the file

  # other optional parameters for Taggun API (eg: incognito, refresh, ipAddress, language)
  'incognito': (
    None, #set filename to none for optional parameters
    'false') #value for the parameters
  }

response = requests.post(url, files=files, headers=headers)

print(response.content)
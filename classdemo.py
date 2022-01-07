import request
print("number taka")
number=input()
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message= Please return your Library book &language=english&route=p&numbers=" + number
headers = {'authorization': "SvbMBw3BMNBHYHT64ZNoWT3cqIryPondGNbXHoxEuNBnbK2kQYI6ifqvrtOc",
           'Content-Type': "application/x-www-form-urlencoded",
           'Cache-Control': "no-cache", }
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
import http.client
import json

api_key = "AIzaSyDIWw8tYzvYxUmyLWIN4G75-45Q6i4ckQ8"
msg = 'Amazon is sending you a refunding of $32.64. Please reply with your bank account and routing number to receive your refund.'

conn = http.client.HTTPSConnection("generativelanguage.googleapis.com")


headers = {
    "Content-Type": "application/json"
}
payload = json.dumps({
    "contents": [{
        "parts": [{"text": f"{msg} tell me above message is froud/spam/harmful or not ONLY ANSWER IN YES OR NO. DO NOT GENERATE ANY OTHER TEXT."}]
    }]
})


conn.request("POST", f"/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}", payload, headers)

response = conn.getresponse()
data = response.read()
jsondata = json.loads(data.decode("utf-8"))
ans = jsondata['candidates'][0]['content']['parts'][0]['text']
ans = ans.replace(' ','').replace('\n','').lower()
if ans == 'yes':
    print("The message is spam")
else:
    print("The message is not spam")
    
conn.close()

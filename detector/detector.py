import http.client
import json

class Gemini():
    def __init__(self, api_key):
        self.api_key = api_key
        self.conn = http.client.HTTPSConnection("generativelanguage.googleapis.com")
        self.headers = {
            "Content-Type": "application/json"
        }
        self.conn = http.client.HTTPSConnection("generativelanguage.googleapis.com")
        self.headers = {
            "Content-Type": "application/json"
        }
    def checkspam(self, msg):
        try:
            payload = json.dumps({
                "contents": [{
                    "parts": [{"text": f"{msg} tell me above message is froud/spam/harmful or not ONLY ANSWER IN YES OR NO. DO NOT GENERATE ANY OTHER TEXT."}]
                }]
            })
            
            self.conn.request("POST", f"/v1beta/models/gemini-1.5-flash:generateContent?key={self.api_key}", payload, self.headers)
            
            
            response = self.conn.getresponse()
            data = response.read()
            jsondata = json.loads(data.decode("utf-8"))
            if 'error' in jsondata:
                    raise Exception("Gemini API Key is Not Valid!")
            ans = jsondata['candidates'][0]['content']['parts'][0]['text']
            ans = ans.replace(' ','').replace('\n','').lower()
            if ans == 'yes':
                return True,"Spam Message Detected!"
            else:
                return False,"Not a Spam Message."
        except Exception as e:
            return False,str(e)
            
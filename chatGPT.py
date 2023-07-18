import requests
import json
import pandas

table = pandas.read_excel('graf.xlsx',engine='openpyxl')[:50]
dictionary = table.to_json()

question = {
    'question':'как дела?',
    'table':dictionary,
    'request':''
}

API_TOKEN = "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"
headers = {
    'Content-Type':'application/json',
    'Authorization': 'Bearer ' + API_TOKEN
}
def sent_message(message):
    data = {
        'model':'gpt-3.5-turbo-16k',
        'messages':[{'role':'system','content':'You are ChatGPT'},{'role':'user','content':message}]
        
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    information = json.loads(response.text)
    print(information['choices'][0]['message']['content'])
    
    

sent_message(json.dumps( question))    
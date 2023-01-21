import json

#opening json file
with open('message.json') as message_json:
  message = json.load(message_json)

print(message['text'])

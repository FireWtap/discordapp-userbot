import requests, json, sys, random

Discord = "https://discordapp.com/api/v6/"
token = open('token.txt').read()
def getUpdates(chatid):
  req = requests.get(Discord + "channels/" + str(chatid) + "/messages?limit=1", headers={"Authorization":"token"}).text
  return json.loads(req) 

def sendMessage(chatid, content, tts):
  return requests.post(Discord + "channels/" + str(chatid) + "/messages#", data={"tts":str(tts).lower(), "content":str(content), "nonce":str(chatid)}, headers={"Authorization":token}).text

def joinServer(invite):
  return requests.post(Discord + "invite/" + invite, headers={"Authorization":token})

def sendTypingAction(chatid):
  return requests.post(Discord + "channels/" + str(chatid) + "/typing", headers={"Authorization":token}).text

def sendFile(chatid, file, content):
  return requests.post(Discord + "channels/" + str(chatid) + "/messages", headers={"Authorization":token, "content":str(content)}, files={"file":open(file, 'rb')}).text

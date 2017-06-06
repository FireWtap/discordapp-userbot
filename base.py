import requests, json, sys, random

Discord = "https://discordapp.com/api/v6/"
token = open('token.txt').read()
def getUpdates(chatid):
  req = requests.get(Discord + "channels/" + str(chatid) + "/messages?limit=1", headers={"Authorization":token}).text
  return json.loads(req) 

def sendMessage(chatid, content, tts):
  return requests.post(Discord + "channels/" + str(chatid) + "/messages#", data={"tts":str(tts).lower(), "content":str(content), "nonce":str(chatid)}, headers={"Authorization":token}).text

def joinServer(invite):
  return requests.post(Discord + "invite/" + invite, headers={"Authorization":token})

def sendTypingAction(chatid):
  return requests.post(Discord + "channels/" + str(chatid) + "/typing", headers={"Authorization":token}).text

def sendFile(chatid, file, content):
  return requests.post(Discord + "channels/" + str(chatid) + "/messages", headers={"Authorization":token, "content":str(content)}, files={"file":open(file, 'rb')}).text

def setStatus(status):
  return requests.patch(Discord + "users/@me/settings", headers={"Authorization":token, "Content-Type":"application/json"}, data={"status":str(status)}).text

def pinMessage(chatid, messageid):
  return requests.post(Discord + "channels/" + str(chatid) + "/pins/" + str(messageid), headers={"Authorization":token}).text

def setName(newname, password, email):
  return requests.post(Discord + "users/@me/settings", headers={"username":newname, "password":password, "email":email, "Authorization":token}).text

def sendFriendRequest(username, discriminator):
  return requests.post(Discord + "users/@me/relationships", headers={"Authorization":token, "Content-Type":"application/json"}, data={"username":username, "discriminator":discriminator}).text

def editMessage(chatid, messageid, text):
  return requests.patch(Discord + "channels/" + str(chatid) + "/messages/" + str(messageid), headers={"Authorization":token}, data={"content":text}).text

def deleteMessage(chatid, messageid):
  return requests.delete(Discord + "channels/" + str(chatid) + "/messages/" + str(messageid), headers={"Authorization":token}).text

def kickUser(chatid, userid, reason):
  return requests.delete(Discord + "guilds/" + str(chatid) + "/members/" + str(userid) + "?reason=" + reason, headers={"Authorization":token}).text

def banUser(chatid, userid, rason):
  return requests.put(Discord + "guilds/" + str(chatid) + "/bans/" + str(userid) + "?delete-message-days=0&reason=" + reason, headers={"Authorization":token}).text

def createServer(icon, name, region):
  return requests.post(Discord + "guilds", headers={"Authorization":token}, data={"icon":icon, "name":name, "region":region}).text

def deleteServer(chatid):
  return requests.post(Discord + "guilds/" + str(chatid) + "/delete", headers={"Authorization":token}).text

def getInvite(chatid):
  return json.loads(requests.post(Discord + "channels/" + str(chatid) + "/invites", headers={"Authorization":token}, data={"max_age":"0", "max_uses":"0", "temporary":"false"}).text)["code"]

def getUserInfo(userid):
  return json.loads(requests.get(Discord + "users/" + str(userid) + "/profile", headers={"Authorization":token, "Content-Type":"application/json"}).text)

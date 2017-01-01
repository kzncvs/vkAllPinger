import vk_api
import time

id = 15 #VK chat ID (copy from url)

login, password = '', '' #VK login & password
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.authorization()
except vk_api.AuthorizationError as error_msg:
    print(error_msg)
vk = vk_session.get_api()

uslist = vk.messages.getChatUsers(chat_id = id)
mes = ' '
for i in range(len(uslist)):
    mes = mes + '@id' + str(uslist[i]) + ' ' + '(' + 'kek' + ')' + ' '

while True:
    now = vk.messages.get(out = 0, count = 10)
    for i in range(len(now['items'])):
        if (now['items'][i]['body'].find('@all', 0, len(now['items'][i]['body'])) != -1):
            vk.messages.send(peer_id = id + 2000000000, message = mes)
            vk.messages.deleteDialog(peer_id = id + 2000000000)
            break
    time.sleep(5)

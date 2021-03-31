from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import (PeerFloodError, UserNotMutualContactError ,
                                          UserPrivacyRestrictedError, UserChannelsTooMuchError,
                                          UserBotError, InputUserDeactivatedError)
from telethon.tl.functions.channels import InviteToChannelRequest
import time, os, sys, json
import random

wt = (
    '''
                                                  
    _    ____  ____  _____ ____  
   / \  |  _ \|  _ \| ____|  _ \ 
  / _ \ | | | | | | |  _| | |_) |
 / ___ \| |_| | |_| | |___|  _ < 
/_/   \_\____/|____/|_____|_| \_\
                                 


            version : 1.0 by Ankit Choudhary

    '''
)
COLORS = {
    "re": "\u001b[31;1m",
    "gr": "\u001b[32m",
    "ye": "\u001b[33;1m",
}
re = "\u001b[31;1m"
gr = "\u001b[32m"
ye = "\u001b[33;1m"
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text
# clearType = input('terminal or cmd. (t/c): ').lower()
clearType = "t"
if clearType == 't':
    clear = lambda:os.system('clear')
elif clearType == 'c':
    clear = lambda:os.system('clear')
else:
    print('Invalid input!!!')
    sys.exit()
if sys.version_info[0] < 3:
    telet = lambda :os.system('pip install -U telethon')
elif sys.version_info[0] >= 3:
    telet = lambda :os.system('pip3 install -U telethon')
telet()
clear()

if os.path.isfile('getmem_log.txt'):
    with open('getmem_log.txt', 'r') as r:
        data = r.readlines()
    api_id = data[0]
    api_hash = data[1]

else:
    api_id = input('Enter api_id: ')
    api_hash = input('Enter api_hash: ')
    with open('getmem_log.txt', 'w') as a:
        a.write(api_id + '\n' + api_hash)

client = TelegramClient('anon', api_id, api_hash)

async def main():
    # To Add Members.......
    async def getmem():
        clear()
        print(colorText(wt))
        print('')
        print('')
        
        print(ye+'[+] Choose your channel to Add members.')
        a=0
        for i in channel:
            print(gr+'['+str(a)+']', i.title)
            a += 1
        opt1 = int(input(ye+'Enter a number: '))
        my_participants = await client.get_participants(channel[opt1])
        target_group_entity = InputPeerChannel(channel[opt1].id, channel[opt1].access_hash)
        my_participants_id = []
        for my_participant in my_participants:
            my_participants_id.append(my_participant.id)
        with open('members.txt', 'r') as r:
            users = json.load(r)
        count = 1
        i = 0
        adds = 0
        exi = 0
        pri = 0
        bot = 0
        tomuch = 0
        dlt = 0
        mut = 0
        ero = 0
        flooderror = 0
        for user in users:
            clear()
            print(colorText(wt))
            print(r"==========================================")
            print(gr+"| Member Added                      : ", adds, "|")
            print(ye+"| User Exists. Skipped              : ", exi, "|")
            print(re+"| Privacy Enabled. Skipped          : ", pri, "|")
            print(re+"| This is Bot. Skipped              : ", bot, "|")
            print(re+"| User in too much channel. Skipped : ", tomuch, "|")
            print(re+"| Deleted Account. Skipped          : ", dlt, "|")
            print(re+"| Mutual No. Skipped                : ", mut, "|")
            print(re+"| Error                             : ", ero, "|")
            print(re+"| Peer Flood Error                  : ", flooderror, "|")
            print(r"==========================================")
            if count%51 == 0:
               # print(colorText(wt))
                print('')
                print('')
                print(ye+"50 members added")
                break
            elif count >= 300:
                await client.disconnect()
                break
            elif i >= 8:
                await client.disconnect()
                print(re+"Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                break
            if user['uid'] in my_participants_id:
               # print(gr+'User present. Skipping.')
                exi+=1
                clear()
                print(colorText(wt))
                print(r"==========================================")
                print(gr+"| Member Added                      : ", adds, "|")
                print(ye+"| User Exists. Skipped              : ", exi, "|")
                print(re+"| Privacy Enabled. Skipped          : ", pri, "|")
                print(re+"| This is Bot. Skipped              : ", bot, "|")
                print(re+"| User in too much channel. Skipped : ", tomuch, "|")
                print(re+"| Deleted Account. Skipped          : ", dlt, "|")
                print(re+"| Mutual No. Skipped                : ", mut, "|")
                print(re+"| Error                             : ", ero, "|")
                print(re+"| Peer Flood Error                  : ", flooderror, "|")
                print(r"==========================================")
                continue
            else:
                try:
                    user_to_add = InputPeerUser(user['uid'], user['access_hash'])
                    add = await client(InviteToChannelRequest(target_group_entity,[user_to_add]))
                   # print(gr+'Added ', str(user['uid']))
                    count+=1
                    i = 0
                    adds+=1
                   # time.sleep(random.randrange(1, 5))
                    
                except PeerFloodError:
                   # print(re+"Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
                    i += 1
                    flooderror+=1
                except UserPrivacyRestrictedError:
                   # print(re+"The user's privacy settings do not allow you to do this. Skipping.")
                   # print("Waiting for 5-15 Seconds...")
                    pri+=1
                   # time.sleep(random.randrange(5, 15))
                
                except UserBotError:
                   # print(re+"Can't add Bot. Skipping.")
                    bot+=1
                
                except InputUserDeactivatedError:
                   # print(re+"The specified user was deleted. Skipping.")
                    dlt+=1
                    
                except UserChannelsTooMuchError:
                   # print(re+"User in too much channel. Skipping.")
                    tomuch+=1
                except UserNotMutualContactError:
                   # print(re+'Mutual No. Skipped.')
                    mut+=1
                
                except Exception as e:
                   # print(re+"Error:", e)
                   # print("Trying to continue...")
                   # i += 1
                   # time.sleep(1)
                    ero+=1
                    continue
               # time.sleep(1)
                #end
    
    print(colorText(wt))
    chats = []
    channel = []
    result = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
    ))
    chats.extend(result.chats)
    for a in chats:
        try:
            if True:
                channel.append(a)
        except:
            continue

    a = 0
    print('')
    print('')
    print(ye+'Choose a group to scrape.')
    for i in channel:
        print(gr+'['+str(a)+']', i.title)
        a += 1
    op = input(ye+'Enter a number (or press ENTER to skip): ')
    if op == '':
        print(ye+'Ok. skipping...')
        await getmem()
        sys.exit()
    else: 
        pass
    opt = int(op)
    print('')
    print(ye+'[+] Fetching Members...')
    target_group = channel[opt]
    all_participants = []
    mem_details = []
    all_participants = await client.get_participants(target_group)
    for user in all_participants:
        try:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                firstname = user.first_name
            else:
                firstname = ""
            if user.last_name:
                lastname = user.last_name
            else:
                lastname = ""

            new_mem = {
                'uid': user.id,
                'username': username,
                'firstname': firstname,
                'lastname': lastname,
                'access_hash': user.access_hash
            }
            mem_details.append(new_mem)
        except ValueError:
            continue
    
    with open('members.txt', 'w') as w:
        json.dump(mem_details, w)
    print(ye+'Please wait.....')
    done = input(gr+'[+] Members scraped successfully. (Press enter to Add members)')
    await getmem()

    await client.disconnect()

with client:
    client.loop.run_until_complete(main())

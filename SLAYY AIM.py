import os #line:1
import json #line:2
import shutil #line:3
import zipfile #line:4
import subprocess #line:5
import urllib .request #line:6
try :#line:8
    newest_version ="https://raw.githubusercontent.com/kbdevs/ai-aimbot/main/current_version.txt"#line:9
    req =urllib .request .Request (newest_version ,headers ={'Cache-Control':'no-cache'})#line:10
    response =urllib .request .urlopen (req )#line:11
    remote_version =response .read ().decode ().strip ()#line:12
    file_paths =["./library.py","./yolo.cfg","./yolo.weights","./req.txt","./LICENSE","./README.md","./current_version.txt",]#line:22
    localv_path ="localv.json"#line:24
    if not os .path .exists (localv_path )or not os .path .exists (file_paths [1 ]):#line:26
        local_version ="0.0.0"#line:27
        data ={"version":remote_version ,"pip":False ,"python":False ,}#line:32
        with open (localv_path ,"w")as file :#line:33
            json .dump (data ,file )#line:34
    else :#line:35
        with open (localv_path ,"r")as file :#line:36
            data =json .load (file )#line:37
            local_version =data ["version"]#line:38
    if remote_version !=local_version :#line:40
        print ("Deleting old files...")#line:42
        for file_path in file_paths :#line:43
            if os .path .exists (file_path ):#line:44
                try :#line:45
                    os .remove (file_path )#line:46
                except Exception as e :#line:47
                    print (f"Error occurred while removing {file_path}: {e}")#line:48
        print ("Downloading SLAYY AIM...")#line:50
        url ="https://github.com/pro1234qwerr/SLAYY-AIM/archive/refs/heads/main.zip"#line:52
        response =urllib .request .urlopen (url )#line:53
        zip_content =response .read ()#line:54
        with open ("ai-aimbot.zip","wb")as file :#line:57
            file .write (zip_content )#line:58
        print ("Unzipping...")#line:60
        with zipfile .ZipFile ("ai-aimbot.zip","r")as zip_ref :#line:62
            zip_ref .extractall ("ai-aimbot")#line:63
        os .remove ("ai-aimbot.zip")#line:64
        print ("Moving files...")#line:66
        for root ,dirs ,files in os .walk ("ai-aimbot"):#line:68
            for file in files :#line:69
                shutil .move (os .path .join (root ,file ),os .path .join (".",file ))#line:70
        shutil .rmtree ("ai-aimbot")#line:73
        with open ("localv.json","w")as file :#line:75
            data ["version"]=remote_version #line:76
            json .dump (data ,file )#line:77
        with open ("localv.json","r")as file :#line:79
            pls =json .load (file )#line:80
            python =pls ["python"]#line:81
        if python is not True :#line:83
            print ("Downloading python...")#line:84
            url ="https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"#line:86
            filename ="pythoninstaller.exe"#line:87
            urllib .request .urlretrieve (url ,filename )#line:88
            print ("Installing python...")#line:90
            subprocess .run ([filename ,"/quiet","InstallAllUsers=1","PrependPath=1","Include_test=0"])#line:91
            with open ("localv.json","w")as file :#line:93
                pls ["python"]=True #line:94
                json .dump (pls ,file )#line:95
            os .remove (filename )#line:97
        with open ("localv.json","r")as file :#line:100
            data2 =json .load (file )#line:101
            pip =data ["pip"]#line:102
        if pip is not True :#line:104
            print ("Installing required modules...")#line:105
            subprocess .run (["pip","install","-r","req.txt"])#line:106
            subprocess .run (["pip3","install","-r","req.txt"])#line:107
            with open ("localv.json","w")as file :#line:108
                data2 ["pip"]=True #line:109
                json .dump (data2 ,file )#line:110
            os .remove (file_paths [3 ])#line:112
        for file_path in file_paths [4 :7 ]:#line:114
            if os .path .exists (file_path ):#line:115
                try :#line:116
                    os .remove (file_path )#line:117
                except Exception as e :#line:118
                    print (f"Error occurred while removing {file_path}: {e}")#line:119
    if os .path .exists ("library.py"):#line:121
        subprocess .run (["python","library.py"])#line:122
    else :#line:123
        print ("Failed to update, please delete localv.json and launch this again.")#line:124
        exit ()#line:125
except KeyboardInterrupt :#line:127
    exit ()#line:128

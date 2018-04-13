
import csv
import string
import os

def Play(video_id,total):    #输入了av号和总集数，默认无脑播放整个视频——B站官方有版权的暂时不行
    total=total+1
    status=0
    for i in range(1,total):
        if status > 0 :
            print("ERROR!Quiting by mpv.")
            break
        url='https://www.bilibili.com/video/'+str(video_id)+'/index_'+str(i)+'.html'
        cmd='mpv -fs '+url  #不想默认全屏放映的话去掉 -fs 即可
        status=os.system(cmd)

def Menu(video_info):             #生成选择界面。需要配合data.csv文件，每一行共三个数据，分别时视频名称、av号、总集数。记住：不许有空行！
    print("您的数据库中有以下视频，请选择对应的序号以播放：")
    i=0
    for data in video_info :
        i=i+1
        dis="["+str(i)+"]"+data[0]
        print(dis)

def Select(video_info):  #决定你的选择
    num=input("您的选择是:")
    num=int(num)
    i=0
    for data in video_info :
        i=i+1
        if num == i :
            Play(data[1],int(data[2]))
            break
        else:
            continue
        break

with open("data.csv","r",encoding="utf-8") as csvfile: #生成选择界面
    load_data=csv.reader(csvfile)
    Menu(load_data)

with open("data.csv","r",encoding="utf-8") as csvfile:   #开始选择，请开始你的表演
    cmd=csv.reader(csvfile)
    Select(cmd)
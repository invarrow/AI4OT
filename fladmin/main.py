import pygame
pygame.init()
pygame.mixer.init()
import time,csv
import os
osCommandString = "notepad.exe log.txt"


from pyModbusTCP.client import ModbusClient
import csv
from time import sleep
import numpy as np
import joblib
import pandas as pd

f = open('dataset1.csv','r')
csvreader = csv.reader(f)
wdth,height = 1500,800

FPS = 10

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (50, 255, 50)
BLUE = (0, 0, 255)
logimg = pygame.image.load("fladmin\log.png")
logimg = pygame.transform.scale(logimg,(50,50))

cautionimg = pygame.image.load("fladmin\caution.png")
cautionimg = pygame.transform.scale(cautionimg,(50,50))

dis = pygame.display.set_mode((wdth, height))
pygame.display.set_caption('a tiled One')
clock = pygame.time.Clock()

font = pygame.font.SysFont("Ariel", 50)
def Convert(string):
    li = list(string.split(" "))
    return li


def blit_text(msg, color, x, y):
    text = font.render(msg, True, color)
    dis.blit(text, (x,y))

running = True
con_h,con_w = 238,wdth-250
con_x= 250
con_y = [height-235]
for i in range(4):
    con_y.append(con_y[i]+50)
print(con_y)

dt = [4,3,46,2.68965569,12356,0]
dts = ['address','function','length','system mode','control scheme','pump']

model = joblib.load('bruno1.joblib')
client = ModbusClient('localhost',port = 502)

data = pd.read_csv('dataset1.csv')

df = pd.DataFrame(data)
print(df)

df.columns = ['address','function','length','setpoint','gain','reset rate','deadband','cycle time', 'rate', 'system mode', 'control scheme','pump','solenoid','pressure measurement','crc rate','command response','time','binary result','categorized result','specific result']
df = df.replace('?',-1)
df = df.drop(columns = ['setpoint','gain','reset rate','deadband','cycle time','rate','system mode','time','binary result','categorized result','specific result'])

for row in range(0,df.size):
    #print(df.iloc[row])

    r = pd.DataFrame([df.iloc[row]])
    print(r)
    pred = model.predict(r)
    print(pred)
    if pred==[0]:
        
        try:
            rt =client.write_single_register(row,int(df.iloc[row]))
            
            # print(rt)
        except:
            pass
    else:
        break


alert = None
log = open("log.txt","w")
index = 0
while running:
    if index>=df.size:
        running = False

    r = pd.DataFrame([df.iloc[index]])
    print(r)
    pred = model.predict(r)
    print(pred)
    if pred==[0]:
        
        try:
            rt =client.write_single_register(index,df.iloc[index])
            
            # print(rt)
        except:
            pass
    else:
        liss = ["Normal","NRMI","CMRI","MSCI","MPCI","MFCI","DOS","Recon"]
        print(f"{liss[int(pred)]} is the type of attack, Use this for diagnosis")
        # alert = f"{liss[int(pred)]} is the type of attack, Use this for diagnosis"
        # blit_text(f"{liss[int(pred)]} is the type of attack, Use this for diagnosis",BLACK,250,10)

    for line in csvreader:
        log.write(str(line)+"\n")
        break
    
    dis.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ax <= mouse[0] <= ax+awidth and ay <= mouse[1] <= ay+aht and click:
                    if pygame.mouse.get_pressed()[0]:    
                        data = Convert(input('Enter data to simulate an attack: '))
                        count = 0
                        for i in data:
                            i = float(i)
                            # count = float(count)
                            if i!=float(dt[count]) and count<6:
                                print(f"'{dts[count]}' is suspected to have anomaly with value '{i}'")
                                alert = f"'{dts[count]}' is suspected to have anomaly with value '{i}'"
                            
                            count+=1
            if lx <= mouse[0] <= lx+lwidth and ly <= mouse[1] <= ly+lht and click:
                if pygame.mouse.get_pressed()[0]:
                    os.system(osCommandString)
                        
    
    
    
    pygame.draw.rect(dis,BLACK,(0,0,250,height),2)
    pygame.draw.rect(dis,BLACK,(250,0,wdth-248,height-240),2)
    pygame.draw.rect(dis,BLACK,(250,height-240,con_w,con_h),2)

    for y in con_y:
        blit_text(str(line),(0,0,0),con_x,y)

        
    mouse = pygame.mouse.get_pos()

    awidth,aht = 200,80
    ax,ay = 20,120
    color_light = (180,0,0)
    color_dark = (245,0,0)

    lwidth,lht = 200,80
    lx,ly = 20,20
    lcolor_light = (0, 102, 204)
    lcolor_dark = (128, 191, 255)


    click = pygame.mouse.get_pressed()
    pygame.draw.rect(dis,color_light,[ax,ay,awidth,aht])
    pygame.draw.rect(dis,lcolor_light,[lx,ly,lwidth,lht])
    

    if ax <= mouse[0] <= ax+awidth and ay <= mouse[1] <= ay+aht:
        pygame.draw.rect(dis,color_light,[ax,ay,awidth,aht])
            
    else:
        pygame.draw.rect(dis,color_dark,[ax,ay,awidth,aht]) 

    if lx <= mouse[0] <= lx+lwidth and ly <= mouse[1] <= ly+lht:
        pygame.draw.rect(dis,lcolor_light,[lx,ly,lwidth,lht])
            
    else:
        pygame.draw.rect(dis,lcolor_dark,[lx,ly,lwidth,lht]) 
    
    blit_text("Attack",BLACK,ax+75,ay+25) 
    blit_text("LOGS!",BLACK,lx+75,ly+25)  
     
    dis.blit(logimg,(lx+10,ly+20))
    dis.blit(cautionimg,(ax+10,ay+17))
    if alert!=None:
        blit_text(alert,RED,ax+255,ay+35)
    else:
        print(alert)

    pygame.display.update()
    clock.tick(FPS)
    index+=1
    # time.sleep()
    
pygame.quit()
            
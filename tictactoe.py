import pygame,sys,time
from pygame.locals import *
import random as rd
import itertools as it
import functools


pygame.init()
tie=0
win=0
lost=0
swidth=1019
sheight=869
screen=pygame.display.set_mode((swidth,sheight),pygame.RESIZABLE)
pygame.display.set_caption('THIS IS TIC TAC TOE')
gameloop=True
clock=pygame.time.Clock()
xrange=[0]
yrange=[0]
image0=pygame.image.load('0.jpg').convert_alpha()
imagex=pygame.image.load('x.jpg').convert_alpha()
imager=pygame.image.load('re.png').convert_alpha()
imagec=pygame.image.load('close.png').convert_alpha()
text_size=32
totallist=[1,2,3,4,5,6,7,8,9]
products=[6,28,45,80,105,162,120,504]
perm=list(it.combinations(totallist,3))
sumlist=[sum(x) for x in perm]
prolist=[]
checklist=[]
win_combo=[(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
for x in perm:
    tmp=functools.reduce(lambda x,y:x*y ,x)
    prolist.append(tmp)
'''for i,j,k in zip(perm,sumlist,prolist):
    if i in win_combo:
        print(i,j,k)
print('thank')
for i,j,k in zip(perm,sumlist,prolist):
    if k in products:
        print(i,j,k)
        checklist.append([i,j,k])'''
 


green    =  (0,255,0,20)
white    =  (255,255,255)
aqua     =  (0, 255, 255)
black    =  (0, 0, 0)
blue     =  (0, 0, 255)
fuchsia  =  (255, 0, 255)
gray     =  (128, 128, 128)
lgray    =  (150,150,150,150)
greeny   =  (0, 128, 0)
lime     =  (0, 255, 0)
maroon   =  (128, 0, 0)
navyblue =  (0, 0, 128)
olive    =  (128, 128, 0)
purple   =  (128, 0, 128)
red      =  (255, 0, 0)
silver   =  (192, 192, 192)
teal     =  (0, 128, 128)
white    =  (255, 255, 255)
yellow   =  (255, 255, 0)
colors   =  [green,aqua,blue,fuchsia,greeny,
             lime,maroon,navyblue,olive,purple,red,silver,teal,yellow]

color1=rd.choice(colors)
color2=rd.choice(colors)
color3=rd.choice(colors)
color4=rd.choice(colors)

dicty={}
valcount=0
for i in range(3):
    for j in range(3):
        valcount+=1
        dicty[valcount]=[j,i]



class score():
    def __init__ (self,swidth,sheight,font_size):
        brd=board(swidth,sheight)
        self.x1=110+brd.bwidth
        self.y1=font_size+60
        scorewidth=(swidth//5)
    def drawtext(self,screen,fontval,val,font):
        self.y1+=val
        new_surf=font.render(fontval,False,(white))
        screen.blit(new_surf,(self.x1,self.y1))
        
    

class board():
    def __init__(self,swidth,sheight):
        self.bx=50
        self.by=50
        self.bwidth=swidth-100-(swidth//5)
        self.bheight=sheight-100
    def drawboard(self,screen):
        board=pygame.draw.rect(screen,(255,255,255),(self.bx,self.by,self.bwidth,self.bheight))


block=0
class lining():
    global block
    def __init__(self,w,h):
        self.lwid=w
        self.lhit=h
        self.px=0
        self.py=0
    def verdrawline(self,px,py,screen,color):
        global block
        self.px=px
        self.py=py
        verline=pygame.draw.rect(screen,color,(self.px,self.py,self.lwid,self.lhit))
        block=verline

line_max_height=0
line_min_height=1000
def drawingvlines(bx,by,bwidth,bheight,screen,vcount,vlh):
    global line_max_height,black,swidth,line_min_height,colors,color1,color2,color3,color4,xrange,yrange
    if vcount%90==0:
        color1=rd.choice(colors)
        color2=rd.choice(colors)
        color3=rd.choice(colors)
        color4=rd.choice(colors)
    lin=lining(10,vlh)
    tmp=(bwidth-40)//3
    bwidth=bwidth+bx-10
    bheight=bheight+by-10
    a=bx
    b=bx+tmp+10
    c=b+tmp+10
    d=bwidth
    by+=vcount
    lin.verdrawline(a,by,screen,color1)
    lin.verdrawline(b,by,screen,color2)
    lin.verdrawline(c,by,screen,color3)
    lin.verdrawline(d,by,screen,color4)
    line_max_height=block.bottom
    line_min_height=by
    xrange.extend([a+10,b+10,c+10,d+10])

hline_max_width=0
hline_min_width=1000
def drawinghlines(bx,by,bwidth,bheight,screen,hcount,hlw):
    global hline_max_width,black,swidth,hline_min_width,colors,color1,color2,color3,color4,xrange,yrange
    lin=lining(hlw,10)
    tmp=(bheight-40)//3
    bwidth=bwidth+bx-10
    bheight=bheight+by-10
    a=by
    b=by+tmp+10
    c=b+tmp+10
    d=bheight
    bx+=hcount
    lin.verdrawline(bx,a,screen,color2)
    lin.verdrawline(bx,b,screen,color4)
    lin.verdrawline(bx,c,screen,color1)
    lin.verdrawline(bx,d,screen,color3)
    hline_max_width=block.right
    hline_min_width=bx
    yrange.extend([a+10,b+10,c+10,d+10])

printw=[]
printh=[]
donelist=[]
totallist=[1,2,3,4,5,6,7,8,9]
notdonelist=[]
antiprint=[]
isdone=False
def drawgray(mousex,mousey,col):
    global screen,xrange,yrange,image0,imagex,printw,printh,donelist,dicty,notdonelist,antiprint,isdone,clickflag
    for i in range(3):
        for j in range(3):
            checkxrange=[xrange[i],xrange[i+1]]
            checkyrange=[yrange[j],yrange[j+1]]
            if checkxrange[0]<=mousex and mousex<checkxrange[1] and checkyrange[0]<=mousey and mousey<checkyrange[1]:
                wid=checkxrange[1]-checkxrange[0]-10
                hit=checkyrange[1]-checkyrange[0]-10
                if col==True:
                    pygame.draw.rect(screen,lgray,(checkxrange[0],checkyrange[0],wid,hit))
                    return False
                else:
                    for key,[val1,val2] in dicty.items():
                        if [i,j]==[val1,val2] and key not in antiprint and key not in donelist:
                            donelist.append(key)
                            printw.append(i)
                            printh.append(j)
                            return True




someonewinning=0
def winningcheck(length,chosen):
    global win_combo,donelist,antiprint,someonewinning
    flag=1
    cheat=[1,3,7,9]
    put=[2,4,6,8]
    rd.shuffle(put)
    rd.shuffle(cheat)
    dinni={7:[2,6],9:[4,2],1:[8,6],3:[4,8]}
    tinni={7:[2,6],9:[4,2],1:[8,6],3:[4,8]}
    if len(donelist)==2:
        if(donelist[0] in cheat and donelist[1] in put) or (donelist[1] in cheat and donelist[0] in put):
            
            chosen=rd.choice(cheat)
            while chosen in antiprint or chosen in donelist:
                chosen=rd.choice(cheat)
            someonewinning=0
            return chosen
    if len(donelist)==2 and (5 in donelist and donelist[1] in cheat):
        chosen=rd.choice(cheat)
        while chosen in antiprint or chosen in donelist:
            chosen=rd.choice(cheat)
        someonewinning=0
        return chosen
    if len(antiprint)==1 and len(donelist)==2:
        for vals in win_combo:
            if donelist[0] in vals and donelist[1] in vals:
                tmp=[x for x in vals if x!=donelist[0] if x!=donelist[1]]
                chosen=tmp[0]
                if chosen not in antiprint and chosen not in donelist:
                    someonewinning=0
                    return chosen
        if donelist[0] in cheat or donelist[1] in cheat:
            chosen=rd.choice(put)
            if chosen not in antiprint and chosen not in donelist:
                someonewinning=0
                return chosen
        if donelist[0] in put and donelist[1] in put:
            chosen=rd.choice(cheat)
            for key,vals in dinni.items():
                tmp=chosen
                if donelist[0] in vals and donelist[1] in vals and chosen==key:
                    chosen=rd.choice(cheat)
                    while(chosen==tmp):
                        chosen=rd.choice(cheat)
            if chosen not in antiprint and chosen not in donelist:
                someonewinning=0
                return chosen
    permdone=list(it.combinations(donelist,2))
    permanti=list(it.combinations(antiprint,2))
    if length>1:
        for vals in win_combo:
            for v in permanti:
                if v[0] in vals and v[1] in vals:
                    tmp=[x for x in vals if x!=v[0] if x!=v[1]]
                    chosen=tmp[0]
                    flag=0
                    if chosen not in antiprint and chosen not in donelist:
                        if flag==0:
                            someonewinning=0
                            return chosen
                    if chosen in antiprint or chosen in donelist:
                        chosen=rd.choice(notdonelist)
                        flag=1
    if flag==1:
        for vals in win_combo:
            for v in permdone:
                if v[0] in vals and v[1] in vals:
                    tmp=[x for x in vals if x!=v[0] if x!=v[1]]
                    chosen=tmp[0]
                    flag=0
                    if chosen not in antiprint and chosen not in donelist:
                        if flag==0:
                            someonewinning=0
                            return chosen
                    if chosen in antiprint or chosen in donelist:
                        chosen=rd.choice(notdonelist)
                        flag=1
    someonewinnig=1
    return chosen

def youwon(listy):
    permdone=list(it.combinations(listy,3))
    for vals in win_combo:
        for v in permdone:
            if v[0] in vals and v[1] in vals and v[2] in vals:
                time.sleep(2)
                return True
    return False
                    
                    
                    
            
            
    



center=0                          
vflag=0    
vcount=0
hflag=0
hcount=0
vlh=0
hlw=0
turn=0
gameover=False
clickhua1=False
clickhua2=False
cheatingflag=0
while gameloop:
    if not gameover:
        font = pygame.font.Font('freesansbold.ttf', text_size)
        notdonelist=[x for x in totallist if x not in donelist if x not in antiprint]
        xrange.clear()
        yrange.clear()
        if vflag==0:
            vcount+=5
        else:
            vcount-=5
        if hflag==0:
            hcount+=5
        else:
            hcount-=5
        brd=board(swidth,sheight)
        scr=score(swidth,sheight,text_size)
        reflag=0
        screen.fill(black)
        clock.tick(30)
        if line_max_height>brd.bheight+45:
            vflag=1
        if line_min_height<56:
            vflag=0
        if hline_max_width>brd.bwidth+45:
            hflag=1
        if hline_min_width<56:
            hflag=0
        brd.drawboard(screen)
        old_screen=screen
        vlh=0.75*brd.bheight
        hlw=0.75*brd.bwidth
        drawingvlines(brd.bx,brd.by,brd.bwidth,brd.bheight,screen,vcount,vlh)
        drawinghlines(brd.bx,brd.by,brd.bwidth,brd.bheight,screen,hcount,hlw)
        screen.blit(old_screen,(0,0))
        mousex,mousey=pygame.mouse.get_pos()
        ret=drawgray(mousex,mousey,True)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameloop=False
                print('WINS ',win)
                print('LOST ',lost)
                print('TIES ',tie)
            if event.type==pygame.VIDEORESIZE:
                old_screen=screen
                swidth=event.w
                sheight=event.h
                screen=pygame.display.set_mode((swidth,sheight),pygame.RESIZABLE)
                screen.blit(old_screen,(0,0))
                reflag=1
                pygame.display.update()
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousex,mousey=pygame.mouse.get_pos()
                tre=drawgray(mousex,mousey,False)
                if tre==True:
                    turn=1  
        for c,d in zip(printw,printh):
            tmpx=xrange[c+1]-xrange[c]-10
            tmpy=yrange[d+1]-yrange[d]-10
            image=pygame.transform.scale(imagex,(tmpx,tmpy))
            screen.blit(image,(xrange[c],yrange[d]))
        if turn==1 and len(notdonelist)!=0:
            if 5 not in donelist and 5 not in antiprint:
                chosen=5
                cheatingflag=1
                center=1
            else:
                chosen=rd.choice(notdonelist)
            cheat=[1,3,7,9]
            length=len(antiprint)
            chosen=winningcheck(length,chosen)
            if cheatingflag==1 and len(antiprint)==1 and donelist[0] in cheat and donelist[1] in cheat and someonewinning==1:
                alist=[2,4,6,8]
                rd.shuffle(alist)
                for i in alist:
                    if i not in antiprint and i not in donelist:
                        chosen=i
                        cheatingflag=0
            if center!=1 and len(antiprint)==0:
                center=0
                chosen=rd.choice(cheat)
            if chosen not in antiprint and chosen not in donelist:
                antiprint.append(chosen)
                turn=0
        for i in antiprint:
            c1,d1=dicty[i]
            tmpx1=xrange[c1+1]-xrange[c1]-10
            tmpy1=yrange[d1+1]-yrange[d1]-10
            image=pygame.transform.scale(image0,(tmpx1,tmpy1))
            screen.blit(image,(xrange[c1],yrange[d1]))
        winner='WINS '+str(win)
        loser='LOST '+str(lost)
        tieer='TIES '+str(tie)
        scr.drawtext(screen,winner,0,font)
        scr.drawtext(screen,loser,60,font)
        scr.drawtext(screen,tieer,60,font)
        if len(notdonelist)==0:
            time.sleep(2)
            gameover=True
            tie+=1
        if reflag!=1:
            pygame.display.update()
        if len(donelist)>=3 and gameover==False:
            gameover=youwon(donelist)
            if gameover==True:
                win+=1
        if len(antiprint)>=3 and gameover==False:
            gameover=youwon(antiprint)
            if gameover==True:
                lost+=1
            
    else:
        center=0
        font = pygame.font.Font('freesansbold.ttf', text_size)
        scr=score(swidth,sheight,text_size)
        reflag=0
        brd=board(swidth,sheight)
        screen.fill(black)
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameloop=False
            if event.type==pygame.VIDEORESIZE:
                old_screen=screen
                swidth=event.w
                sheight=event.h
                screen=pygame.display.set_mode((swidth,sheight),pygame.RESIZABLE)
                screen.blit(old_screen,(0,0))
                reflag=1
                pygame.display.update()
        h=brd.bheight//2
        w=brd.bwidth
        text_size=w//15
        image=pygame.transform.scale(imager,(w,h))
        rectangle=image.get_rect()
        screen.blit(image,(brd.bx,brd.by))
        x1=rectangle.centerx-(text_size//2)
        y1=rectangle.centery-(h//2)
        new_surf=font.render("RESTART",False,(white))
        screen.blit(new_surf,(x1,y1))
        new_image=pygame.transform.scale(imagec,(w,h))
        screen.blit(new_image,(brd.bx,brd.by+h))
        end_surf=font.render("STOP",False,(red))
        y1=rectangle.centery+(h//1.5)
        screen.blit(end_surf,(x1,y1))
        rex=brd.bx
        rey=brd.by
        stopx=brd.bx
        stopy=brd.by+h
        winner='WINS '+str(win)
        loser='LOST '+str(lost)
        tieer='TIES '+str(tie)
        scr.drawtext(screen,winner,0,font)
        scr.drawtext(screen,loser,60,font)
        scr.drawtext(screen,tieer,60,font)
        '''print('rex',rex)
        print(rex+w)
        print(rey)
        print('reyh',rey+h)
        time.sleep(2)'''
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousex,mousey=pygame.mouse.get_pos()
                '''print('mousex',mousex)
                print('mousey',mousey)'''
                if rex<=mousex and mousex<rex+w and rey<=mousey and mousey<rey+h:
                    gameover=False
                    vflag=0    
                    vcount=0
                    hflag=0
                    hcount=0
                    vlh=0
                    hlw=0
                    turn=0
                    printw=[]
                    printh=[]
                    donelist=[]
                    totallist=[1,2,3,4,5,6,7,8,9]
                    notdonelist=[]
                    antiprint=[]
                    isdone=False
                    clickhua1=False
                    clickhua2=False
                    someonewinning=0
                if stopx<=mousex and mousex<stopx+w and stopy<=mousey and mousey<stopy+h:
                    gameloop=False
                    print('WINS ',win)
                    print('LOST ',lost)
                    print('TIES ',tie)
        if reflag!=1:
            pygame.display.update()
pygame.quit()

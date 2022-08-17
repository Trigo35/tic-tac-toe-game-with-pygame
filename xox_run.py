import pygame
white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
blue=(0,0,250)
def draw_x(pos):
    space=50
    pygame.draw.line(screen,red,(pos[0]-space,pos[1]+space),(pos[0]+space,pos[1]-space),3)
    pygame.draw.line(screen,red,(pos[0]-space,pos[1]-space),(pos[0]+space,pos[1]+space),3)
def draw_o(pos):
    r=60
    pygame.draw.circle(screen,red,(pos[0],pos[1]),r,width=2)
def drawxo(kar,pos):
    if kar==1:
        draw_x(pos)
    elif kar==2:
        draw_o(pos)

def control3(xotup):
    global done
    xwin=[1,1,1]
    owin=[2,2,2]
    testlist=[]
    #for horizontal wins
    for i in xotup:
        testlist=i
        if testlist==xwin:
            print("x won")
            x=xotup.index(i)
            pygame.draw.line(screen,blue,(50,((x*200)+100)),(550,((x*200)+100)),5)
        elif testlist==owin:
            print("o won")
            x = xotup.index(i)
            pygame.draw.line(screen, blue, (50, ((x * 200) + 100)), (550, ((x * 200) + 100)), 5)
        #print ('Testlist:',testlist)
    #for vertical wins
    testlist=[]
    for i in range(3):
        testlist=[]
        for j in range(3):
            testlist.append(xotup[j][i])
        print('Testlist:',testlist)
        if testlist==xwin:
            print("x won")
            x = i
            pygame.draw.line(screen, blue, (((x * 200) + 100), 50), (((x * 200) + 100), 550), 5)

        elif testlist==owin:
            print("o won")
            x = i
            pygame.draw.line(screen, blue, (((x * 200) + 100), 50), (((x * 200) + 100), 550), 5)

    #for diagonal wins
    testlist=[]
    for j in range(3):
        testlist.append(xotup[j][j])
    if testlist == xwin:
        print("x won")
        pygame.draw.line(screen, blue, (50, 50), (550, 550), 5)
    elif testlist == owin:
        print("o won")
        pygame.draw.line(screen, blue, (50, 50), (550, 550), 5)
    testlist=[]
    for i in range(1,4):
        j=-i
        i=i-1
        testlist.append(xotup[j][i])
    if testlist == xwin:
        print("x won")
        pygame.draw.line(screen, blue, (550, 50), (50, 550), 5)
    elif testlist == owin:
        print("o won")
        pygame.draw.line(screen, blue, (550, 50), (50, 550), 5)

def addxo(xotup,kar,pos):
    global error
    x=pos[0] -1
    y=pos[1] - 1
    if xotup[y][x]==0:
        xotup[y][x] = kar
    else:
        print('error')
        error=True
    print(xotup)
    return xotup

pygame.init()
screen_size=(600,600)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption("XOX Game")
screen.fill(white)
pygame.draw.line(screen,black,(200,0),(200,600),2)
pygame.draw.line(screen,black,(400,0),(400,600),2)
pygame.draw.line(screen,black,(0,200),(600,200),2)
pygame.draw.line(screen,black,(0,400),(600,400),2)

pygame.display.flip()
done=False
error=False
clock = pygame.time.Clock()
xotup=[[0,0,0],[0,0,0],[0,0,0]]
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.KEYDOWN:
            m_pos=pygame.mouse.get_pos()
            print(m_pos)
            kar=0
            if event.key== pygame.K_x:
                kar=1
            elif event.key == pygame.K_o:
                kar=2
            if m_pos[0]<200 and m_pos[1]<200:
                xotup=addxo(xotup, kar, (1, 1))
                if not error:
                    drawxo(kar,[100,100])
            elif 200<m_pos[0]<400  and m_pos[1]<200:
                xotup=addxo(xotup, kar, (2, 1))
                if not error:
                    drawxo(kar,[300,100])
            elif 400<m_pos[0]<600  and m_pos[1]<200:
                xotup = addxo(xotup, kar, (3, 1))
                if not error:
                    drawxo(kar,[500,100])
            elif m_pos[0]<200 and 200<m_pos[1]<400:
                xotup = addxo(xotup, kar, (1, 2))
                if not error:
                    drawxo(kar,[100,300])
            elif 200<m_pos[0]<400  and 200<m_pos[1]<400:
                xotup = addxo(xotup, kar, (2, 2))
                if not error:
                    drawxo(kar,[300,300])
            elif 400<m_pos[0]<600  and 200<m_pos[1]<400:
                xotup = addxo(xotup, kar, (3, 2))
                if not error:
                    drawxo(kar,[500,300])
            elif m_pos[0]<200 and 400<m_pos[1]<600:
                xotup=addxo(xotup, kar, (1, 3))
                if not error:
                    drawxo(kar,[100,500])
            elif 200<m_pos[0]<400  and 400<m_pos[1]<600:
                xotup = addxo(xotup, kar, (2, 3))
                if not error:
                    drawxo(kar,[300,500])
            elif 400<m_pos[0]<600  and 400<m_pos[1]<600:
                xotup = addxo(xotup, kar, (3, 3))
                if not error:
                    drawxo(kar,[500,500])
            control3(xotup)
            pygame.display.flip()
            error=False
pygame.quit()



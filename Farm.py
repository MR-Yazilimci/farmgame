import pygame,sys
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption("Farm")
monitor_size = [1024,512]
surf = pygame.Surface((512,256))
screen = pygame.display.set_mode(monitor_size,pygame.RESIZABLE,32,0,1)
#pygame.display.set_icon(minilogo)
screen_size = [screen.get_width(),screen.get_height()]

font = pygame.font.SysFont("Arial",16)
afont = pygame.font.SysFont("Arial",32)
pfont = pygame.font.SysFont("Consolas",16)
sltfps = ""

gamemap = pygame.image.load("sprites/map.png")

gamest = "menu"

pb1  = pygame.image.load("sprites/P1B.png")
pb2  = pygame.image.load("sprites/P2B.png")
pb1 = pygame.transform.scale2x(pb1)
pb2 = pygame.transform.scale2x(pb2)

ayar1 = pygame.image.load("sprites/ayar.png")
ayar2 = pygame.image.load("sprites/ayar2.png")
ayar1 = pygame.transform.scale2x(ayar1)
ayar2 = pygame.transform.scale2x(ayar2)

pbrect= pb1.get_rect()
ayarrct = ayar1.get_rect()
mrect = pygame.Rect(1,1,1,1)
pbrect.x,pbrect.y = (screen_size[0]//2)-(pb1.get_width()//2),(screen_size[1]//2)-(pb1.get_height()//2)
ayarrct.x,ayarrct.y = (screen_size[0]//2)-(pb1.get_width()//2)+200,(screen_size[1]//2)-(pb1.get_height()//2)

px,py= [0,0]

m = 1

grnt = pygame.Surface((512,256))

capa = pygame.image.load("sprites/capa.png")
caparect = capa.get_rect()
caparect.x,caparect.y = 0 , 128-16

capali = pygame.image.load("sprites/capali.png")
capalirect = capali.get_rect()
capalirect.x,capalirect.y = 0 ,0

patatoE = pygame.image.load("sprites/patatoE.png")
patatos = pygame.image.load("sprites/patatos.png")
domatoE = pygame.image.load("sprites/domatoE.png")
domatos = pygame.image.load("sprites/domatos.png")
domatosrect = domatos.get_rect()
domatorect = domatoE.get_rect()
patatosrect = patatos.get_rect()
patatorect = patatoE.get_rect()
domatosrect.x,domatosrect.y = 256-48 , 0
domatorect.x,domatorect.y = 256-16 , 128-16
patatosrect.x,patatosrect.y = 256-48 , 16
patatorect.x,patatorect.y = 256-16-16 , 128-16

patato_1 = pygame.image.load("sprites/patato_1.png")
patato_2 = pygame.image.load("sprites/patato_2.png")
patato_3 = pygame.image.load("sprites/patato_3.png")
patato_4 = pygame.image.load("sprites/patato_4.png")
patato_5 = pygame.image.load("sprites/patato_5.png")

patatolist = [patato_1,patato_2,patato_3,patato_4,patato_5]

domato_1 = pygame.image.load("sprites/domato_1.png")
domato_2 = pygame.image.load("sprites/domato_2.png")
domato_3 = pygame.image.load("sprites/domato_3.png")
domato_4 = pygame.image.load("sprites/domato_4.png")
domato_5 = pygame.image.load("sprites/domato_5.png")

domatolist = [domato_1,domato_2,domato_3,domato_4,domato_5]

rmx,rmy =0,0
rmrct= pygame.Rect(1,1,1,1)

pak = 0
ca = 0
a = 0

#msp = pygame.Surface((16,16),pygame.SRCALPHA)
#msp.blit(capali,(0,0))
#msp.set_alpha(96)
#screen.blit(msp,(0,0))
mspc = pygame.Surface((16,16),pygame.SRCALPHA)

maplist = [
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]]

max ,may = (rmx//16)-4 ,(rmy//16)-1
alp = 64
alpi = 0
atimer = pygame.time.get_ticks()
pk = 0
dak = 0
dk = 0
patato_1rect = pygame.Rect(0,0,16,16)
domato_1rect = pygame.Rect(0,0,16,16)

frm = 0

idomato = 0
ipatato = 0

while True:
    key = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    screen.fill((0,0,0))
    mx,my = pygame.mouse.get_pos()
    rmrct.x,rmrct.y = rmx,rmy
    mrect.x,mrect.y = mx,my
    max ,may = (rmx//16)-4 ,((rmy-py)//16)-1
    max,may = int(max),int(may)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == VIDEORESIZE:
            screen_size = [screen.get_width(),screen.get_height()]
            pbrect.x,pbrect.y = (screen_size[0]//2)-(pb1.get_width()//2),(screen_size[1]//2)-(pb1.get_height()//2)
            ayarrct.x,ayarrct.y = (screen_size[0]//2)-(pb1.get_width()//2)+200,(screen_size[1]//2)-(pb1.get_height()//2)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if gamest == "menu":
                    if mrect.colliderect(pbrect):
                        gamest = "game"
                    if mrect.colliderect(ayarrct):
                        gamest = "ayar"
                elif gamest == "ayar":
                    if mrect.colliderect(pygame.Rect(24,72,16,16)):
                        m+=1
                        if m > 2:
                            m = 1
                elif gamest == "game":
                    if rmrct.colliderect(domatorect):
                        pak = 0
                        dak = 1
                        py = 0
                        ca = 0
                    if rmrct.colliderect(patatorect):
                        pak = 1
                        dak = 0
                        py = 0
                        ca = 0
                    if rmrct.colliderect(caparect):
                        frm = 1
                        pak = 0
                        dak = 0
                        ca = 1
                        py = 0
                    if ca == 1:
                        if a == 1:
                            if rmx > 64 and rmy-py > 16 and rmy-py < 240 and rmx < 240 :
                                maplist[may][max][0] = 1
                    if pak == 1:
                        if pk == 1:
                            maplist[may][max][1] = "patato"
                            maplist[may][max][2] = 0
                            maplist[may][max][3] = pygame.time.get_ticks()
                    if dak == 1:
                        if dk == 1:
                            maplist[may][max][1] = "domato"
                            maplist[may][max][2] = 0
                            maplist[may][max][3] = pygame.time.get_ticks()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if gamest == "ayar":
                    gamest = "game"
                elif gamest == "game":
                    gamest = "ayar"
    if gamest == "game":
        if frm == 0:
            if key[K_a]:
                px-=1
            if key[K_d]:
                px+=1
        if key[K_w]:
            if ca == 1:
                py += 16
            else:
                py+=1
        if key[K_s]:
            if ca == 1:
                py -= 16
            else:
                py-=1
        if py > 0:
            py = 0
        if px < 0:
            px = 0
        if px > 256:
            px = 256
        if py < -128:
            py = -128
        surf.blit(gamemap,(0-px,0+py))
        if frm == 1:
            sira = 13
            while sira > -1:
                sira2 = 10
                while sira2 > -1:
                    if maplist[sira][sira2][0] == 1:
                        surf.blit(capali,(64+sira2*16,16+sira*16+py))
                        if pak == 1:
                            if maplist[sira][sira2][1] == 0:
                                pako = pygame.Surface((16,16),pygame.SRCALPHA)
                                pako.blit(patato_1,(0,0))
                                pako.set_alpha(alp)
                                surf.blit(pako,(64+sira2*16,16+sira*16+py))
                        elif dak == 1:
                            if maplist[sira][sira2][1] == 0:
                                dako = pygame.Surface((16,16),pygame.SRCALPHA)
                                dako.blit(domato_1,(0,0))
                                dako.set_alpha(alp)
                                surf.blit(dako,(64+sira2*16,16+sira*16+py))
                        if maplist[sira][sira2][1] == "patato":
                            surf.blit(patatolist[maplist[sira][sira2][2]],(64+sira2*16,16+sira*16+py))
                            if maplist[sira][sira2][2] < 4:
                                if pygame.time.get_ticks() - maplist[sira][sira2][3] > 1000:
                                    maplist[sira][sira2][3] = pygame.time.get_ticks()
                                    maplist[sira][sira2][2]+= 1

                        elif maplist[sira][sira2][1] == "domato":
                            surf.blit(domatolist[maplist[sira][sira2][2]],(64+sira2*16,16+sira*16+py))
                            if maplist[sira][sira2][2] < 4:
                                if pygame.time.get_ticks() - maplist[sira][sira2][3] > 1000:
                                    maplist[sira][sira2][3] = pygame.time.get_ticks()
                                    maplist[sira][sira2][2]+= 1
                    else:
                        if ca == 1:
                            msp = pygame.Surface((16,16),pygame.SRCALPHA)
                            msp.blit(capali,(0,0))
                            msp.set_alpha(alp)
                            surf.blit(msp,(64+sira2*16,16+sira*16+py))
                    sira2 -= 1
                sira -= 1

        if pak == 1:
            if alpi == 0:
                if pygame.time.get_ticks() - atimer > 10:
                    alp+= 1
                    atimer = pygame.time.get_ticks()
                if alp == 150:
                    alpi = 1
            elif alpi == 1:
                if pygame.time.get_ticks() - atimer > 10:
                    alp-= 1
                    atimer = pygame.time.get_ticks()
                if alp == 35:
                    alpi = 0
            if rmx > 64 and rmy-py > 16 and rmy-py < 240 and rmx < 240 :
                if maplist[may][max][0] == 0:
                    pk = 0
                    
                else:
                    pk = 1
                    mspc = pygame.Surface((16,16),pygame.SRCALPHA)
                    mspc.blit(patato_1,(0,0))
                    mspc.set_alpha(128)
                    surf.blit(mspc,patato_1rect)
            else:
                pk=0
            px = 256
            patato_1rect.x,patato_1rect.y = (rmx//16)*16,(rmy//16)*16

        if dak == 1:
            if alpi == 0:
                if pygame.time.get_ticks() - atimer > 10:
                    alp+= 1
                    atimer = pygame.time.get_ticks()
                if alp == 150:
                    alpi = 1
            elif alpi == 1:
                if pygame.time.get_ticks() - atimer > 10:
                    alp-= 1
                    atimer = pygame.time.get_ticks()
                if alp == 35:
                    alpi = 0
            if rmx > 64 and rmy-py > 16 and rmy-py < 240 and rmx < 240 :
                if maplist[may][max][0] == 0:
                    dk = 0
                    
                else:
                    dk = 1
                    mspc = pygame.Surface((16,16),pygame.SRCALPHA)
                    mspc.blit(domato_1,(0,0))
                    mspc.set_alpha(128)
                    surf.blit(mspc,domato_1rect)
            else:
                dk=0
            px = 256
            domato_1rect.x,domato_1rect.y = (rmx//16)*16,(rmy//16)*16

        if ca == 1:
            surf.blit(domatoE,domatorect)
            surf.blit(patatoE,patatorect)
            if alpi == 0:
                if pygame.time.get_ticks() - atimer > 10:
                    alp+= 1
                    atimer = pygame.time.get_ticks()
                if alp == 150:
                    alpi = 1
            elif alpi == 1:
                if pygame.time.get_ticks() - atimer > 10:
                    alp-= 1
                    atimer = pygame.time.get_ticks()
                if alp == 35:
                    alpi = 0
            
            
            if rmx > 64 and rmy-py > 16 and rmy-py < 240 and rmx < 240 :
                if maplist[may][max][0] == 0:
                    a = 1
                    mspc = pygame.Surface((16,16),pygame.SRCALPHA)
                    mspc.blit(capali,(0,0))
                    mspc.set_alpha(96)
                    surf.blit(mspc,capalirect)
                    #surf.blit(capali,capalirect)
                else:
                    a = 0
                    if mouse[0]:
                        if maplist[may][max][1] == "domato":
                            if maplist[may][max][2] == 4:
                                idomato+=1
                                maplist[may][max]= [0,0,0,0]
                        elif maplist[may][max][1] == "patato":
                            if maplist[may][max][2] == 4:
                                ipatato+=1
                                maplist[may][max]= [0,0,0,0]
                #surf.blit(capali,capalirect)
            else:
                a=0
            px = 256
            capalirect.x,capalirect.y = (rmx//16)*16,(rmy//16)*16
            
            #11 x 14
        surf.blit(domatos,domatosrect)
        idom = pfont.render(":"+str(idomato),1,(255,255,255))
        surf.blit(idom,(domatosrect.x+16,domatosrect.y))
        surf.blit(patatos,patatosrect)
        ipat = pfont.render(":"+str(ipatato),1,(255,255,255))
        surf.blit(ipat,(patatosrect.x+16,patatosrect.y))
        
        surf.blit(capa,caparect)

        pygame.draw.rect(surf,(255,255,255),(rmx,rmy,1,1))
        pygame.draw.rect(surf,(255,255,255),(rmx,rmy,1,1))

        if m == 1:
            grnt.blit(pygame.transform.scale(surf,(1024,512)),(0,0))
        elif m == 2:
            grnt.blit(pygame.transform.scale2x(surf),(0,0))

        if screen_size[0]//2 > screen_size[1]:
            rmx = ((mx - (screen_size[0]/2-screen_size[1]))*256)/(screen_size[1]*2)
            rmy = ((my*128)/screen_size[1])
            screen.blit(pygame.transform.scale(grnt,(screen_size[1]*2,screen_size[1])),((screen_size[0]//2-screen_size[1]),0))
            pygame.draw.rect(screen,(255,255,255),((screen_size[0]//2-screen_size[1]),0,screen_size[1]*2,screen_size[1]),2)
            
        else:
            rmx = (mx*256)/screen_size[0]
            rmy = ((my- -((screen_size[0]/2-screen_size[1])/2))*128)/(screen_size[0]/2)
            screen.blit(pygame.transform.scale(grnt,(screen_size[0],screen_size[0]//2)),(0,-((screen_size[0]//2-screen_size[1])//2)))
            pygame.draw.rect(screen,(255,255,255),(0,-((screen_size[0]//2-screen_size[1])//2),screen_size[0],screen_size[0]//2),2)
    elif gamest == "menu":
        if mrect.colliderect(pbrect):
            screen.blit(pb2,pbrect)
        else:
            screen.blit(pb1,pbrect)
        if mrect.colliderect(ayarrct):
            screen.blit(ayar2,ayarrct)
        else:
            screen.blit(ayar1,ayarrct)
    elif gamest == "ayar":
        ayar1 = afont.render("Görüntü ayarları:",1,(0,0,0))
        ayar2 = afont.render("Pastel görüntü",1,(255,255,255))

        pygame.draw.rect(screen,(255,255,255),(24,24,200,32))
        screen.blit(ayar1,(24,24))
        screen.blit(ayar2,(48,64))
        if m == 1:
            pygame.draw.rect(screen,(255,0,0),(24,72,16,16))
        elif m== 2:
            pygame.draw.rect(screen,(0,255,0),(24,72,16,16))
    sltfps = str(int(clock.get_fps()))
    gf = font.render(sltfps,1,(255,255,255))
    #screen.blit(gf,(0,0))
    clock.tick(60)
    pygame.display.update()
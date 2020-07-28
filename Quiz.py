#---------------------------------------------Modules------
import sys
from os import environ, listdir
from os.path import isfile, join
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
import time

#---------------------------------------------Colors-------
black = (0,0,0)
white = (255,255,255)
red = (180,0,0)
blue = (0,0,180)
green = (0,180,0)
gray = (200,200,200)
dark_gray = (70,70,70)

#---------------------------------------------Show_Screen-------
def scr():
    global screen, white, black
    pygame.draw.rect(screen, white, (0,0,1440,810))
    for ic in [(30,30,1380,5), (30,775,1380,5) ,(30,30,5,750), (1405,30,5,750)]:
        pygame.draw.rect(screen, black, ic)
    pygame.display.flip()
    
#---------------------------------------------Screen-------
pygame.init()
screen = pygame.display.set_mode((1440, 810))
pygame.display.set_caption("Quiz")
scr()

#---------------------------------------------Login--------
def loginRects(but_font, c1, c2, c3):
    global screen, black, gray
    pygame.draw.rect(screen, gray, (690,160,610,70))
    for ic in [(690,160,610,5), (690,225,610,5), (690,160,5,70), (1295,160,5,70)]:
        pygame.draw.rect(screen, c1, ic)
    pygame.draw.rect(screen, gray, (690,320,610,70))
    for ic in [(690,320,610,5), (690,385,610,5), (690,320,5,70), (1295,320,5,70)]:
        pygame.draw.rect(screen, c2, ic)
    pygame.draw.rect(screen, c3, (910,430,170,70))
    but_label = but_font.render("LOGIN", 1, gray)
    screen.blit(but_label, (930, 447))

def login():
    global screen, black, red, white, gray, dark_gray, green
    u_file = open("./files/users.txt", "r")
    users = {us[0]: [us[1], us[2]] for us in [u[:-1].split() for u in u_file.readlines()]}
    u_file.close()
    
    pygame.draw.rect(screen, white, (630,40,770,730))
    li_font = pygame.font.SysFont("", 70)
    but_font = pygame.font.SysFont("", 60)
    box_font = pygame.font.SysFont("", 50)
    nati_font = pygame.font.SysFont("", 40)
    war_font = pygame.font.SysFont("", 30)
    
    li_label = li_font.render("USERNAME", 1, black)
    screen.blit(li_label, (715, 110))
    li_label = li_font.render("PASSWORD", 1, black)
    screen.blit(li_label, (715, 270))
    
    loginRects(but_font, black, black, black)
    
    login_exit = True
    login_mode = 0
    cursor = 0
    sts = ["",""]
    box_coor = [(700, 175), (700, 335)]
    while login_exit:
        if login_mode == 2:
            loginRects(but_font, black, black, red)
            for imc in range(2):
                box_label = box_font.render(sts[imc], 1, black)
                screen.blit(box_label, box_coor[imc])
        else:
            if login_mode == 0:
                loginRects(but_font, red, black, black)
            elif login_mode == 1:
                loginRects(but_font, black, red, black)
            if 0 <= cursor % 100 <= 49:
                box_label = box_font.render(sts[login_mode]+"|", 1, black)
            elif 50 <= cursor % 100 <= 99:
                box_label = box_font.render(sts[login_mode], 1, black)
            screen.blit(box_label, box_coor[login_mode])
            box_label = box_font.render(sts[1-login_mode], 1, black)
            screen.blit(box_label, box_coor[1-login_mode])
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                exit0(0)
                return 0
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return 0
                elif (evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN) and login_mode == 2:
                    pygame.draw.rect(screen, white, (685,510,450,80))
                    if "" in sts:
                        if sts[0] == "":
                            war_label = war_font.render("*Username is empty", 1, red)
                            screen.blit(war_label, (690, 515))
                            if sts[1] == "":
                                war_label = war_font.render("*Password is empty", 1, red)
                                screen.blit(war_label, (690, 540))
                        elif sts[1] == "":
                            war_label = war_font.render("*Password is empty", 1, red)
                            screen.blit(war_label, (690, 515))
                        break
                    if sts[0] not in users:
                        war_label = war_font.render("*Username is wrong", 1, red)
                        screen.blit(war_label, (690, 515))
                        break
                    if sts[1] != users[sts[0]][0]:
                        war_label = war_font.render("*Password is wrong", 1, red)
                        screen.blit(war_label, (690, 515))
                        war_label = war_font.render("*Did you forget your password?", 1, red)
                        screen.blit(war_label, (690, 540))
                        forget = 1
                        yn = [["NO", (1062,535,50,28), (1073, 540)], ["YES", (1005,535,50,28), (1010, 540)]]
                        forget_exit = True
                        while forget_exit:
                            pygame.draw.rect(screen, red, yn[forget][1])
                            war_label = war_font.render(yn[forget][0], 1, white)
                            screen.blit(war_label, yn[forget][2])
                            pygame.draw.rect(screen, black, yn[1-forget][1])
                            war_label = war_font.render(yn[1-forget][0], 1, white)
                            screen.blit(war_label, yn[1-forget][2])
                            pygame.display.flip()
                            for eventi in pygame.event.get():
                                if eventi.type == pygame.QUIT:
                                    exit0(0)
                                    return 0
                                elif eventi.type == pygame.KEYDOWN:
                                    if eventi.key == pygame.K_ESCAPE:
                                        return 0
                                    if eventi.key == pygame.K_RIGHT:
                                        forget = 0
                                    if eventi.key == pygame.K_LEFT:
                                        forget = 1
                                    if eventi.key == pygame.K_KP_ENTER or eventi.key == pygame.K_RETURN:
                                        if forget == 0:
                                            forget_exit = False
                                            login_mode = 1
                                            break
                                        if forget == 1:
                                            li_label = li_font.render("NATIONAL-CODE", 1, black)
                                            screen.blit(li_label, (715, 590))
                                            cursor = 0
                                            nati = ""
                                            pygame.display.flip()
                                            nati_exit = True
                                            while nati_exit:
                                                pygame.draw.rect(screen, gray, (690,640,610,70))
                                                for ic in [(690,640,610,5), (690,705,610,5), (690,640,5,70), (1295,640,5,70)]:
                                                    pygame.draw.rect(screen, red, ic)
                                                if 0 <= cursor % 200 <= 99:
                                                    nati_label = box_font.render(nati+"|", 1, black)
                                                elif 100 <= cursor % 200 <= 199:
                                                    nati_label = box_font.render(nati, 1, black)
                                                screen.blit(nati_label, (700,655))
                                                pygame.display.flip()
                                                for evente in pygame.event.get():
                                                    if evente.type == pygame.QUIT:
                                                        exit0(0)
                                                        return 0
                                                    elif evente.type == pygame.KEYDOWN:
                                                        if evente.key == pygame.K_ESCAPE or evente.key == pygame.K_UP:
                                                            forget = 0
                                                            nati_exit = False
                                                            pygame.draw.rect(screen, white, (689,589,627,170))
                                                            pygame.display.flip()
                                                        elif evente.key == pygame.K_BACKSPACE:
                                                            nati = nati[:-1]
                                                        elif evente.key == pygame.K_KP_ENTER or evente.key == pygame.K_RETURN:
                                                            pygame.draw.rect(screen, white, (699,717,600,30))
                                                            c_gr = red
                                                            if nati == "":
                                                                nati_war = "National-code is empty"
                                                            elif not nati.isdigit():
                                                                nati_war = "National-code must be numerical"
                                                            elif nati != users[sts[0]][1]:
                                                                nati_war = "National-code is wrong"
                                                            else:
                                                                nati_war = "Your password is "+users[sts[0]][0]
                                                                c_gr = green
                                                                forget_exit = False
                                                                nati_exit = False
                                                                login_mode = 1
                                                                for ic in [(690,640,610,5), (690,705,610,5), (690,640,5,70), (1295,640,5,70)]:
                                                                    pygame.draw.rect(screen, black, ic)
                                                            nati_label = nati_font.render(nati_war, 1, c_gr)
                                                            screen.blit(nati_label, (700,718))
                                                            pygame.display.flip()
                                                        elif len(nati) <= 9:
                                                            nati += evente.unicode
                                                cursor += 1
                        break
                    return [sts[0]] + users[sts[0]]
                elif evento.key == pygame.K_UP or (evento.key == pygame.K_TAB and pygame.key.get_mods() & pygame.KMOD_SHIFT):
                    login_mode = {0:0, 1:0, 2:1}[login_mode]
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_TAB or evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN:
                    login_mode = {0:1, 1:2, 2:2}[login_mode]
                elif evento.key == pygame.K_BACKSPACE:
                    sts[login_mode] = sts[login_mode][:-1]
                elif login_mode != 2 and len(sts[login_mode]) <= 15:
                    sts[login_mode] += evento.unicode
        cursor += 1
        pygame.display.flip()
#---------------------------------------------Signup--------
def signupRects(but_font, c1, c2, c3, c4):
    global screen, black, gray
    pygame.draw.rect(screen, gray, (690,160,610,70))
    for ic in [(690,160,610,5), (690,225,610,5), (690,160,5,70), (1295,160,5,70)]:
        pygame.draw.rect(screen, c1, ic)
    pygame.draw.rect(screen, gray, (690,320,610,70))
    for ic in [(690,320,610,5), (690,385,610,5), (690,320,5,70), (1295,320,5,70)]:
        pygame.draw.rect(screen, c2, ic)
    pygame.draw.rect(screen, gray, (690,480,610,70))
    for ic in [(690,480,610,5), (690,545,610,5), (690,480,5,70), (1295,480,5,70)]:
        pygame.draw.rect(screen, c3, ic)
    pygame.draw.rect(screen, c4, (900,590,190,70))
    but_label = but_font.render("SIGN UP", 1, gray)
    screen.blit(but_label, (910, 607))

def signup():
    global screen, black, red, white, green
    u_file = open("./files/users.txt", "r")
    users = {us[0]: [us[1], us[2]] for us in [u[:-1].split() for u in u_file.readlines()]}
    u_file.close()
    
    pygame.draw.rect(screen, white, (630,40,770,730))
    li_font = pygame.font.SysFont("", 70)
    but_font = pygame.font.SysFont("", 60)
    box_font = pygame.font.SysFont("", 50)
    war_font = pygame.font.SysFont("", 30)
    
    li_label = li_font.render("USERNAME", 1, black)
    screen.blit(li_label, (715, 110))
    li_label = li_font.render("PASSWORD", 1, black)
    screen.blit(li_label, (715, 270))
    li_label = li_font.render("NATIONAL-CODE", 1, black)
    screen.blit(li_label, (715, 430))
    
    signupRects(but_font, black, black, black, black)
    signup_exit = True
    signup_mode = 0
    cursor = 0
    sts = ["","",""]
    box_coor = [(700, 175), (700, 335), (700, 495)]
    conv_mode = [[1,2], [0,2], [0,1]]
    while signup_exit:
        if signup_mode == 3:
            signupRects(but_font, black, black, black, red)
            for imc in range(3):
                box_label = box_font.render(sts[imc], 1, black)
                screen.blit(box_label, box_coor[imc])
        else:
            if signup_mode == 0:
                signupRects(but_font, red, black, black, black)
            elif signup_mode == 1:
                signupRects(but_font, black, red, black, black)
            elif signup_mode == 2:
                signupRects(but_font, black, black, red, black)
            if 0 <= cursor % 100 <= 49:
                box_label = box_font.render(sts[signup_mode]+"|", 1, black)
            elif 50 <= cursor % 100 <= 99:
                box_label = box_font.render(sts[signup_mode], 1, black)
            screen.blit(box_label, box_coor[signup_mode])
            box_label = box_font.render(sts[conv_mode[signup_mode][0]], 1, black)
            screen.blit(box_label, box_coor[conv_mode[signup_mode][0]])
            box_label = box_font.render(sts[conv_mode[signup_mode][1]], 1, black)
            screen.blit(box_label, box_coor[conv_mode[signup_mode][1]])
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                exit0(0)
                return 0
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return 0
                elif (evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN) and signup_mode == 3:
                    pygame.draw.rect(screen, white, (689,589,627,170))
                    txts = []
                    if "" in sts:
                        if sts[0] == "":
                            txts.append("Username is empty")
                        if sts[1] == "":
                            txts.append("Password is empty")
                        if sts[2] == "":
                            txts.append("National-code is empty")
                    elif not sts[2].isdigit():
                        txts.append("National-code must be numerical")
                    elif len(sts[2]) != 10:
                        txts.append("National-code must be 10 digits")
                    elif sts[0] in users:
                        txts.append("Username is already taken")
                    if txts == []:
                        war_label = war_font.render("*Signed-up succesfully", 1, green)
                        screen.blit(war_label, (690, 670))
                        pygame.display.flip()
                        u_file = open("./files/users.txt", "a")
                        u_file.write(" ".join(sts) + "\n")
                        u_file.close()
                        time.sleep(1.5)
                        return 0
                    for iwr in range(len(txts)):
                        war_label = war_font.render("*"+txts[iwr], 1, red)
                        screen.blit(war_label, (690, 670+iwr*27))
                    pygame.display.flip()
                    
                elif evento.key == pygame.K_UP or (evento.key == pygame.K_TAB and pygame.key.get_mods() & pygame.KMOD_SHIFT):
                    signup_mode = {0:0, 1:0, 2:1, 3:2}[signup_mode]
                elif evento.key == pygame.K_DOWN or evento.key == pygame.K_TAB or evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN:
                    signup_mode = {0:1, 1:2, 2:3, 3:3}[signup_mode]
                elif evento.key == pygame.K_BACKSPACE:
                    sts[signup_mode] = sts[signup_mode][:-1]
                elif (signup_mode in [0,1] and len(sts[signup_mode]) <= 15) or (signup_mode == 2 and len(sts[signup_mode]) <= 9):
                    sts[signup_mode] += evento.unicode
        cursor += 1
        pygame.display.flip()
#---------------------------------------------Account-------
def account(user):
    global screen, black, red, white, green
    scr()
    acc_bar = ["QUIZ", "LOG OUT"]
    acc_num = {0: 180+100, 1: 380+100}
    mode_font = pygame.font.SysFont("", 90)
    yn_font = pygame.font.SysFont("", 60)
    imgQ = pygame.image.load('./files/Q.png')
    
    acc_font = pygame.font.SysFont("", 40)
    acc_label = acc_font.render(user[0], 1, black)
    screen.blit(acc_label, (85, 50))
    pygame.draw.rect(screen, green, (50,50,30,30))
    
    for im in range(2):
        label = mode_font.render(acc_bar[im], 1, black)
        screen.blit(label, (180, acc_num[im]))
    pygame.draw.rect(screen, white, (630,40,770,730))
    screen.blit(imgQ,(695,120))
    acc_mode = 0
    pygame.display.flip()
    while True:
        for evento in pygame.event.get():
            exmo = 0
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN:
                    if acc_mode == 0:
                        quiz_name = select(user)
                        if type(quiz_name) == str:
                            quiz(user, quiz_name)
                            scr()
                            screen.blit(acc_label, (85, 50))
                            pygame.draw.rect(screen, green, (50,50,30,30))
                            pygame.display.flip()
                    elif acc_mode == 1:
                        exmo = 1
                elif evento.key == pygame.K_UP:
                    acc_mode = 0
                elif evento.key == pygame.K_DOWN:
                    acc_mode = 1
                elif evento.key == pygame.K_ESCAPE:
                    acc_mode = 1
                    exmo = 1
                        
            for im in range(2):
                label = mode_font.render(acc_bar[im], 1, black)
                screen.blit(label, (180, acc_num[im]))    
            label = mode_font.render(acc_bar[acc_mode], 1, red)
            screen.blit(label, (180, acc_num[acc_mode]))
            pygame.display.flip()
            
            if evento.type == pygame.QUIT:
                acc_mode = exit0(0) - 1
            if exmo:
                acc_mode = exit0(1) - 1
                if acc_mode == -1:
                    return 0
        
        for im in range(2):
            label = mode_font.render(acc_bar[im], 1, black)
            screen.blit(label, (180, acc_num[im]))
        label = mode_font.render(acc_bar[acc_mode], 1, red)
        screen.blit(label, (180, acc_num[acc_mode]))
        pygame.draw.rect(screen, white, (630,40,770,730))
        screen.blit(imgQ,(695,120))
        pygame.display.flip()
    pygame.display.flip()
#---------------------------------------------Select--------
def select(user):
    global screen, black, red, white
    q_path = "./files/quizzes"
    quizzes = [f.replace(".txt", "") for f in listdir(q_path) if isfile(join(q_path, f))]
    qn = len(quizzes)
    pygame.draw.rect(screen, white, (630,40,770,730))
    quiz_font = pygame.font.SysFont("", 90)
    q_font = pygame.font.SysFont("", 60)
    
    label_quiz = quiz_font.render("QUIZZES", 1, black)
    screen.blit(label_quiz, (800, 100))
    quiz_mode = 0
    while True:
        for iqn in range(qn):
            labelq = q_font.render(quizzes[iqn], 1, black)
            screen.blit(labelq, (650+((iqn%3)*230), 210+((iqn//3)*100)))
        labelq = q_font.render(quizzes[quiz_mode], 1, red)
        screen.blit(labelq, (650+((quiz_mode%3)*230), 210+((quiz_mode//3)*100)))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                exit0(0)
                pygame.draw.rect(screen, white, (630,40,770,730))
                screen.blit(label_quiz, (870, 100))
                pygame.display.flip()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN:
                    return quizzes[quiz_mode]
                elif evento.key == pygame.K_ESCAPE:
                    return 0
                elif evento.key == pygame.K_END:
                    quiz_mode = qn-1
                elif evento.key == pygame.K_HOME:
                    quiz_mode = 0
                elif evento.key == pygame.K_DOWN and quiz_mode < qn-3:
                    quiz_mode += 3
                elif evento.key == pygame.K_UP and quiz_mode > 2:
                    quiz_mode -= 3
                elif evento.key == pygame.K_RIGHT and quiz_mode != qn-1:
                    quiz_mode += 1
                elif evento.key == pygame.K_LEFT and quiz_mode != 0:
                    quiz_mode -= 1
#---------------------------------------------Quiz----------
def result(user, ans, quest, tend):
    global screen, black, red, white, blue, gray, dark_gray
    
    correct = [quest[iq][1].index(quest[iq][2]) for iq in range(10)]
    isc = [0 if ans[iq]==-1 else 2 if ans[iq]==correct[iq] else 1 for iq in range(10)]
    iscc = [gray, red, green]
    iscw = ["Blank", "Wrong", "Correct"]
    iscr = [190,170,155]
    
    scr()
    acc_font = pygame.font.SysFont("", 40)
    Q_font = pygame.font.SysFont("", 65)
    Q2_font = pygame.font.SysFont("", 45)
    acc_label = acc_font.render(user[0], 1, black)
    screen.blit(acc_label, (85, 50))
    pygame.draw.rect(screen, green, (50,50,30,30))
    
    Q_label = Q_font.render("Correct: "+str(isc.count(2)) , 1, green)
    screen.blit(Q_label, (585, 248))
    Q_label = Q_font.render("Blank: "+str(isc.count(0)) , 1, dark_gray)
    screen.blit(Q_label, (585, 328))
    Q_label = Q_font.render("Worng: "+str(isc.count(1)) , 1, red)
    screen.blit(Q_label, (585, 408))
    Q_label = Q_font.render("Score: "+str(isc.count(2)*10)+"%" , 1, black)
    screen.blit(Q_label, (585, 488))
    pygame.display.flip()
    which_exit = True
    which = 1
    cursor = 0
    while which_exit:
        if not tend:
            if cursor % 600 < 300:
                Q_label = Q_font.render("Time is up" , 1, red)
                screen.blit(Q_label, (580, 168))
            elif cursor % 600 == 300:
                pygame.draw.rect(screen, white, (579,167,300,70))
            cursor += 1
        if which:
            pygame.draw.rect(screen, gray, (510,580,200,70))
            pygame.draw.rect(screen, red, (730,580,200,70))
        else:
            pygame.draw.rect(screen, red, (510,580,200,70))
            pygame.draw.rect(screen, gray, (730,580,200,70))
        Q_label = Q_font.render("Quit", 1, black)
        screen.blit(Q_label, (560, 594))
        Q_label = Q_font.render("Details", 1, black)
        screen.blit(Q_label, (755, 594))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                scr()
                exit0(0)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN:
                    if which == 0:
                        return 0
                    which_exit = False
                elif evento.key == pygame.K_ESCAPE:
                    if which == 0:
                        return 0
                    which = 0
                elif evento.key == pygame.K_RIGHT:
                    which = 1
                elif evento.key == pygame.K_LEFT:
                    which = 0
    iq = 0
    cursor = 0
    while True:
        pygame.draw.rect(screen, white, (150,170,1100,480))
        if 0 <= iq <= 9:
            Q_label = Q_font.render(iscw[isc[iq]], 1, iscc[isc[iq]])
            screen.blit(Q_label, (iscr[isc[iq]], 180))
            Q_label = Q_font.render(quest[iq][0], 1, black)
            screen.blit(Q_label, (330, 180))
            for iqa in range(4):
                Q_label = Q_font.render(quest[iq][1][iqa], 1, black)
                screen.blit(Q_label, (380, 290+iqa*80))
                pygame.draw.rect(screen, black, (330,292+iqa*80,40,40))
                pygame.draw.rect(screen, white, (335,297+iqa*80,30,30))
            if ans[iq] != -1:
                pygame.draw.rect(screen, red, (340,302+ans[iq]*80,20,20))
            pygame.draw.rect(screen, green, (340,302+correct[iq]*80,20,20))
        elif iq == -1:
            if cursor % 400 < 200:
                pygame.draw.rect(screen, red, (620,440,200,70))
            else:
                pygame.draw.rect(screen, black, (620,440,200,70))
            cursor += 1
            Q_label = Q_font.render("Quit" , 1, white)
            screen.blit(Q_label, (670, 454))
        
        if 0 <= iq <= 9:
            pygame.draw.rect(screen, red, (225+iq*100,680,95,60))
        for ip in range(10):
            if ip != iq:
                pygame.draw.rect(screen, gray, (225+ip*100,680,95,60))
            pygame.draw.rect(screen, iscc[isc[ip]], (225+ip*100,672,95,5))
            Q_label = Q_font.render(str(ip+1), 1, black)
            screen.blit(Q_label, (260+ip*100-((len(str(ip+1))-1)*12), 688))
        
        if iq == -1:
            pygame.draw.rect(screen, red, (85,680,100,60))
        else:
            pygame.draw.rect(screen, gray, (85,680,100,60))
        Q_label = Q2_font.render("Quit", 1, black)
        screen.blit(Q_label, (100, 696))
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                scr()
                exit0(0)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN and iq == -1:
                    return 0
                elif evento.key == pygame.K_ESCAPE:
                    if iq == -1:
                        return 0
                    iq = -1
                elif evento.key == pygame.K_END:
                    iq = 9
                elif evento.key == pygame.K_HOME:
                    iq = -1
                elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_PAGEUP:
                    if iq != 9:
                        iq += 1
                elif evento.key == pygame.K_LEFT or evento.key == pygame.K_PAGEDOWN:
                    if iq != -1:
                        cursor = 0
                        iq -= 1

def time0(time1, tt, acc_font):
    global screen, white, red
    time2 = time.localtime()[5]
    if time1 != time2:
        time1 = time2
        if tt[1] == 0:
            if tt[0] == 0:
                return -1
            tt[0] -= 1
            tt[1] += 60
        tt[1] -= 1
        pygame.draw.rect(screen, white, (1325,45,65,35))
        acc_label = acc_font.render(str(tt[0])+":"+(2-len(str(tt[1])))*"0"+str(tt[1]) , 1, red)
        screen.blit(acc_label, (1330, 50))
    return time2
            
def quiz(user, q_name):
    global screen, black, red, white, blue, gray
    q_file = open("./files/quizzes/"+q_name+".txt", "r")
    qt = q_file.readlines()
    quest = [[qt[j*3+i][:-1] if i!=1 else qt[j*3+i][:-1].split(" + ") for i in range(3)] for j in range(len(qt)//3)]
    q_file.close()
    
    scr()
    Q_font = pygame.font.SysFont("", 65)
    Q2_font = pygame.font.SysFont("", 45)
    acc_font = pygame.font.SysFont("", 40)
    acc_label = acc_font.render(user[0], 1, black)
    screen.blit(acc_label, (85, 50))
    pygame.draw.rect(screen, green, (50,50,30,30))
    
    ans = [-1]*10
    iq = ia = 0
    cursor = 0
    tt = [3,0]
    time1 = time.localtime()[5]
    while True:
        pygame.draw.rect(screen, white, (280,170,1100,450))
        if 0 <= iq <= 9:
            Q_label = Q_font.render(quest[iq][0], 1, black)
            screen.blit(Q_label, (330, 180))
            for iqa in range(4):
                Q_label = Q_font.render(quest[iq][1][iqa], 1, black)
                screen.blit(Q_label, (380, 290+iqa*80))
                if ia == iqa:
                    pygame.draw.rect(screen, red, (330,292+iqa*80,40,40))
                else:
                    pygame.draw.rect(screen, black, (330,292+iqa*80,40,40))
                pygame.draw.rect(screen, white, (335,297+iqa*80,30,30))
            if ans[iq] != -1:
                pygame.draw.rect(screen, blue, (340,302+ans[iq]*80,20,20))
        elif iq == 10:
            Q_label = Q_font.render("Answered: "+str(10-ans.count(-1)) , 1, black)
            screen.blit(Q_label, (585, 278))
            Q_label = Q_font.render("Blank: "+str(ans.count(-1)) , 1, black)
            screen.blit(Q_label, (620, 358))
            if cursor % 400 < 200:
                pygame.draw.rect(screen, red, (620,440,200,70))
            else:
                pygame.draw.rect(screen, black, (620,440,200,70))
            cursor += 1
            Q_label = Q_font.render("Finish" , 1, white)
            screen.blit(Q_label, (655, 454))
        elif iq == -1:
            if cursor % 400 < 200:
                pygame.draw.rect(screen, red, (620,440,200,70))
            else:
                pygame.draw.rect(screen, black, (620,440,200,70))
            cursor += 1
            Q_label = Q_font.render("Quit" , 1, white)
            screen.blit(Q_label, (670, 454))
        
        time1 = time0(time1, tt, acc_font)
        if time1 == -1:
            result(user, ans, quest, 0)
            return 0
            
        if 0 <= iq <= 9:
            pygame.draw.rect(screen, red, (225+iq*100,680,95,60))
        for ip in range(10):
            if ip != iq:
                pygame.draw.rect(screen, gray, (225+ip*100,680,95,60))
            Q_label = Q_font.render(str(ip+1), 1, black)
            screen.blit(Q_label, (260+ip*100-((len(str(ip+1))-1)*12), 688))
        
        if iq == 10:
            pygame.draw.rect(screen, red, (1265,680,100,60))
        else:
            pygame.draw.rect(screen, gray, (1265,680,100,60))
        Q_label = Q2_font.render("Done", 1, black)
        screen.blit(Q_label, (1277, 696))
        if iq == -1:
            pygame.draw.rect(screen, red, (85,680,100,60))
        else:
            pygame.draw.rect(screen, gray, (85,680,100,60))
        Q_label = Q2_font.render("Quit", 1, black)
        screen.blit(Q_label, (100, 696))
        pygame.display.flip()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                scr()
                exit0(0)
                return 0
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN:
                    if 0 <= iq <= 9:
                        if ans[iq] == ia:
                            ans[iq] = -1
                        else:
                            ans[iq] = ia
                    if iq == 10:
                        result(user, ans, quest, 1)
                        return 0
                    if iq == -1:
                        return 0
                elif evento.key == pygame.K_ESCAPE:
                    if iq == -1:
                        return 0
                    iq = -1
                elif evento.key == pygame.K_END:
                    iq = 10
                elif evento.key == pygame.K_HOME:
                    iq = -1
                elif evento.key == pygame.K_DOWN:
                    if ia != 3:
                        ia += 1
                elif evento.key == pygame.K_UP:
                    if ia != 0:
                        ia -= 1
                elif evento.key == pygame.K_RIGHT or evento.key == pygame.K_PAGEUP:
                    if iq != 10:
                        cursor = 0
                        iq += 1
                        ia = 0
                        if 0 <= iq <= 9 and ans[iq] != -1:
                            ia = ans[iq]
                elif evento.key == pygame.K_LEFT or evento.key == pygame.K_PAGEDOWN:
                    if iq != -1:
                        cursor = 0
                        iq -= 1
                        ia = 0
                        if 0 <= iq <= 9 and ans[iq] != -1:
                            ia = ans[iq]
        time1 = time0(time1, tt, acc_font)
        if time1 == -1:
            result(user, ans, quest, 0)
            return 0
#---------------------------------------------Exit----------
def exit0(which):
    global screen, black, red, white
    which_st = ["EXIT", "LOG-OUT"]
    yn_color = {(1, "YES"): red , (0, "NO"): red, (0, "YES"): black, (1, "NO"): black}
    yn_coor = {"YES": (840, 440), "NO": (1000, 440)}
    pygame.draw.rect(screen, white, (630,40,770,730))
    Ex_font = pygame.font.SysFont("", 70)
    Ex_label = Ex_font.render("ARE YOU SURE TO " + which_st[which] + "?", 1, black)
    screen.blit(Ex_label, (650, 350))
    pygame.display.flip()
    
    exit_mode = 0
    while True:
        for yn in ["YES", "NO"]:
            label = yn_font.render(yn, 1, yn_color[(exit_mode, yn)])
            screen.blit(label, yn_coor[yn])
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT or ( evento.type == pygame.KEYDOWN and (evento.key == pygame.K_ESCAPE or ((evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN) and exit_mode))):
                exit_mode = 1
                for yn in ["YES", "NO"]:
                    label = yn_font.render(yn, 1, yn_color[(exit_mode, yn)])
                    screen.blit(label, yn_coor[yn])
                pygame.display.flip()
                if which:
                    return 0
                else:
                    pygame.quit()
                    sys.exit(0)
            elif evento.type == pygame.KEYDOWN:
                if (evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN) and not exit_mode:
                    return 2
                elif evento.key == pygame.K_UP:
                    return 1
                elif evento.key == pygame.K_RIGHT:
                    exit_mode = 0
                elif evento.key == pygame.K_LEFT:
                    exit_mode = 1
#---------------------------------------------|------
mode_bar = ["LOG IN", "SIGN UP", "EXIT"]
mode_num = {0: 180, 1: 380, 2: 580}
mode_font = pygame.font.SysFont("", 90)
yn_font = pygame.font.SysFont("", 60)

imgQ = pygame.image.load('./files/Q.png')
screen.blit(imgQ,(695,120))

while True:
    for im in range(3):
        label = mode_font.render(mode_bar[im], 1, black)
        screen.blit(label, (180, mode_num[im]))
    pygame.draw.rect(screen, white, (630,40,770,730))
    screen.blit(imgQ,(695,120))
    mode = 0
    pygame.display.flip()
    while True:
        for evento in pygame.event.get():
            exmo = 0
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_KP_ENTER or evento.key == pygame.K_RETURN:
                    if mode == 0:
                        user = login()
                        if type(user) == list:
                            account(user)
                            scr()
                    elif mode == 1:
                        signup()
                    elif mode == 2:
                        exmo = 1
                elif evento.key == pygame.K_UP:
                    mode -= 1
                    if mode <= 0:
                        mode = 0
                elif evento.key == pygame.K_DOWN:
                    mode += 1
                    if mode >= 2:
                        mode = 2
                elif evento.key == pygame.K_ESCAPE:
                    mode = 2
                    exmo = 1
                        
            for im in range(3):
                label = mode_font.render(mode_bar[im], 1, black)
                screen.blit(label, (180, mode_num[im]))    
            label = mode_font.render(mode_bar[mode], 1, red)
            screen.blit(label, (180, mode_num[mode]))
            pygame.display.flip()
            
            if evento.type == pygame.QUIT or exmo:
                mode = exit0(0)
        
        for im in range(3):
            label = mode_font.render(mode_bar[im], 1, black)
            screen.blit(label, (180, mode_num[im]))
        label = mode_font.render(mode_bar[mode], 1, red)
        screen.blit(label, (180, mode_num[mode]))
        pygame.draw.rect(screen, white, (630,40,770,730))
        screen.blit(imgQ,(695,120))
        pygame.display.flip()

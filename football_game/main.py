import pgzrun
from random import *

WIDTH = 1074
HEIGHT = 600
TITLE = '射门游戏'

g_flag = 1
i_flag = 1
player_flag = False
g_move_flag = True
i_move_flag = True
result = ''
score = 0

goalkeeper = Actor('守门员')
ball = Actor('足球')
strength_line = Actor('力度条')
indicator = Actor('指针')

goalkeeper.x = 430
goalkeeper.y = 320
ball.x = 537
ball.y = 550
strength_line.x = 900
strength_line.y = 400
indicator.x = 870
indicator.y = randint(265,535)

music.play('背景音乐')

def draw():
    global score
    screen.blit('背景',[-40,0])
    screen.draw.text(str(score),(20, 10),fontsize=48)
    screen.draw.text(str(result),(150,150) if len(result) == 4 else (330,150),fontsize=200,fontname='font',color='red')
    goalkeeper.draw()
    ball.draw()
    strength_line.draw()
    indicator.draw()

def update():
    global g_flag,player_flag,i_flag,g_move_flag,i_move_flag,score,result
    if g_move_flag:
        if g_flag == 1 and goalkeeper.x < 640:
            goalkeeper.x += 3
        elif goalkeeper.x >= 640:
            g_flag = 2
        if g_flag == 2 and goalkeeper.x > 430:
            goalkeeper.x -= 3
        elif goalkeeper.x <= 430:
            g_flag = 1

    if i_move_flag:
        if i_flag == 1 and indicator.y > 265:
            indicator.y -= 3
        elif indicator.y <= 265:
            i_flag = 2
        if i_flag == 2 and indicator.y < 535:
            indicator.y += 3
        elif indicator.y >= 535:
            i_flag = 1

    def close():
        global g_move_flag,player_flag
        g_move_flag,player_flag = False,False

    if player_flag and 307.5 <= indicator.y <= 492.5:
        i_move_flag = False
        if ball.y > 330:
            ball.y -= 2
        else:
            if ball.colliderect(goalkeeper):
                result = '失败'
                close()
            else:
                result = '成功'
                score += 1
                close()
    elif player_flag:
        i_move_flag = False
        if ball.y > 400:
            ball.y -= 2
        else:
            result = '力度不够'
            close()

def on_key_down(key):
    global player_flag
    if key == keys.SPACE:
        player_flag = True
    if key == keys.R:
        global g_flag,i_flag,g_move_flag,i_move_flag,score,result
        g_flag = 1
        i_flag = 1
        player_flag = False
        result = ''
        g_move_flag = True
        i_move_flag = True

        goalkeeper.x = 430
        goalkeeper.y = 320
        ball.x = 537
        ball.y = 550
        strength_line.x = 900
        strength_line.y = 400
        indicator.x = 870
        indicator.y = 307.5

pgzrun.go()
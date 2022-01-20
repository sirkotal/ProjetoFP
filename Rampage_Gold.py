import pygame
import random
from math import dist

resolution = (800,600)
hitbox = 64
one_block = 32

hit_count1 = 0
hit_count2 = 0
hit_count3 = 0

pygame.init()

screen = pygame.display.set_mode(resolution)

background = pygame.image.load("city_v2.png")
building1 = pygame.image.load("building1.png")
building2 = pygame.image.load("building2.png")
building3 = pygame.image.load("building3.png")
pygame.display.flip()

george_idle = pygame.image.load("george_idle2.png")
tank = pygame.image.load("tank.png")
chopper = pygame.image.load("helicopter.png")
chopper_r = pygame.image.load("helicopter.png")
chopper_l = pygame.image.load("helicopter2.png")
side_count = 1

bullet = pygame.image.load("bullet.png")
transparent = pygame.image.load("transparent.png")
bullet1 = transparent
bullet2 = transparent
bullet3 = transparent
bullet4 = transparent
bullet5 = transparent
bullet6 = transparent

traj1 = 0
traj2 = 0
traj3 = 0
traj4 = 0
traj5 = 0
traj6 = 0

measure = pygame.image.load("measurer.png")

# great_ape = pygame.image.load("great_ape.png")
# assault_theme = pygame.mixer.music.load("Kyoufu no Ginyu Tokusentai.mp3")
# pygame.mixer.music.play(loops=-1)

george_x = 0
george_y = 475
HP = 100

tank_x = 0
tank_y = 550

chopper_x = -75     #-75
chopper_y = 160
v_chopper = 0

bullet_list = [[120,185],[240,185],[360,185],[480,185],[600,185],[720,185]]
v_trigger = 0.05 
reverse_trigger = -0.05

v1 = 0
v2 = 0
level1 = [
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000000000000000000",
    "0000000000003003000000000",
    "0000000000002114000000000",
    "0000003003002114000000000",
    "0000002114002114000000000",
    "0000002114002114000003003",
    "0000002114002114000002111",
    "0000002114002114000002111",
    "0000002114002114000002111",
    "0000002114002114000002111",
    "0000002114002114000002111",
    "0000002114002114000002111",
    "0000000000000000000000000",
    "0000000000000000000000000",
]

running = True
clock = pygame.time.Clock()
left_key = right_key = up_key = down_key = False

while running:

    #1 input
    hit_key = False
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                running = False
            elif ev.key == pygame.K_LEFT:
                left_key = True
            elif ev.key == pygame.K_RIGHT:
                right_key = True
            elif ev.key == pygame.K_UP:
                up_key = True
            elif ev.key == pygame.K_DOWN:
                down_key = True
            elif ev.key == pygame.K_SPACE:
                hit_key = True
        elif ev.type == pygame.KEYUP:
            if ev.key == pygame.K_LEFT:
                left_key = False
            elif ev.key == pygame.K_RIGHT:
                right_key = False
            elif ev.key == pygame.K_UP:
                up_key = False
            elif ev.key == pygame.K_DOWN:
                down_key = False
            elif ev.key == pygame.K_SPACE:
                hit_key = False
    
    
    
    #2 movement
    frame_rate = clock.tick()
    if right_key:
        v1 = +0.1
    elif left_key:
        v1 = -0.1
    else:
        v1 = 0
        
        
    
    for row in range(len(level1)):
        for column in range(len(level1[row])):
            if level1[row][column] == "2":
                if george_x >= column*32-58 and george_x <= column*32+6:
                    if up_key:
                        v2 = -0.08
                    elif down_key:
                        v2 = +0.08
                    else:
                        v2 = 0
            elif level1[row][column] == "4":
                if george_x >= column*32-58 and george_x <= column*32+6:
                    if up_key:
                        v2 = -0.08
                    elif down_key:
                        v2 = +0.08
                    else:
                        v2 = 0
            elif level1[row][column] == "3":
                if george_x >= column*32-58 and george_x <= column*32+6:
                    if george_y <= row*32:
                        george_y = row*32
                        v2 = 0
                     
    
    george_x += v1*frame_rate
    george_y += v2*frame_rate
    previous_x = george_x
    
    
    if george_y != 475:
        george_x -= v1*frame_rate
    if george_y > 475:
        george_y = 475
        v2 = 0
    if george_y < 0:
        george_y = 0
        v2 = 0
    if george_x < -8:
        george_x = -8
        v1 = 0
    if george_x > 725:
        george_x = 725
        v1 = 0

    
    #3 destruction
    if hit_key and george_y != 475:
        if george_x >= 134 and george_x <= 294:
            hit_count1 += 1
        elif george_x >= 326 and george_x <= 486:
            hit_count2 += 1
        elif george_x >= 614 and george_x <= 799:
            hit_count3 += 1
    
    
    if hit_count1 == 2:
        if george_y >= 416:
            b1_height = 0
        elif george_y < 416:
            b1_height = 1
            
    if hit_count2 == 2:
        if george_y >= 384:
            b2_height = 0
        elif george_y < 384:
            b2_height = 1
            
    if hit_count3 == 2:
        if george_y >= 448:
            b3_height = 0
        elif george_y < 448:
            b3_height = 1
    
    if hit_count1 == 3 and b1_height == 0:
        building1 = pygame.image.load("building1_down.png")
    elif hit_count1 == 3 and b1_height == 1:
        building1 = pygame.image.load("building1_up.png")
        
    if hit_count2 == 3 and b2_height == 0:
        building2 = pygame.image.load("building2_down.png")
    elif hit_count2 == 3 and b2_height == 1:
        building2 = pygame.image.load("building2_up.png")
        
    if hit_count3 == 3 and b3_height == 0:
        building3 = pygame.image.load("building3_down.png")
    elif hit_count3 == 3 and b3_height == 1:
        building3 = pygame.image.load("building3_up.png")
        
    if hit_count1 == 6:
        building1 = pygame.image.load("building1_damaged.png")
        
    if hit_count2 == 6:
        building2 = pygame.image.load("building2_damaged.png")
        
    if hit_count3 == 6:
        building3 = pygame.image.load("building3_damaged.png")
        
    if hit_count1 == 8:
        building1 = pygame.image.load("building1_heavy.png")
        
    if hit_count2 == 8:
        building2 = pygame.image.load("building2_heavy.png")
        
    if hit_count3 == 8:
        building3 = pygame.image.load("building3_heavy.png")
        
    if hit_count1 >= 12:
        building1 = pygame.image.load("building1_destroyed.png")
        if george_y != 475:
            if george_x >= 134 and george_x <= 294:
                george_y += 0.08*frame_rate
        
    if hit_count2 >= 12:
        building2 = pygame.image.load("building2_destroyed.png")
        if george_y != 475:
            if george_x >= 326 and george_x <= 486:
                george_y += 0.08*frame_rate
        
            
    if hit_count3 >= 12:
        building3 = pygame.image.load("building3_destroyed.png")
        if george_y != 475:
            if george_x >= 614 and george_x <= 799:
                george_y += 0.08*frame_rate
        
        
    
    #4 tank
    # if hit_count1 >= 3:
    #     tank_x += 0.1*frame_rate
    
    #5 chopper 
    if chopper_x > 0 and chopper_x < 800:
        air_spawn = True
    else:
        air_spawn = False
    
    if air_spawn == False:
        if hit_count1 >= 3:
            if side_count == 1:
                chopper = chopper_r
                v_chopper = 0.05
            elif side_count == -1:
                chopper = chopper_l
                v_chopper = -0.05
            
    
    chopper_x += v_chopper*frame_rate
    
    if chopper_x < -150:
        side_count = 1
    if chopper_x > 801:
        side_count = -1
        
    #4.5 bullets
    
    #5 graphics
    screen.blit(background,(0,0))
    screen.blit(building1,(192,288))
    screen.blit(building2,(384,224))
    screen.blit(building3,(672,352))
    
    screen.blit(george_idle,(int(george_x),int(george_y)))
    screen.blit(tank,(int(tank_x),int(tank_y)))
    screen.blit(chopper,(int(chopper_x),int(chopper_y)))
    screen.blit(bullet1,(bullet_list[0][0],bullet_list[0][1]))
    screen.blit(bullet2,(bullet_list[1][0],bullet_list[1][1]))
    screen.blit(bullet3,(bullet_list[2][0],bullet_list[2][1]))
    screen.blit(bullet4,(bullet_list[3][0],bullet_list[3][1]))
    screen.blit(bullet5,(bullet_list[4][0],bullet_list[4][1]))
    screen.blit(bullet6,(bullet_list[5][0],bullet_list[5][1]))
    
    
    if chopper_x >= 75 and chopper_x <= 85:
        traj1 += 1
    if traj1 > 0:
        bullet1 = bullet
        bullet_list[0][0] += v_trigger*frame_rate
        bullet_list[0][1] += v_trigger*frame_rate
    if dist([george_x+30,george_y+35], [bullet_list [0][0],bullet_list[0][1]]) <= 30:
        bullet1 = transparent
        HP -= 10
        bullet_list[0] = [120,185]
    elif bullet_list[0][0] > 801 or bullet_list[0][1] > 601:
        traj1 = 0
        bullet1 = transparent
        bullet_list[0] = [120,185]
    
    if chopper_x >= 195 and chopper_x <= 205:
        traj2 += 1
    if traj2 > 0:
        bullet2 = bullet
        bullet_list[1][0] += v_trigger*frame_rate
        bullet_list[1][1] += v_trigger*frame_rate
    if dist([george_x+30,george_y+35], [bullet_list [1][0],bullet_list[1][1]]) <= 30:
        bullet2 = transparent
        HP -= 10
        bullet_list[1] = [240,185]
    elif bullet_list[1][0] > 801 or bullet_list[1][1] > 601:
        traj2 = 0
        bullet2 = transparent
        bullet_list[1] = [240,185]
            
    if chopper_x >= 315 and chopper_x <= 325:
        traj3 += 1
    if traj3 > 0:
        bullet3 = bullet
        bullet_list[2][0] += reverse_trigger*frame_rate
        bullet_list[2][1] += v_trigger*frame_rate
    if dist([george_x+30,george_y+35], [bullet_list [2][0],bullet_list[2][1]]) <= 30:
        bullet3 = transparent
        HP -= 10
        bullet_list[2] = [360,185]
    elif bullet_list[2][0] > 801 or bullet_list[2][1] > 601:
        traj3 = 0
        bullet3 = transparent
        bullet_list[2] = [360,185]
    
    if chopper_x >= 435 and chopper_x <= 445:
        traj4 += 1
    if traj4 > 0:
        bullet4 = bullet
        bullet_list[3][0] += v_trigger*frame_rate
        bullet_list[3][1] += v_trigger*frame_rate
    if dist([george_x+30,george_y+35], [bullet_list [3][0],bullet_list[3][1]]) <= 30:
        traj4 = 0
        bullet4 = transparent
        HP -= 10
        bullet_list[3] = [480,185]
    elif bullet_list[3][0] > 801 or bullet_list[3][1] > 601:
        traj4 = 0
        bullet4 = transparent
        bullet_list[3] = [480,185]
    
    if chopper_x >= 555 and chopper_x <= 565:
        traj5 += 1
    if traj5 > 0:
        bullet5 = bullet
        bullet_list[4][0] += reverse_trigger*frame_rate
        bullet_list[4][1] += v_trigger*frame_rate
    if dist([george_x+30,george_y+35], [bullet_list [4][0],bullet_list[4][1]]) <= 30:
        HP -= 10
        bullet_list[4] = [600,185]
        bullet5 = transparent
    elif bullet_list[4][0] > 801 or bullet_list[4][1] > 601:
        traj5 = 0
        bullet5 = transparent
        bullet_list[4] = [600,185]
    
    if chopper_x >= 675 and chopper_x <= 685:
        traj6 += 1
    if traj6 > 0:
        bullet6 = bullet
        bullet_list[5][0] += reverse_trigger*frame_rate
        bullet_list[5][1] += v_trigger*frame_rate
    if dist([george_x+30,george_y+35], [bullet_list [5][0],bullet_list[5][1]]) <= 30:
        HP -= 10
        bullet_list[5] = [720,185]
        bullet6 = transparent
    elif bullet_list[5][0] > 801 or bullet_list[5][1] > 601:
        traj6 = 0
        bullet6 = transparent
        bullet_list[5] = [720,185]

    
    pygame.display.flip()
    

    if v1 > 0 and george_y == 475:
        counter = 1
        george_idle = pygame.image.load("george_idle2.png")
    elif v1 < 0 and george_y == 475:
        counter = -1
        george_idle = pygame.image.load("george_idle.png")
    elif v2 != 0:
        for row in range(len(level1)):
            for column in range(len(level1[row])):
                if level1[row][column] == "2":
                    if george_x >= column*32-58 and george_x <= column*32+6:
                        george_idle = pygame.image.load("george_climb.png")
                elif level1[row][column] == "4":
                    if george_x >= column*32-58 and george_x <= column*32+6:
                        george_idle = pygame.image.load("george_climb2.png")


          
pygame.quit()

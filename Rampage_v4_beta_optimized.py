import pygame
import random

resolution = (800,600)
hitbox = 64
one_block = 32

hit_count1 = 0
hit_count2 = 0
hit_count3 = 0

pygame.init()

screen = pygame.display.set_mode(resolution)

background = pygame.image.load("city_v2.png")

b1_n = pygame.image.load("building1.png")
b1_u = pygame.image.load("building1_up.png")
b1_d = pygame.image.load("building1_down.png")
b1_da = pygame.image.load("building1_damaged.png")
b1_h = pygame.image.load("building1_heavy.png")
b1_de = pygame.image.load("building1_destroyed.png")

b2_n = pygame.image.load("building2.png")
b2_u = pygame.image.load("building2_up.png")
b2_d = pygame.image.load("building2_down.png")
b2_da = pygame.image.load("building2_damaged.png")
b2_h = pygame.image.load("building2_heavy.png")
b2_de = pygame.image.load("building2_destroyed.png")

b3_n = pygame.image.load("building3.png")
b3_u = pygame.image.load("building3_up.png")
b3_d = pygame.image.load("building3_down.png")
b3_da = pygame.image.load("building3_damaged.png")
b3_h = pygame.image.load("building3_heavy.png")
b3_de = pygame.image.load("building3_destroyed.png")

building1 = b1_n
building2 = b2_n
building3 = b3_n

pygame.display.flip()

george_right = pygame.image.load("george_idle2.png")
george_left = pygame.image.load("george_idle.png")
george_upl = pygame.image.load("george_climb2.png")
george_upr = pygame.image.load("george_climb.png")

george_idle = george_right

tank = pygame.image.load("tank.png")
chopper = pygame.image.load("helicopter.png")
bullet = pygame.image.load("bullet.png")

# great_ape = pygame.image.load("great_ape.png")
# assault_theme = pygame.mixer.music.load("Great Ape Assault.mp3")
# pygame.mixer.music.play(loops=-1)

george_x = 0
george_y = 475

tank_x = 0
tank_y = 550

chopper_x = -75
chopper_y = 160
v_chopper = 0

bullet_x = 100
bullet_y = 160
va = 0
vb = 0

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
        building1 = b1_d
    elif hit_count1 == 3 and b1_height == 1:
        building1 = b1_u
        
    if hit_count2 == 3 and b2_height == 0:
        building2 = b2_d
    elif hit_count2 == 3 and b2_height == 1:
        building2 = b2_u
        
    if hit_count3 == 3 and b3_height == 0:
        building3 = b3_d
    elif hit_count3 == 3 and b3_height == 1:
        building3 = b3_u
        
    if hit_count1 == 6:
        building1 = b1_da
        
    if hit_count2 == 6:
        building2 = b2_da
        
    if hit_count3 == 6:
        building3 = b3_da
        
    if hit_count1 == 8:
        building1 = b1_h
        
    if hit_count2 == 8:
        building2 = b2_h
        
    if hit_count3 == 8:
        building3 = b3_h
        
    if hit_count1 >= 12:
        building1 = b1_de
        if george_y != 475:
            if george_x >= 134 and george_x <= 294:
                george_y += 0.08*frame_rate
        
    if hit_count2 >= 12:
        building2 = b2_de
        if george_y != 475:
            if george_x >= 326 and george_x <= 486:
                george_y += 0.08*frame_rate
        
            
    if hit_count3 >= 12:
        building3 = b3_de
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
            v_chopper = 0.05
            va = 0.05
    
    chopper_x += v_chopper*frame_rate
    bullet_x += v_chopper*frame_rate
    bullet_y += va*frame_rate
    
    if chopper_x < -75:
        chopper_x = -75
        v_chopper = 0
    if chopper_x > 801:
        chopper_x = 801
        v_chopper = 0
    
    
    
    #5 graphics
    screen.blit(background,(0,0))
    screen.blit(building1,(192,288))
    screen.blit(building2,(384,224))
    screen.blit(building3,(672,352))
    
    screen.blit(george_idle,(int(george_x),int(george_y)))
    screen.blit(tank,(int(tank_x),int(tank_y)))
    screen.blit(chopper,(int(chopper_x),int(chopper_y)))
    # screen.blit(bullet,(bullet_x,bullet_y))
    pygame.display.flip()
    
    

    if v1 > 0 and george_y == 475:
        counter = 1
        george_idle = george_right
    elif v1 < 0 and george_y == 475:
        counter = -1
        george_idle = george_left
    elif v2 != 0:
        for row in range(len(level1)):
            for column in range(len(level1[row])):
                if level1[row][column] == "2":
                    if george_x >= column*32-58 and george_x <= column*32+6:
                        george_idle = george_upr
                elif level1[row][column] == "4":
                    if george_x >= column*32-58 and george_x <= column*32+6:
                        george_idle = george_upl


          
pygame.quit()
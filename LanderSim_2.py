"""
LanderSim 2.0

Description:
"""

# IMPORT
import gameapp, random
def GAME():
    # WINDOW & BACKGROUND
    window = tsapp.GraphicsWindow(1344, 2292, tsapp.CYAN)
    ground = tsapp.Sprite("EarthLayer.png", 0, 0)
    ground.scale = 1.32
    ground.y = window.height - ground.height
    ground.x = 0
    window.add_object(ground)

    # MAIN VARIABLES
    GRAVITY = 9.1
    capsule = tsapp.Sprite("SpaceCapsule.png", window.center_x, 0, 0.40)
    capsule_fire = tsapp.Sprite("FireBig.png", capsule.x-10, capsule.y-10, 0.6)
    capsule_fire.center = capsule.center
    window.add_object(capsule_fire)
    window.add_object(capsule)
    death = 0

    # GENERATE CLOUDS
    clouds = []
    for y in range(0, 1600, 100):
        cloud = tsapp.Sprite(random.choice(["Cloud4.png", "Cloud5.png"]), random.randint(10, 1100), y)
        clouds.append(cloud)
    
    # ADD CLOUDS
    for cloud in clouds:
        window.add_object(cloud)

    # START TEXT
    text = tsapp.TextLabel("Parisienne-Regular.ttf", 160, 0, 320, 1344, "Welcome to LanderSim", tsapp.RED)
    text.align = "center"
    window.add_object(text)

    # WAIT TO START
    while not tsapp.was_key_pressed(tsapp.K_SPACE) and window.is_running:
        window.finish_frame()
    
    # MAIN LOOP
    while window.is_running:
        capsule.y_speed += GRAVITY
        capsule_fire.center = capsule.center
    
        # LAND/CRASH
        if capsule.is_colliding_rect(ground):
            if capsule.y_speed >= 200:
                death = True
                capsule.image = "ExplosionSheet.png"
                start = tsapp.get_program_duration()
                capsule_fire.destroy()
                capsule.y_speed = 0
                break
            else:
                capsule_fire.destroy
                break
                death = False
            
    
        # INTERACTION
        if tsapp.is_key_down(tsapp.K_w) or tsapp.is_key_down(tsapp.K_UP) or tsapp.is_key_down(tsapp.K_SPACE):
            capsule.y_speed -= 10
        
        if tsapp.is_key_down(tsapp.K_a) or tsapp.is_key_down(tsapp.K_LEFT):
            capsule.y_speed -= 5
            capsule.x_speed -= 5
            capsule.angle -= 2
    
        if tsapp.is_key_down(tsapp.K_d) or tsapp.is_key_down(tsapp.K_RIGHT):
            capsule.y_speed -= 5
            capsule.x_speed += 5
            capsule.angle += 2
        
        if tsapp.is_key_down(tsapp.K_s) or tsapp.is_key_down(tsapp.K_DOWN):
            capsule.y_speed += 10
        
        # Go to other side
        if capsule.x <= 0:
            capsule.x = 1300 - capsule.width
    
        elif capsule.x >=  1344 - capsule.width:
            capsule.x = 44
    
        window.finish_frame()

    # ANNIHILATE
    if death:
        capsule.image = "ExplosionSheet.png"
        capsule.scale = 10
        capsule_fire.destroy()
        window.finish_frame()
        text.text = "Congrats, you have annihilated the entire world!"
        text.font_size = 100
        ground.destroy()
        for cloud in clouds:
            cloud.destroy()
        window.background_color = tsapp.BLACK
        
        while tsapp.get_program_duration() - start <= 900 and window.is_running:
            window.finish_frame()
        
        capsule.destroy()
    
    else:
        text.text = "You Won!!!"
        capsule.image = "AstronautStand.png"
        capsule.y_speed = 0
        capsule_fire.destroy()

    while window.is_running:
        window.finish_frame()
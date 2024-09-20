import pgzrun
import random

FONT_OPTION=(255, 255, 255)
WIDTH=800
HEIGHT=600

CENTER_X =WIDTH/2
CENTER_Y =HEIGHT/2

CENTER= (CENTER_X, CENTER_Y)

FINAL_LEVEL = 6
START_SPEED = 10

ITEMS = ["testegg", "egg3", "egg4", "egg5"]

game_over=False
game_complete=False

current_level = 1

items=[]
animations=[]

def draw():
    global items, current_level, game_complete, game_over
    screen.clear()
    screen.blit("bground", (0, 0))
    if game_over:
        display_message("GAME OVER", "TRY AGAIN")
    elif game_complete:
        display_message("YOU WIN", "WELL DONE")
    else:
        for item in items:
            item.draw()

def display_message(heading, subheading):
    screen.draw.text(heading, fontsize=60, center=CENTER, color="RED")
    screen.draw.text(subheading, fontsize=30, center=(CENTER_X, CENTER_Y+30), color="RED")

def update():
    global items
    if len(items) == 0:
        items=make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create= get_option_to_create(number_of_extra_items)
    new_items=create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(number_of_extra_items):
    items_to_create=["egg"]
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item = Actor(option+"img")
        new_items.append(item)
    return new_items


def layout_items(item_to_layout):
    number_of_gaps =len(item_to_layout) + 1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(item_to_layout)
    for index, item in enumerate(item_to_layout):
        new_x_pos = (index+1) * gap_size
        item.x = new_x_pos

def animate_items(item_to_animate):
    global animations
    for i in item_to_animate:
        duration = START_SPEED - current_level
        i.anchor=("center", "bottom")
        animation = animate(i, duration=duration,on_finished=handle_game_over,y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "egg" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_level,items, animations,game_complete
    stop_animations(animations)
    if current_level==FINAL_LEVEL:
        game_complete=True
    else:
        current_level += 1
        items=[]
        animations=[]
    
def stop_animations(animate_to_stop):
    for animation in animate_to_stop:
        if animation.running:
            animation.stop()

pgzrun.go()
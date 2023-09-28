from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

tur_ground = load_image('TUK_GROUND.png')

character = load_image('pokemon.png')

def handle_events():
    global moving, xdir, ydir
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            moving = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                moving = False
            elif event.key == SDLK_LEFT:
                xdir -= 1
            elif event.key == SDLK_RIGHT:
                xdir += 1
            elif event.key == SDLK_UP:
                ydir += 1
            elif event.key == SDLK_DOWN:
                ydir -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                xdir += 1
            elif event.key == SDLK_RIGHT:
                xdir -= 1
            elif event.key == SDLK_UP:
                ydir -= 1
            elif event.key == SDLK_DOWN:
                ydir += 1

moving = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
xdir, ydir = 0, 0
xidleframe, xidle = 142, 0
yidleframe, yidle = 267, 0

while moving:
    clear_canvas()
    tur_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    x += xdir * 5
    y += ydir * 5

    # Idle 상태
    if 0 == xdir and 0 == ydir:
        if 0 <= xidle % 15 and 4 >= xidle % 15:
            character.clip_draw(142, 267, 40, 42, x, y, 150, 150)

        elif 5 <= xidle % 15 and 9 >= xidle % 15:
            character.clip_draw(183, 267, 65, 37, x, y, 250, 150)

        elif 10 <= xidle % 15 and 14 >= xidle % 15:
            character.clip_draw(249, 267, 39, 43, x, y, 150, 150)

        xidle += 1

    # Left 상태
    elif -1 == xdir and 0 == ydir:
        if 0 <= xidle % 15 and 4 >= xidle % 15:
            character.clip_draw(123, 157, 59, 52, x, y, 250, 150)

        elif 5 <= xidle % 15 and 9 >= xidle % 15:
            character.clip_draw(183, 157, 60, 39, x, y, 250, 150)

        elif 10 <= xidle % 15 and 14 >= xidle % 15:
            character.clip_draw(243, 157, 60, 40, x, y, 250, 150)

        xidle += 1

    # Right 상태
    elif 1 == xdir and 0 == ydir:
        if 0 <= xidle % 15 and 4 >= xidle % 15:
            character.clip_draw(123, 157, 59, 52, x, y, 250, 150)

        elif 5 <= xidle % 15 and 9 >= xidle % 15:
            character.clip_draw(183, 157, 60, 39, x, y, 250, 150)

        elif 10 <= xidle % 15 and 14 >= xidle % 15:
            character.clip_draw(243, 157, 60, 40, x, y, 250, 150)

        xidle += 1

    # Up 상태
    elif 0 == xdir and 1 == ydir:
        if 0 <= xidle % 15 and 4 >= xidle % 15:
            character.clip_draw(123, 157, 59, 52, x, y, 250, 150)

        elif 5 <= xidle % 15 and 9 >= xidle % 15:
            character.clip_draw(183, 157, 60, 39, x, y, 250, 150)

        elif 10 <= xidle % 15 and 14 >= xidle % 15:
            character.clip_draw(243, 157, 60, 40, x, y, 250, 150)

        xidle += 1

    # Down 상태
    elif 0 == xdir and -1 == ydir:
        if 0 <= xidle % 15 and 4 >= xidle % 15:
            character.clip_draw(123, 157, 59, 52, x, y, 250, 150)

        elif 5 <= xidle % 15 and 9 >= xidle % 15:
            character.clip_draw(183, 157, 60, 39, x, y, 250, 150)

        elif 10 <= xidle % 15 and 14 >= xidle % 15:
            character.clip_draw(243, 157, 60, 40, x, y, 250, 150)

        xidle += 1




    update_canvas()
    handle_events()

    delay(0.02)
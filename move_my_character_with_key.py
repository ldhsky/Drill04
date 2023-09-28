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

while moving:
    clear_canvas()
    tur_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(30, 56, 50, 50, x, y, 150, 150)

    update_canvas()
    handle_events()

    delay(0.05)
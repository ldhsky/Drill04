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
frame = 0
pi = 3.141592653589793

while moving:
    clear_canvas()
    tur_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    x += xdir * 5
    y += ydir * 5

    if 115 >= x:
        x += 5
    if 1165 <= x:
        x -= 5
    if 115 >= y:
        y += 5
    if 919 <= y:
        y -= 5

    # Idle 상태
    if 0 == xdir and 0 == ydir:
        if 0 <= frame % 15 and 4 >= frame % 15:
            character.clip_draw(142, 267, 40, 42, x, y, 150, 150)

        elif 5 <= frame % 15 and 9 >= frame % 15:
            character.clip_draw(183, 267, 65, 37, x, y, 250, 150)

        elif 10 <= frame % 15 and 14 >= frame % 15:
            character.clip_draw(249, 267, 39, 43, x, y, 150, 150)


    # LeftTop 상태
    elif -1 == xdir and 1 == ydir:
        if 0 <= frame % 15 and 4 >= frame % 15:
            character.clip_draw(139, 56, 50, 55, x, y, 150, 150)

        elif 5 <= frame % 15 and 9 >= frame % 15:
            character.clip_draw(190, 56, 54, 47, x, y, 150, 150)

        elif 10 <= frame % 15 and 14 >= frame % 15:
            character.clip_draw(245, 56, 49, 43, x, y, 150, 150)


    # LeftBottom 상태
    elif -1 == xdir and -1 == ydir:
        if 0 <= frame % 15 and 4 >= frame % 15:
            character.clip_draw(146, 112, 42, 45, x, y, 150, 150)

        elif 5 <= frame % 15 and 9 >= frame % 15:
            character.clip_draw(189, 112, 47, 36, x, y, 150, 150)

        elif 10 <= frame % 15 and 14 >= frame % 15:
            character.clip_draw(236, 112, 50, 39, x, y, 150, 150)


    # RightTop 상태
    elif 1 == xdir and 1 == ydir:
        if 0 <= frame % 15 and 4 >= frame % 15:
            character.clip_composite_draw(139, 56, 50, 55, 0, 'h', x, y, 150, 150)

        elif 5 <= frame % 15 and 9 >= frame % 15:
            character.clip_composite_draw(190, 56, 54, 47, 0, 'h', x, y, 150, 150)

        elif 10 <= frame % 15 and 14 >= frame % 15:
            character.clip_composite_draw(245, 56, 49, 43, 0, 'h', x, y, 150, 150)


    # RightBottom 상태
    elif 1 == xdir and -1 == ydir:
        if 0 <= frame % 15 and 4 >= frame % 15:
            character.clip_composite_draw(146, 112, 42, 45, 0, 'h', x, y, 150, 150)

        elif 5 <= frame % 15 and 9 >= frame % 15:
            character.clip_composite_draw(189, 112, 47, 36, 0, 'h', x, y, 150, 150)

        elif 10 <= frame % 15 and 14 >= frame % 15:
            character.clip_composite_draw(236, 112, 50, 39, 0, 'h', x, y, 150, 150)


    # Left 상태
    elif -1 == xdir and 0 == ydir:
        if 0 <= frame % 15 and 4 >= frame % 15:
            character.clip_draw(123, 157, 59, 52, x, y, 250, 150)

        elif 5 <= frame % 15 and 9 >= frame % 15:
            character.clip_draw(183, 157, 60, 39, x, y, 250, 150)

        elif 10 <= frame % 15 and 14 >= frame % 15:
            character.clip_draw(243, 157, 60, 40, x, y, 250, 150)


    # Right 상태
    elif 1 == xdir and 0 == ydir:
        if 0 <= frame % 15 and 4 >= frame % 15:
            character.clip_composite_draw(123, 157, 59, 52, 0, 'h', x, y, 250, 150)

        elif 5 <= frame % 15 and 9 >= frame % 15:
            character.clip_composite_draw(183, 157, 60, 39, 0, 'h', x, y, 250, 150)

        elif 10 <= frame % 15 and 14 >= frame % 15:
            character.clip_composite_draw(243, 157, 60, 40, 0, 'h', x, y, 250, 150)


    # Up 상태
    elif 0 == xdir and 1 == ydir:
        if 0 <= frame % 15 and 4 >= frame % 15:
            character.clip_draw(145, 209, 43, 57, x, y, 130, 200)

        elif 5 <= frame % 15 and 9 >= frame % 15:
            character.clip_draw(189, 209, 64, 46, x, y, 200, 150)

        elif 10 <= frame % 15 and 14 >= frame % 15:
            character.clip_draw(253, 209, 33, 46, x, y, 100, 150)


    # Down 상태
    elif 0 == xdir and -1 == ydir:
        if 0 <= frame % 15 and 4 >= frame % 15:
            character.clip_composite_draw(145, 209, 43, 57, pi, 'h', x, y, 130, 200)

        elif 5 <= frame % 15 and 9 >= frame % 15:
            character.clip_composite_draw(189, 209, 64, 46, pi, 'h', x, y, 200, 150)

        elif 10 <= frame % 15 and 14 >= frame % 15:
            character.clip_composite_draw(253, 209, 33, 46, pi, 'h', x, y, 100, 150)

    frame += 1

    update_canvas()
    handle_events()

    delay(0.02)
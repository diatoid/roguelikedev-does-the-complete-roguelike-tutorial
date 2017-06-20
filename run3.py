#!/usr/bin/env python3

import tdl

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

def handle_keys():
    global playerx, playery
    # Turn based
    # key = tdl.event.key_wait()
    # Realtime
    keypress = False
    for event in tdl.event.get():
        if event.type == 'KEYDOWN':
            key = event
            keypress = True
    if not keypress:
        return
        
    if key.key == 'ENTER' and key.alt:
        tdl.set_fullscreen(not tdl.get_fullscreen())
 
    elif key.key == 'ESCAPE':
        return True
 
    if key.key == 'UP':
        playery -= 1
    if key.key == 'DOWN':
        playery += 1
    if key.key == 'LEFT':
        playerx -= 1
    if key.key == 'RIGHT':
        playerx += 1

tdl.set_font('./arial10x10.png', greyscale=True, altLayout=True)
console = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT, title='Roguelike Tutorial', fullscreen=False)
tdl.setFPS(LIMIT_FPS)

playerx = SCREEN_WIDTH//2
playery = SCREEN_HEIGHT//2

while not tdl.event.is_window_closed():
    console.draw_char(playerx, playery, '@', bg=None, fg=(255,255,255))
    tdl.flush()
    console.draw_char(playerx, playery, ' ', bg=None)

    exit = handle_keys()
    if exit:
        break



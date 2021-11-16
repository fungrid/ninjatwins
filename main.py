def on_button_pressed_a():
    global J2, State
    if State == 0:
        prep()
    elif State == 1:
        J2 = 2
    else:
        led.stop_animation()
        State = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def gameOver():
    global State
    State = 2

def on_button_pressed_b():
    global J1, State
    if State == 0:
        prep()
    elif State == 1:
        J1 = 2
    else:
        led.stop_animation()
        State = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def prep():
    global N1X, N1Y, N2X, N2Y, OX, SCORE, State
    led.stop_animation()
    N1X = 1
    N1Y = 4
    N2X = 0
    N2Y = 4
    OX = 8
    SCORE = 0
    State = 1
SCORE = 0
OX = 0
N2Y = 0
N2X = 0
N1Y = 0
N1X = 0
J1 = 0
J2 = 0
State = 0
State = 0

def on_every_interval():
    global N1Y, N2Y, OX, SCORE, J1, J2
    if State == 1:
        led.unplot(N1X, N1Y)
        led.unplot(N2X, N2Y)
        N1Y = N1Y - J1
        N2Y = N2Y - J2
        if N1X != OX:
            N1Y += 1
        if N1Y > 4:
            N1Y = 4
        if N2X != OX:
            N2Y += 1
        if N2Y > 4:
            N2Y = 4
        led.plot(N1X, N1Y)
        led.plot(N2X, N2Y)
        led.unplot(OX, 4)
        OX += -1
        if OX == 5:
            led.plot_brightness(4, 4, 8)
        led.plot_brightness(OX, 4, 128)
        if OX == 1:
            if N1Y < 4:
                SCORE += 1
            else:
                gameOver()
        if OX == 0:
            if N2Y < 4:
                SCORE += 1
            else:
                gameOver()
        if OX == -1:
            OX = 8
        J1 = 0
        J2 = 0
loops.every_interval(500, on_every_interval)

def on_forever():
    if State == 0:
        basic.show_string("NinjaTwins TheLast")
    elif State == 1:
        pass
    else:
        basic.show_string("" + str((SCORE)))
basic.forever(on_forever)

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pass
input.on_button_pressed(Button.B, on_button_pressed_b)

N1X = 2
N1Y = 4
N2X = 0
N2Y = 4

def on_every_interval():
    global N1Y, N2Y
    led.plot(N1X, N1Y)
    led.plot(N2X, N2Y)
    N1Y += 1
    N2Y += 1
    led.plot_brightness(4, 0, 128)
loops.every_interval(500, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)

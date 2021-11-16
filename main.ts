input.onButtonPressed(Button.A, function () {
    J2 = 2
})
function gameOver () {
    basic.showString("" + (SCORE))
}
input.onButtonPressed(Button.B, function () {
    J1 = 2
})
function prep () {
    N1X = 1
    N1Y = 4
    N2X = 0
    N2Y = 4
    OX = 8
    SCORE = 0
}
let OX = 0
let N2Y = 0
let N2X = 0
let N1Y = 0
let N1X = 0
let J1 = 0
let SCORE = 0
let J2 = 0
prep()
loops.everyInterval(500, function () {
    led.unplot(N1X, N1Y)
    led.unplot(N2X, N2Y)
    N1Y = N1Y - J1
    N2Y = N2Y - J2
    N1Y += 1
    if (N1Y > 4) {
        N1Y = 4
    }
    N2Y += 1
    if (N2Y > 4) {
        N2Y = 4
    }
    led.plot(N1X, N1Y)
    led.plot(N2X, N2Y)
    led.unplot(OX, 4)
    OX += -1
    if (OX == 5) {
        led.plotBrightness(4, 4, 8)
    }
    led.plotBrightness(OX, 4, 128)
    if (OX == 1) {
        if (N1Y < 4) {
            SCORE += 1
        } else {
            gameOver()
        }
    }
    if (OX == 0) {
        if (N2Y < 4) {
            SCORE += 1
        } else {
            gameOver()
        }
    }
    if (OX == -1) {
        OX = 8
    }
    J1 = 0
    J2 = 0
})
basic.forever(function () {
	
})

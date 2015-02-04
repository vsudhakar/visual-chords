#constants
SCREEN_SIZE=(1280,1024)
WIDTH=SCREEN_SIZE[0]
HEIGHT=SCREEN_SIZE[1]
KEYS={
    "K_q":0,
    "K_2":1,
    "K_w":2,
    "K_3":3,
    "K_e":4,
    "K_r":5,
    "K_5":6,
    "K_t":7,
    "K_6":8,
    "K_y":9,
    "K_7":10,
    "K_u":11,
    "K_i":12,
    "K_9":13,
    "K_o":14,
    "K_0":15,
    "K_p":16,
    "K_LEFTBRACKET":17,
    "K_EQUALS":18,
    "K_RIGHTBRACKET":19
}

COLORS={
    0:(255, 0, 0),
    1:(255, 127, 0),
    2:(255, 255, 0),
    3:(127, 255, 0),
    4:(0, 255, 0),
    5:(0, 255, 127),
    6:(0, 255, 255),
    7:(0, 127, 255),
    8:(0, 0, 255),
    9:(127, 0, 255),
    10:(255, 0, 255),
    11:(255, 0, 127)
}

def COLOR(n, mod=0):
    if mod==0:
        return COLORS[n%12]

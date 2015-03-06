#constants
from ctypes import windll as wd
SCREEN_SIZE=(wd.user32.GetSystemMetrics(0),wd.user32.GetSystemMetrics(1))
WIDTH=SCREEN_SIZE[0]
HEIGHT=SCREEN_SIZE[1]
KEYS={
    113:0,
    50:1,
    119:2,
    51:3,
    101:4,
    114:5,
    53:6,
    116:7,
    54:8,
    121:9,
    55:10,
    117:11,
    105:12,
    57:13,
    111:14,
    48:15,
    112:16,
    91:17,
    61:18,
    93:19
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

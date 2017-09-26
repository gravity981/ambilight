from tkinter import *
from tkinter.colorchooser import *
from requests import post

HOST = 'amlipi'
PORT = '5000'
AMBILIGHT_SERVICE = 'ambilight'
COLOR_RESOURCE = 'color'


def getUrl(host=HOST, port=PORT, service=AMBILIGHT_SERVICE, resource=COLOR_RESOURCE):
    return str('http://%s:%s/%s/%s' % (host, port, service, resource))

def sendColor(r, g, b):
    resp = post(getUrl(), json={"r": r, "g": g, "b": b})
    print(str(resp))

def pickColor():
    rgb, hec = askcolor()
    print(rgb)
    sendColor(int(rgb[0]), int(rgb[1]), int(rgb[2]))

root = Tk()
root.title('AmbiLight Client')
frame = Frame(root, width=320).pack()
Button(frame, text='Pick Color', command=pickColor).pack(fill=X)
Button(frame, text='Red', command=lambda: sendColor(255,0,0)).pack(fill=X)
Button(frame, text='Green', command=lambda: sendColor(0,255,0)).pack(fill=X)
Button(frame, text='Blue', command=lambda: sendColor(0,0,255)).pack(fill=X)
Button(frame, text='White', command=lambda: sendColor(255,255,255)).pack(fill=X)
Button(frame, text='Black', command=lambda: sendColor(0,0,0)).pack(fill=X)
root.mainloop()

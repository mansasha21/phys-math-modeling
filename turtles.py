# -*- coding: utf-8 -*-
"""turtles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wl6WD8ntb-XqJEb1m4CfYfHvWXR-99ok
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
import matplotlib
import random

matplotlib.rcParams["animation.embed_limit"] = 75

N = 4
R = 30
v = 2
vx = 0.03
frames = 1500
dt = 1

class finish:
    finished = False
    real_time = frames

fig, ax = plt.subplots()
ax = plt.axis([-40, 40, -40, 40])
tracks = []
dots = []
curr_coord = [
    [R * np.cos((2 * np.pi * i) / N), R * np.sin((2 * np.pi * i) / N)] for i in range(N)
]

rand_coord = [
    [random.random()*R, random.random()*R] for i in range(N)
]

curr_coord1 = [list(i) for i in curr_coord]

#curr_coord = rand_coord
#curr_coord1 = [list(i) for i in rand_coord]

for x, y in curr_coord:
    (dot,) = plt.plot([x], [y], "o")
    dots.append(dot)
    tracks.append([x])
    tracks.append([y])

for i in range(frames):
    x,y = 0, 0
    for k in range(N):
        if k != N - 1:
            x = curr_coord1[k + 1][0] - curr_coord1[k][0]
            y = curr_coord1[k + 1][1] - curr_coord1[k][1]
        else:
            x = curr_coord1[0][0] - curr_coord1[k][0]
            y = curr_coord1[0][1] - curr_coord1[k][1]
        norm = np.linalg.norm([x, y])
        curr_coord1[k][0] += x / norm * vx * dt
        curr_coord1[k][1] += y / norm * vx * dt
        tracks[2 * k].append(curr_coord1[k][0])
        tracks[2 * k + 1].append(curr_coord1[k][1])

for i in range(N):
    plt.plot(tracks[2 * i], tracks[2 * i + 1])




def animate(i):

    if i % 100 == 0:
      print("{}% prepared".format(1.*i/frames)) 
    for k, dot in zip(range(N), dots):
        curr_coord[k][0] = tracks[2 * k][i]
        curr_coord[k][1] = tracks[2 * k + 1][i]
        dot.set_data(curr_coord[k][0], curr_coord[k][1])
    if round(curr_coord[0][0],1) == round(curr_coord[1][0],1) and round(curr_coord[0][1],1) == round(curr_coord[1][1],1) and not finish.finished:
      finish.finished = True
      finish.real_time = i
    return dots

myAnimation = animation.FuncAnimation(
    fig, animate, frames=frames, blit=True, repeat=False
)

HTML(myAnimation.to_jshtml(embed_frames=frames))

print('real_time = ',finish.real_time)
theor_time = R/(vx*np.sin(np.pi/N))
print('theor_time = ',theor_time)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
import matplotlib
import random

matplotlib.rcParams["animation.embed_limit"] = 75

N = 6
R = 30
v = 2
vx = 0.03
frames = 2500
dt = 1

class finish:
    finished = False
    real_time = frames

fig, ax = plt.subplots()
ax = plt.axis([-40, 40, -40, 40])
tracks = []
dots = []
curr_coord = [
    [R * np.cos((2 * np.pi * i) / N), R * np.sin((2 * np.pi * i) / N)] for i in range(N)
]

rand_coord = [
    [random.random()*R, random.random()*R] for i in range(N)
]

curr_coord1 = [list(i) for i in curr_coord]

#curr_coord = rand_coord
#curr_coord1 = [list(i) for i in rand_coord]

for x, y in curr_coord:
    (dot,) = plt.plot([x], [y], "o")
    dots.append(dot)
    tracks.append([x])
    tracks.append([y])

for i in range(frames):
    x,y = 0, 0
    for k in range(N):
        if k != N - 1:
            x = curr_coord1[k + 1][0] - curr_coord1[k][0]
            y = curr_coord1[k + 1][1] - curr_coord1[k][1]
        else:
            x = curr_coord1[0][0] - curr_coord1[k][0]
            y = curr_coord1[0][1] - curr_coord1[k][1]
        norm = np.linalg.norm([x, y])
        curr_coord1[k][0] += x / norm * vx * dt
        curr_coord1[k][1] += y / norm * vx * dt
        tracks[2 * k].append(curr_coord1[k][0])
        tracks[2 * k + 1].append(curr_coord1[k][1])

for i in range(N):
    plt.plot(tracks[2 * i], tracks[2 * i + 1])




def animate(i):

    if i % 100 == 0:
      print("{}% prepared".format(1.*i/frames)) 
    for k, dot in zip(range(N), dots):
        curr_coord[k][0] = tracks[2 * k][i]
        curr_coord[k][1] = tracks[2 * k + 1][i]
        dot.set_data(curr_coord[k][0], curr_coord[k][1])
    if round(curr_coord[0][0],1) == round(curr_coord[1][0],1) and round(curr_coord[0][1],1) == round(curr_coord[1][1],1) and not finish.finished:
      finish.finished = True
      finish.real_time = i
    return dots

myAnimation = animation.FuncAnimation(
    fig, animate, frames=frames, blit=True, repeat=False
)

HTML(myAnimation.to_jshtml(embed_frames=frames))

print('real_time = ',finish.real_time)
theor_time = R/(vx*np.sin(np.pi/N))
print('theor_time = ',theor_time)

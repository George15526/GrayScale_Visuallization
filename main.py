import matplotlib.pyplot as plt
import numpy as np

R = 0
G = 0
B = 0

plt.ion()
plt.subplots()

while(R<256 and G<256 and B<256):
    R += 5
    G += 5
    B += 5
    
    plt.clf()
    ax = plt.axes()
    ax.set(facecolor=(R/255, G/255, B/255))
    
    plt.pause(0.2)
    
plt.ioff()
plt.show()
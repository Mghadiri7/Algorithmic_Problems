#!/usr/bin/env python
# coding: utf-8

# ## Traveling Salesman

# ### Importing Dependencies

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import cv2
from random import randint as rnd
from random import shuffle


# ### Setting the Problem Parameters

# In[2]:


N_Cities = 4
Area_Width = 500
Area_Hight = 500


# ### City Randomizer Function

# In[3]:


def city_randomizer(n, w, h):
    offset = 20
    city_list = []
    for i in range(n):
        x = rnd(offset, w-offset)
        y = rnd(offset, h-offset)
        city_list.append([x, y])
    return city_list


# ### Draw Cities Function

# In[4]:


def draw_cities(img, location_list, color):
    for city in location_list:
        img = cv2.circle(img, city, 10, color, -1)
    return img


# ### Random Path Function

# In[5]:


def random_path(location_list):
    shuffle(location_list)
    return location_list


# ### Euclidean Distance Function

# In[6]:


def distance(path):
    dis = 0
    for i in range(len(path)-1):
        dis += np.sqrt((path[i][0]-path[i+1][0])**2 + (path[i][1]-path[i+1][1])**2)
    return dis


# ### Draw Path Function

# In[9]:


def draw_path(img, path, color):
    for i in range(len(path)-1):
        img = cv2.line(img, path[i], path[i+1], color, 2)
    return img


# ### Main

# In[ ]:


area = np.full((Area_Width, Area_Hight, 3), 255, np.uint8)
cities_locations = city_randomizer(N_Cities, Area_Width, Area_Hight)
best_distance = None
best_path = []
counter = 0
while True:
    area = np.full((Area_Width, Area_Hight, 3), 255, np.uint8)
    area = draw_cities(area, cities_locations, (11, 152, 200))
    path = random_path(cities_locations)
    area = draw_path(area, path, (26, 32, 40))
    d = distance(path)
    if best_distance != None:
        if d<best_distance:
            best_distance = d
            best_path = path.copy()
    else:
        best_distance = d
        best_path = path.copy()
    area = draw_path(area, best_path, (255, 87, 52))
    counter+=1
    
    plt.imshow(area)
    plt.title(f"Best Distance so far: {best_distance}")
    plt.xlabel(str(counter))
    plt.grid()
    plt.pause(0.005)
    plt.clf()
plt.imshow(area)
plt.title(f"Best Distance so far: {best_distance}")
plt.xlabel(str(counter))
plt.grid()
plt.show()


# In[ ]:





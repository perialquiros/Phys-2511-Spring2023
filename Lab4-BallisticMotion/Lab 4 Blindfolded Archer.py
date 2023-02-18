#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[17]:


'''
UNITS
DISTANCE - METERS
MASS - KILOGRAMS
TIME - SECONDS
FORCE - NEWTONS
'''
import math as mt

arrowMass = 3
x_init = 0
y_init = 1.5
g_const = -9.8
del_t = 0.0001
target = 25
air_density = 1.3
arrowDrag = 0.52
csectionArea = 0.0079
print("The arrow's mass is " + str(arrowMass) + " kg.")
print("Your initial height " + str(y_init) + " m.")

def shortenFloat (num=float):
    floatAsString = str(num)
    shortenedFloat = float(floatAsString[0:6])
    return shortenedFloat

def takeInputs():

    inputted = False
    while inputted is False:
        magInput = input("What is the velocity's initial magnitude?\n")
        try:
            magInput = float(magInput)
            inputted = True
        except (ValueError, TypeError):
            print("Please try typing a number.")
            
    inputted = False
    while inputted is False:
        angleInput = input("What is the velocity's initial angle in degrees?\n")
        try:
            angleInput = float(angleInput)
            inputted = True
        except (ValueError, TypeError):
            print("Please try typing a number.")


    velX = magInput * mt.cos(mt.radians(angleInput))
    velY = magInput * mt.sin(mt.radians(angleInput))

    '''print("X velocity: " + str(velX))
    print("Y velocity: " + str(velY))'''
    
    return [float(velX), float(velY)]

def simulateTrajectory(velocities, analyzedX):
    
    x = x_init
    y = y_init
    time = 0
    vX_sim = float(velocities[0])
    v_Y = float(velocities[1])
    
    while y > 0:
        v = mt.atan(v_Y/vX_sim)
        airResistX = (air_density * vX_sim * vX_sim * arrowDrag * csectionArea)/(2 * arrowMass)
        vX_sim -= airResistX * del_t
        x += vX_sim * del_t
        v_Y += (g_const * del_t)
        y += v_Y * del_t
        time += del_t
        
    distanceFromTarget = abs(x - target)
    print("The arrow landed " + str(shortenFloat(x)) + " meters away from you.")
    print("Theoretical distance from you: " + str(analyzedX))
    print("Difference between theoretical and simulated outcomes: " + str(analyzedX - x))
    if distanceFromTarget < 0.5:
        print("Nice shot! You hit the target.")
    else:
        distanceFromCloserSide = distanceFromTarget - 0.5
        print("So close! The arrow landed " + str(shortenFloat(distanceFromCloserSide)) + " meters away. Try again.")
        simulateTrajectory(takeInputs(), analyzedX)


def analyzeTrajectory(velocities):
    v_X = velocities[0]
    v_Y = velocities[1]
    
    t_1 = (-v_Y + mt.sqrt((v_Y*v_Y) + (2*g_const*y_init)))/(g_const)
    t_2 = (-v_Y - mt.sqrt((v_Y*v_Y) + (2*g_const*y_init)))/(g_const)
    time = max(t_1, t_2)
    x = v_X * time
    return x
           
velInputs = takeInputs()
simulateTrajectory(velInputs, analyzeTrajectory(velInputs))


# 

# In[ ]:





# In[ ]:





import math

def projectilemotion_solver(speed, angle):
    g = 9.81
    
    theta = math.radians(angle)
    
    range_x = (speed **2) * math.sin (2 * theta) / g
    
    max_height = (speed **2) * (math.sin(theta) **2) / (2*g)
    
    return range_x, max_height
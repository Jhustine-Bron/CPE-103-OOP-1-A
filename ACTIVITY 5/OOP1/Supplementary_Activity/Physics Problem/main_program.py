import projectilemotion

speed = 11
angle = 20

range_x, max_height = projectilemotion.projectilemotion_solver(speed, angle)

print (f"Horizontal Distance (Range): {range_x:.2f} m")
print (f"Maximum Height: {max_height:.2f} m")
# main.py

# Different importing statements

# Selective import of modules
from graphics.rectangle import area as rect_area, perimeter as rect_perimeter
from graphics.circle import area as circle_area, perimeter as circle_perimeter

# Importing entire modules
import graphics.graphics_3D.cuboid as cuboid
import graphics.graphics_3D.sphere as sphere

# Importing everything using *
from graphics.circle import *

# Example usage
length = 5
width = 3
radius = 4
height = 6

# Using selectively imported modules
print("Rectangle Area:", rect_area(length, width))
print("Rectangle Perimeter:", rect_perimeter(length, width))
print()
print("Circle Area:", circle_area(radius))
print("Circle Perimeter:", circle_perimeter(radius))
print()
# Using imported entire modules
print("Cuboid Surface Area:", cuboid.surface_area(length, width, height))
print("Cuboid Volume:", cuboid.volume(length, width, height))
print()
print("Sphere Surface Area:", sphere.surface_area(radius))
print("Sphere Volume:", sphere.volume(radius))
print()
# Using * import
print("Circle Area (Using * import):", area(radius))
print("Circle Perimeter (Using * import):", perimeter(radius))

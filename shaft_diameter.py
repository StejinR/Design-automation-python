import math

def shaft_diameter(power_kw, speed_rpm, shear_stress_mpa):
    torque = (9550 * power_kw) / speed_rpm
    diameter = ((16 * torque * 1000) / (math.pi * shear_stress_mpa)) ** (1/3)
    return round(diameter, 2)

print("Required shaft diameter (mm):", shaft_diameter(5, 1200, 40))

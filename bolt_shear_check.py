"""
Bolt Shear Safety Check
Purpose: Checks whether a bolt is safe in shear for a given load
based on allowable shear stress.
"""

import math

def bolt_shear_check(load_n, bolt_diameter_mm, allowable_shear_mpa):
    area = math.pi * (bolt_diameter_mm ** 2) / 4
    shear_stress = load_n / area
    return round(shear_stress, 2), shear_stress <= allowable_shear_mpa

load = 10000        # N
diameter = 10       # mm
allowable_stress = 60  # MPa

stress, safe = bolt_shear_check(load, diameter, allowable_stress)

print("Shear stress (MPa):", stress)
print("Bolt safe:", safe)

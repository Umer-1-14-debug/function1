import math
angle_deg = float(input("Enter the angle in degrees: "))
angle_rad = math.radians(angle_deg)
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)
print("The value of ",angle_deg," angle is " ,sin_value)
print("The value of ",angle_deg," angle is " ,cos_value)
print("The value of ",angle_deg," angle is " ,tan_value)

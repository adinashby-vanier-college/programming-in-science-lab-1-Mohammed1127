import math

print("The equation for a mass-spring system oscillating in SHM is x(t) = Acos(wt+o). This code will give the value for x at any t for given values of A, w and o")

Amplitude = float(input("Enter your desired amplitude: "))
Angular_frequency = float(input("Enter your desired angluar frequency: "))
Phase_constant = float(input("Enter your desired phase constant"))
Time = float(input("ENter your desired time: "))

x = Amplitude * math.cos((Angular_frequency*Time)+Phase_constant)
print(f"The value of x at this moment with these SHM parameters is {x}")

print(float(math.sqrt(x)))
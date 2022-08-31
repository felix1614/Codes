'''Given the average fuel economy of a vehicle (The number of kilometres a vehicle can travel for each litre of fuel), the amount of fuel in the vehicle's fuel tank, the price of fuel, and the distance of a journey, calculate the total cost of the trip.

You should return
0.00
if the fuel already in the tank is sufficient to cover the journey.
Input
Line 1: A float, e, fuel economy of the vehicle in Km/L
Line 2: A float, f, fuel already in tank in L
Line 3: A float, p, the price of fuel in EUR/L
Line 4: A float, d, the distance of the journey in Km
Output
A float, the cost of the journey in EUR, rounded up to two decimal places.
Constraints
0 < e <= 100000
0 <= f <= 100000
0 <= p <= 100000
0 <= d <= 100000
Example
Input
13.0
2.6
1.64
110
Output
9.62'''
import math

# a =13.0
# f = 2.6
# p = 1.64
# d = 110

a=lambda:float(input())
e=a()
f=a()
print(f'{math.ceil(a()*max(0,a()-e*f)/e*100)/100:.2f}')

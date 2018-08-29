#!/usr/bin/python

# Given a number, return the greatest power of two less than or equal 
# to that number.
# Examples:
# fn(5) => 2  // (2**2 = 4)
# fn(10) => 3  // (2**3 = 8)
# fn(100) => 6 // (2**6 = 64)


def closest_power_of_two(n):
    if n == 0:
        return -1
    power = 0
    while ((2**power) <= n):
        power += 1
    power = power-1
    value = 2**power
    print "2**"+str(power)+"=="+str(value)+", "+ str(value)+ " <= " + str(n)
    return power

if __name__ == '__main__':
   print closest_power_of_two(0)
   print closest_power_of_two(1)
   print closest_power_of_two(2)
   print closest_power_of_two(3)
   print closest_power_of_two(4)
   print closest_power_of_two(5)
   print closest_power_of_two(8)
   print closest_power_of_two(9)
   print closest_power_of_two(16)
   print closest_power_of_two(17)
   print closest_power_of_two(32)
   print closest_power_of_two(33)
   print closest_power_of_two(64)
   print closest_power_of_two(65)
   print closest_power_of_two(128)
   print closest_power_of_two(129)
   print closest_power_of_two(256)
   print closest_power_of_two(257)

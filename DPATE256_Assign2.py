##
#Dhyey Patel
#250960470
#October 25th 2017
#Assignment 2: Volume Calculator
##

# import pi from math, because the number pi is needed
from math import pi

#Have a main function, which runs the other functions
def main():
    #define the 3 lists that will be used
    cube_volumes = []
    pyramid_volumes = []
    ellipsoid_volumes = []
    # set checker to true, so that I can get out of the while loop when needed
    checker = True
    # start while loop
    while (checker):
        # take in the shape through the function shape input
        shape = shapeinput()
        # depending on what shape it is run the function associated to that shape, and add the volume to the associated list
        if (shape == "cube"):
            cube_volumes.append(cube())
        elif (shape == "pyramid"):
            pyramid_volumes.append(pyramid())
        elif (shape == "ellipsoid"):
            ellipsoid_volumes.append(ellipsoid())
        # if the user would like to quit, say that the session has come to an end, and change checker to false to exit the while loop
        elif (shape == "quit"):
            print("You have come to the end of the session")
            checker = False
    # sort all the lists in ascending order
    cube_volumes.sort()
    pyramid_volumes.sort()
    ellipsoid_volumes.sort()
    # print the final output in the specified format
    if (len(cube_volumes)==0 and len(pyramid_volumes)==0 and len(ellipsoid_volumes)==0):
        print("You did not perform any volume calculations")
    else:
        print("The volumes calculated for each shape are shown below: ")
        if (len(cube_volumes)!=0):
            print("Cube: ",end="")
            for el in cube_volumes:
                if (el == cube_volumes[0]):
                    print("%0.1f"%(el),end="")
                else:
                    print(", %0.1f"%(el),end="")
            print()
        elif(len(cube_volumes)==0):
            print("Cube: No computations for this shape")
        if (len(pyramid_volumes)!=0):
            print("Pyramid: ",end="")
            for el in pyramid_volumes:
                if (el == pyramid_volumes[0]):
                    print("%0.1f"%(el),end="")
                else:
                    print(", %0.1f"%(el),end="")
            print()
        elif(len(pyramid_volumes)==0):
            print("Pyramid: No computations for this shape")
        if (len(ellipsoid_volumes)!=0):
            print("Ellipsoid: ",end="")
            for el in ellipsoid_volumes:
                if (el == ellipsoid_volumes[0]):
                    print("%0.1f"%(el),end="")
                else:
                    print(", %0.1f"%(el),end="")
            print()
        elif(len(ellipsoid_volumes)==0):
            print("Ellipsoid: No computations for this shape")

# Function Number 1: Used to get the right shape, and make sure it is a valid input
def shapeinput ():
    # Run until the correct input is given
    while (True):
        # get the user input and check to make sure that it is a valid input
        user_input = input("Enter the shape: ")
        user_input = user_input.lower()
        if (user_input=="cube" or user_input=="pyramid" or user_input=="ellipsoid" or user_input=="quit"):
            return (user_input)

# Function Number 2: Used to prompt for the side length, calculate the volume, print the volume and then return the volume
def cube():
    # prompt the user for the lenght and then calculate the volume
    length = float(input("Enter a side length: "))
    volume = length ** 3
    # round the volume to one decimal, then print the side length and the volume, then return volume
    round(volume,1)
    print("The volume of a cube with a side length %0.1f is %0.1f" % (length, volume))
    return volume

# Function Number 3: Used to prompt for the base and height, calculate the volume, print the volume and then return the volume
def pyramid ():
    # prompt the user for the base and the height, and then calculate the volume
    base = float(input ("Enter the length of the base: "))
    height = float(input ("Enter the length of the height: "))
    volume = (1/3) * (base ** 2) * (height)
    # round the volume to one decimal, then print the base, the height and the volume, then return volume
    round(volume,1)
    print("The volume of a pyramid with a base of %0.1f and a height of %0.1f is %0.1f" % (base, height, volume))
    return volume

# Function Number 4: Used to prompt for the 3 different radii, calculate the volume, print the volume and then return the volume
def ellipsoid ():
    # prompt the user for the 3 radii, and then calculate the volume
    radius1 = float(input("Enter the first radius: "))
    radius2 = float(input("Enter the second radius: "))
    radius3 = float(input("Enter the third radius: "))
    volume = (4/3) * (pi) * (radius1) * (radius2) * (radius3)
    # round the volume to one decimal, then print the 3 radii, then return volume
    round(volume,1)
    print("The volume of a ellipsoid with the radii %0.1f, %0.1f and %0.1f is %0.1f" % (radius1, radius2, radius3, volume))
    return volume

# Run the main function
main()

# Name: Johnathan Sullivan
# Date: 11/17/24
# Lab12part3


# This program reads in from the provided SWPlanets.txt file and reports (prints) /
# the name and rotational speed of the planets that are within the range of 23-26 hours. /
# Create two lists - 1) Store the planet names 2) Store the Rotational Speed. Use the created lists to report (print) /
# the planets meeting the above rotational speed requirement.

# Hint: You can use the string SPLIT method to separate the data fields for each line read in.
# Hint: Use a loop and IF check to see if rotational speed is within the 23-26 hour range.


# Define the main Function
def main():
    planet_names = []
    rotational_speeds = []
# make a try loop
    try:
        file = open('SWPlanets.txt', 'r') #open the file SWPlanets.txt file

        for line in file:
            planet, speed = line.strip().split(',') #Strip the planets and speeds

            speed = int(speed)

            planet_names.append(planet)
            rotational_speeds.append(speed)
     #If the user puts in a wrong file
    except FileNotFoundError:
        print("The file 'SWPlanets.txt' was not found.")
        return
    finally:
        file.close()
# This is the section I used online resources for. I thought of a few ways to do this and I went with this
    print("Planets with Rotational Speeds between 23 and 26 hours:")
    for i in range(len(planet_names)):
        if 23 <= rotational_speeds[i] <= 26:
            print(f"{planet_names[i]}: {rotational_speeds[i]} hours")
main()


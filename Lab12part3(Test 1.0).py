def main():
    # Initialize two lists: one for planet names and one for their rotational speeds
    planet_names = []
    rotational_speeds = []

    try:
        # Open the file
        file = open('SWPlanets.txt', 'r')

        for line in file:
            # Split each line into planet name and rotational speed
            planet, speed = line.strip().split(',')

            # Convert speed to an integer
            speed = int(speed)

            # Add planet and speed to their respective lists
            planet_names.append(planet)
            rotational_speeds.append(speed)

    except FileNotFoundError:
        print("The file 'SWPlanets.txt' was not found.")
        return
    finally:
        # Ensure the file is closed
        file.close()

    # Output the planet names and rotational speeds that meet the condition
    print("Planets with rotational speeds between 23 and 26 hours:")
    for i in range(len(planet_names)):
        if 23 <= rotational_speeds[i] <= 26:
            print(f"{planet_names[i]}: {rotational_speeds[i]} hours")


# Call the main function
main()

# Name: Johnathan Sullivan

# Date: 11/15/2024

# Lab: Lab12part2

# Program will import matlib, it will use the

#a Python program that READS the contents of the provided 1994_Weekly_Gas_Averages.txt file and use matplotlib to plot /

# the data as a bar chart. Be sure to display meaningful labels along the X and Y axis, as we as readable tick marks. /

# Also, add an appropriate title to your graph.

#Read all lines of provided file into a list in order to graph. /

# DO NOT USE  " with open" to read file data into your list.


#import matplot.pyplot

import matplotlib.pyplot as plt

#Define Main Function
def main():

    keep_going = True
    while keep_going: #make the loop
        try:
            # Ask for the filename input
            filename = input('Please enter a filename: ')
            # open the file.
            my_file = open(filename, 'r')

        except FileNotFoundError:
            # File Error
            print(f'The file "{filename}" does not exist! Please enter a valid filename.')

        else:
            # If the file is found, proceed
            print('File was found. You can continue.')
            keep_going = False  # Exit loop after file is successfully opened
            print(f'We are continuing with our program.')


    # Prices data
    try:
        prices = [line.strip() for line in my_file.readlines()]
        prices = [float(price) for price in prices if price]
    # Convert each line to a float
    except ValueError:
        print("The file contains invalid data.")
        return

    # Generate weeks for the x-axis
    weeks = list(range(1, len(prices) + 1))

    # Plotting the data
    plt.bar(weeks, prices,)

    # Add labels and title
    plt.title('Weekly Gas Prices for 1994')
    plt.xlabel('Weeks')
    plt.ylabel('Gas Prices (USD)')


    # Show the plot
    plt.tight_layout()
    plt.show()


# Call the main function
main()


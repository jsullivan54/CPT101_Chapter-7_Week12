# Name: Johnathan Sullivan

# Date: 11/15/2024

# Lab: Lab12part2

# Program will import matlib, it will use the

#a Python program that READS the contents of the provided 1994_Weekly_Gas_Averages.txt file and use matplotlib to plot /

# the data as a bar chart. Be sure to display meaningful labels along the X and Y axis, as we as readable tick marks. /

# Also, add an appropriate title to your graph.

#Read all lines of provided file into a list in order to graph. /

# DO NOT USE  " with open" to read file data into your list.

import matplotlib.pyplot as pit

NUM_WEEKS = 52

infile = open('1994_Weekly_Gas_Averages.txt', 'r')



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

    prices = my_file.readlines()
    print(prices)
    print()

    pit.title('Weekly Gas Prices for 1994 ')

    pit.xlabel('Weeks')

    pit.ylabel('Gas Prices')

    prices = my_file.readlines()
    for i in range (len(prices)):
        prices[i] = float(prices[i].rstrip('n'))


    left_edges = []



    # Create a list with the heights of each bar.
    heights = []

    bar_width = 1
    pit.bar(left_edges, heights, bar_width)
    pit.show()

# Close the file after reading
#1994_Weekly_Gas_Averages.txt.close()

main()

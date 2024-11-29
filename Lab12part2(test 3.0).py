import matplotlib.pyplot as plt


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


    # Process the prices data
    try:
        prices = [line.strip() for line in my_file.readlines()]
        prices = [float(price) for price in prices if price]
    # Convert each line to a float
    except ValueError:
        print("The file contains invalid data. Ensure all lines are valid numeric prices.")
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


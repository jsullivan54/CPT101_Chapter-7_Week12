

def main():
    name_list = []
    again = 'y'
    while again == ' y ':
        name = input('Enter a name:')
        name_list.append(name)
        print('Do you want to add another name?')
        again = input('y = yes, anything else = no:')
        print()
        print('Here are the names you entered.')
        for name in name_list:
            print(name)

if __name__ == '__main__':
    main()
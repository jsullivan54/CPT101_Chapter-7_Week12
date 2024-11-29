

def main():
  food = ['Pizza', 'Burgers', 'Chips']
  print('Here are the items in the food list:')

  print(food)

  item = input('Which item should I change?')
  try:
    item_index = food.index(item)
    new_item = input('Enter the new value:')
    food[item_index] = new_item
    print('Here is the revised list:')
    print(food)
  except ValueError:
      print('That item was not found in the list.')

if __name__ == '__main__':
    main()
import FourTreeCLS

# the main menu start here, loop that asks the user to do what he wants according to the menu:
mainTree = '0'
print("Hello")
while True:
    dic = {1: FourTreeCLS.makeTree, 2: FourTreeCLS.addToTree, 3: FourTreeCLS.deleteNodeFromTree}
    x = input("Menu:\n 1) Make new tree\n 2) Add to existing tree\n"
              " 3) Delete from existing tree\n 4) Print the tree\n 5) Exit\n")
    if x == '1':
        mainTree = dic[1]()
    elif x == '2':
        try:
            dic[2](mainTree)
        except UnboundLocalError as err:
            print(f'Unbound local error,not optional - {err}')
    elif x == '3':
        try:
            dic[3](mainTree)
        except UnboundLocalError as err:
            print(f'Unbound local error,not optional - {err}')
    elif x == '4':
        if mainTree == '0':
            print("The tree is empty.")
        else:
            print(mainTree)
    elif x == '5':
        print("Thanks, good bye")
        break
    else:
        print("Wrong choose, try again please\n")


class TreeError(Exception):
    """
    base class for tree exceptions, gets the massage and the tried value
    """

    def __init__(self, massage, value):
        """
        init function - gets the massage and the tried value
        :param massage: massage to show about the error
        :param value: value tried to delete
        """
        self.massage = massage
        self.value = value


class TreeValueDoesNotExist(TreeError):
    """
    class for exceptions that the user tried to delete value that does not exist
    """

    def __str__(self):
        """
        exception to string
        :return: format of the exception - string
        """
        return f'Coundnt find node with value: {self.value}'


class TreeIllegalValue(TreeError):
    """
    class for exceptions that the user tried to delete node that his list of children is not empty
    """

    def __str__(self):
        """
        exception to string
        :return: format of the exception - string
        """
        return f'Found but illegal to delete value: {self.value}'


class Narray:
    """
    class of the array - each node have list of 4 children
    2 left sons are smaller than the node
    2 right sons are bigger than the node
    list of sons starts with 4 NONE's.
    """

    def __init__(self, entry):
        """
        builds an object with the given value, sons are empty
        :param entry:value of the node
        """
        self.entry = float(entry)
        self.children = [None, None, None, None]

    def addC(self, other):
        """
        function that gets value and enters it to the correct place in the tree
        :param other: the value to enter the tree
        :return:
        """
        if other.entry < self.entry:
            if self.children[0] == None:
                self.children[0] = other
                return
            if self.children[1] == None:
                self.children[1] = other
                return
            x, y = searchPlace(self.children[0], other.entry), searchPlace(self.children[1], other.entry)
            if x > y:
                self.children[1].addC(other)
            else:
                self.children[0].addC(other)
        else:
            if self.children[2] == None:
                self.children[2] = other
                return
            if self.children[3] == None:
                self.children[3] = other
                return
            x, y = searchPlace(self.children[2], other.entry), searchPlace(self.children[3], other.entry)
            if x > y:
                self.children[3].addC(other)
            else:
                self.children[2].addC(other)

    def __repr__(self):
        """
         function returns a printable representation of the tree
        :return:printable representation of the tree
        """
        return f'N-arr({repr(self.entry), repr(self.children)}'

    def __str__(self):
        """
        function converts the tree to string
        :return: format that represents the tree
        """
        return f'N-arr({repr(self.entry), repr(self.children)}'

    def deleteFromT(self, x):
        """
        function that gets value and tries to delete it from the tree
        can raise an exception if the value is not in the tree or have children
        :param x: the value to delete
        :return: -
        """
        flag = False

        def deleteT(self, x):
            """
            help funcion for delete value from tree
            :param self: node to continue from
            :param x: the value to delete
            :return: false if not exists , else true
            """
            nonlocal flag
            if self is None:
                return False
            if x < self.entry:
                if self.children[0] != None and deleteT(self.children[0], x) == True:
                    self.children[0] = None
                    flag = True
                if self.children[1] != None and deleteT(self.children[1], x) == True:
                    self.children[1] = None
                    flag = True
            elif x > self.entry:
                if self.children[2] != None and deleteT(self.children[2], x) == True:
                    self.children[2] = None
                    flag = True
                if self.children[3] != None and deleteT(self.children[3], x) == True:
                    self.children[3] = None
                    flag = True
            else:
                if self.children[0] == None and self.children[1] == None and self.children[2] == None and self.children[
                    3] == None:
                    return True
                else:
                    raise TreeIllegalValue("illegal value", x)

        b = deleteT(self, x)
        if flag == False: raise TreeValueDoesNotExist("Does not exist in tree", x)


def searchPlace(self, x):
    """
    function to help to add to the tree
    :param self: the node to continue from
    :param x: given number to add
    :return: the number of levels to go down for entering the given number
    """
    if x < self.entry and (self.children[0] == None or self.children[1] == None):
        return 1
    if x > self.entry and (self.children[2] == None or self.children[3] == None):
        return 1
    else:
        if x < self.entry:
            s, y = searchPlace(self.children[0], x), searchPlace(self.children[1], x)
            if x > y:
                return 1 + y
            else:
                return 1 + s
        else:
            s, y = searchPlace(self.children[2], x), searchPlace(self.children[3], x)
            if x > y:
                return 1 + y
            else:
                return 1 + s


def addToTree(tree):
    """
    function for the menu - add to tree
    can raise unbound local error if the tree is empty
    :param tree: the tree to add to
    :return: the tree with the added value
    """
    if tree == '0':
        raise UnboundLocalError("The tree is not initialized")
    else:
        return tree.addC(Narray(float(input("Enter the value to enter the tree: "))))


def makeTree():
    """
    makes new tree for menu, asks the user to add the value of the first node
    :return: the new tree
    """
    x=float(input("Enter the value to enter the top of tree: "))
    return Narray(x)


def deleteNodeFromTree(tree):
    """
    delete function for main menu
    can raise unboundLocalError and tree exceptions
    :param tree: tree to delete from
    :return: -
    """
    if tree == '0':
        raise UnboundLocalError("The tree is not initialized")
    else:
        try:
            tree.deleteFromT(float(input("Enter the value to delete:\t")))
            print("Successful.")
        except TreeError as err:
            if type(err) == TreeIllegalValue:
                print(f'Tree illegal value error: {err}.')
            if type(err) == TreeValueDoesNotExist:
                print(f'Tree value does not exist error: {err}.')

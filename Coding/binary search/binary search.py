#binary search
#currently doesnt give you the position of the thing in the list
#just tells you if it's there

'''
binary search algorithm

when searching for a certain item (x) in a list of items:

-split the entire list in half and look at the item you find

	-if the value of (x) is greater than the item you find:
		-disregard the lower half of the list
		-split the 'higher' half of the list in half and continue/repeat

	-if the value of (x) is lesser than the item you find:
		-disregard the 'higher' half of the list
		-split the 'lower' half of the list in half and continue/repeat

	-when you get down to one item:
		-it should be the item
		-OR:
		-if it is not the item, the item is not in the list

'''


def find_the_thing (the_list, the_thing):
    found=False
    while not found:
        if len(the_list) == 1:
            if the_list[0] == the_thing:
                return True
            else:
                print("Looks like it's not in the list.")
                return False

        check = the_list[len(the_list)//2]

        if the_thing == check:
            print(the_thing)
            return True

        else: #split
            the_list_smaller = the_list[0:(len(the_list)//2)] #smaller half
            the_list_bigger = the_list[(len(the_list)//2):(len(the_list))] #bigger half

            if the_thing < check:
                the_list=the_list_smaller

            if the_thing > check:
                the_list=the_list_bigger

        
find_the_thing([1,2,3,4,5,6,7,8,9],8)
find_the_thing([5,6,7,8,9,10,11,12,13,14,15],7)
find_the_thing([1,2,3,4,5,6,7,8,9],-1)

#alist=[1,2,3,4,5,6]
#print(alist[0:(len(alist)//2)])

    

import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def core():
    random.shuffle(nums)
    print("The sequence is", * nums)

    numsint = int(''.join(map(str, nums)))
    inp = input("Enter the numbers that are displayed in order: ")

    try:
        inp = int(inp)

        if(inp == numsint):
            print("That is correct.")
            wait = input("Press enter to end.")
        else:
            print("That is incorrect.")
            wait = input("Press enter to try again.")
            core()
    except:
        print("Please enter something valid.")
        wait = input("Press enter to try again.")
        core()


core()

# write an application to pre-sell a limited number of cinema tickets
# each buyer can buy up to 4 tickets
# no more than 20 tickets can be sold
# prompt user for the desired amount of tickets
# display # of remaining tickets after their purchase
# repeat until all have been sold.

# main() function calls ask_tickets_and_validate() function to run the program.
def main():
   ask_tickets_and_validate()

# function that gets user input, validates input and outputs Buyer #, Ticket Amount Purchased.
def ask_tickets_and_validate():
    # create tickets variable set to max amount available to be sold: 20
    tickets = 20
    # create empty list to append ticket purchase amounts to.
    lst = []
    # create while loop, while tickets is less than 0, continously run.
    while tickets > 0:
        # try/except block. ask user for input and convert string response to integer.
        try:
            num = int(input("How many tickets would you like to purchase? Up to 4 tickets can be purchased: "))
            # if condition. if num is less than 5 and greater than 0, decrement number from ticket amount.
            if 5 > num > 0:
                tickets -= num
                # append num or user's input to our empty list variable: lst
                lst.append(num)
                # print to user the amount of tickets left for purchase.
                print(tickets, ' tickets are here left')
                # create instance of dictionary. use dictionary comprehension.
                # set index as the key for each buyer, and the value as the list element
                # we use enumerate() function create indices of each element in our list
                buyer_dict = {index: value for index, value in enumerate(lst)}
                # use for loop to iterate through our dictionary to help format data in dictionary
                # to look better to user.
                for index, value in buyer_dict.items():
                    print(f"\n", f"Buyer {index + 1}:", f"Ticket Amount: {value}")
            # part of if/elif/else conditional. once tickets equals 0 break out of the while loop
            elif tickets == 0:
                break
                # create validation, if user attempts to input 0 or a number greater than 5 do not continue
                # rest of statements within the while loop.
            else:
                print("Ticket amount must be greater than 0 and less than 5.")
                # throw a valueError to user if a non-integer type is entered in the input() function
        except ValueError:
            print("Invalid input. Ticket amount must be a number.")


main()


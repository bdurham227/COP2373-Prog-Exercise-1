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
    tickets = 20
    lst = []
    while tickets > 0:
        try:
            num = int(input("How many tickets would you like to purchase? Up to 4 tickets can be purchased: "))
            if 5 > num > 0:
                tickets -= num
                lst.append(num)
                print(tickets, ' tickets are here left')
                buyer_dict = {index: value for index, value in enumerate(lst)}
                for index, value in buyer_dict.items():
                    print(f"\n", f"Buyer {index + 1}:", f"Ticket Amount: {value}")

            elif tickets == 0:
                break
            else:
                print("Ticket amount must be greater than 0 and less than 5.")
        except ValueError:
            print("Invalid input. Ticket amount must be a number.")


main()


MAX_LINES = 3
MAX_BET=100
MIN_BET=1


def deposit():
    while True:
        amount = input("enter the amount to be deposited ")#user may add any string as input to stop that we add isdiit function we directly do not convert it as int(input()) because user may add any negative integer as well then 
        if amount.isdigit():#using isdigit is necessary as it checks if the string is convertable or not 
            amount = int(amount)
            if amount>0:
                break
            else:
                print("enter a valid amount")
        else:
            print("enter valid amount")
    return amount

def get_number_of_lines():
     while True:
        lines = input("enter the number of lines from 1 to "+str(MAX_LINES) +") ")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("enter a valid number of lines ")
        else:
            print("enter valid number of lines")
        return lines
def get_bet():
     while True:
        amount = input("enter the amount to be bet ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"amount must be between {MIN_BET}and {MAX_BET}")#f string is a formatted string used to add values from the variable to the sentence that may vary accordingly we dont need to change the statement each time formatted string are diffrent and convienient that string concatination a
        else:
            print("enter a valid number")
        return amount

def main():
   balance = deposit()
   lines = get_number_of_lines()
   print(balance,lines)
main()
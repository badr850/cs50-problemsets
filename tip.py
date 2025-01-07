def main():
  #asking the user for the cost of the meal and the percantage of tip they want to leave.
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave {tip:.2f}$")

#getting rid of "$" and "%" signs (if they exist) and working with floats instead of strings:
def dollars_to_float(d):
    no_dollars=d.replace("$","")
    price=float(no_dollars)
    return price
def percent_to_float(p):
    no_percent=p.replace("%","")
    percentage=float(no_percent)/100
    return percentage

main()

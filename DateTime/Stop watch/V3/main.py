from stopwatch import StopWatch as swa

def main():
    s = int(input("Enter the number of seconds: "))
    sw = swa(s)
    choice = int(input("Enter 1 for countdown or 2 for countup: "))
    match choice :
        case 1:
            sw.countdown()
        case 2:
            sw.countup_with_laps()
        case _ :
            print("Invalid choice!")

if __name__ == '__main__' :
    main()
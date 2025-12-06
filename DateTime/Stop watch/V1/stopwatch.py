import time
import Ansi as an 

class StopWatch :
    def __init__(self, seconds: int = 0):
        self.time_done =  None
        self.seconds = seconds
    
    def format(self , seconds:int):
        sec = seconds % 60 
        mins = (seconds //60) % 60
        hour = seconds // 3600
        return f" {an.HIGHLIGHT}{an.BOLD}{an.RED}{hour:02d}:{mins:02d}:{sec:02d}{an.RESET}"
    
    def countdown(self ):
        try :
            for i in range(self.seconds , 0 , -1):
                print(self.format(i) , end = "\r")
                time.sleep(1)
            print(f"{an.GREEN} 00:00:00{an.RESET}")
            self.time_done = "Time's up!" 
            print(f"{an.BOLD}{an.GREEN}{self.time_done}{an.RESET}")
        except KeyboardInterrupt:
            self.time_done = "Countdown interrupted!"
            print(f"{an.RED}{self.time_done}{an.RESET}")
        except Exception as e:
            self.time_done = f"An error occurred: {e}"
            print(f"{an.RED}{self.time_done}{an.RESET}")

    def countup(self ):
        try :
            for i in range(0 , self.seconds + 1): 
                print(self.format(i) , end = "\r")
                time.sleep(1)
            print(f"{an.GREEN} {self.format(self.seconds)}{an.RESET}")
            self.time_done = f"Count complete upto {self.seconds} seconds"
            print(f"{an.GREEN}{an.BOLD}{self.time_done}{an.RESET}")
        except KeyboardInterrupt:
            self.time_done = "Countup interrupted!"
            print(f"{an.RED}{self.time_done}{an.RESET}")
        except Exception as e:
            self.time_done = f"An error occurred: {e}"
            print(f"{an.RED}{self.time_done}{an.RESET}")

        

if __name__ == "__main__" :
    pass 
    # or can add demo testing here
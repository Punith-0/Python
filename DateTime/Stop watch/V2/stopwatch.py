import time
import Ansi as an 
import msvcrt

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

    def countup_with_laps(self ):
        self.laps = [] 
        i = 0
        print(f"{an.YELLOW}1.l -> Record lap \n2.q ->Quit  {an.RESET}")
        try :
            while (self.seconds == 0 or i <= self.seconds) :
                print(self.format(i) , end = "\r")
                if msvcrt.kbhit() :
                    key = msvcrt.getch().decode().lower()
                    if key == 'l' :
                        self.laps.append(i)
                        print(f"\n{an.YELLOW}Lap recorded at {self.format(i)}{an.RESET}")
                    elif key == 'q' :
                        print(f"\n{an.RED}Countup stopped by user at {self.format(i)}{an.RESET}")
                        self.time_done = f"Stopped at {self.format(i)}"
                        break
                    else :
                        raise KeyboardInterrupt
                time.sleep(1)
                i += 1
            if self.seconds != 0 and i > self.seconds:
                print(f"{an.GREEN} {self.format(self.seconds)}{an.RESET}")
                self.time_done = f"Count complete upto {self.seconds} seconds"
                print(f"{an.GREEN}{an.BOLD}{self.time_done}{an.RESET}")

        except KeyboardInterrupt:
            self.time_done = "Countup interrupted!"
            print(f"{an.RED}{self.time_done}{an.RESET}")
        except Exception as e:
            self.time_done = f"An error occurred: {e}"
            print(f"{an.RED}{self.time_done}{an.RESET}")
        finally :
            if self.laps :
                print(f"{an.BOLD}{an.BLUE}Laps recorded:{an.RESET}")
                for i, lap in enumerate(self.laps, start=1):
                    print(f"Lap {i}: {self.format(lap)}")

        

if __name__ == "__main__" :
    pass 
    # or can add demo testing here
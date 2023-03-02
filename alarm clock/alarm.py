import datetime
import time
import winsound

def set_alarm():
    while True:
        try:
            alarm_time_str = input("Enter the time in HH:MM format for the alarm: ")
            alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M").time()
            break
        except ValueError:
            print("Invalid time format. Please enter time in HH:MM format.")

    print(f"Alarm set for {alarm_time_str}.")

    while True:
        now = datetime.datetime.now().time()
        if now >= alarm_time:
            print("Time's up!")
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            break
        else:
            time.sleep(60)

def main():
    print("Welcome to the Alarm Clock App!")
    while True:
        print("\n1. Set Alarm")
        print("2. Quit")
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            set_alarm()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f"\033[96m{mins:02d}:{secs:02d}\033[0m"  # Cyan timer
        print(timer_format, end="\r")
        time.sleep(1)
        seconds -= 1

    print("\033[91m⏰ Time's up!\033[0m")  # Red message when time is up

# User se input lena
seconds = int(input("\033[94mEnter countdown time in seconds: \033[0m"))  # Blue input prompt
countdown_timer(seconds)

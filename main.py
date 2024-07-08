import threading
import time
import sys
sys.path.append('models')
sys.path.append('utils')
from packet_analysis import start_sniffing
from telegram import send_telegram_message

def print_detected_attacks(detected_attacks):
    while True:
        if detected_attacks:
            headers = ["Timestamp", "Attack Type", "Source IP", "Details"]
            attack_details = []

            for attack in detected_attacks:
                attack_details.append([attack["Timestamp"], attack["Attack Type"], attack["Source IP"], attack["Details"]])

            print("\nDetected Attacks:")
            print(tabulate.tabulate(attack_details, headers=headers, tablefmt="grid"))
            print()

            # Clear detected attacks list after printing
            detected_attacks.clear()

        else:
            # Print message only when no attacks are detected
            print("No attacks detected.")

        time.sleep(1)  # Print every 1 second

def main():
    # Start printing detected attacks in a separate thread
    print_thread = threading.Thread(target=print_detected_attacks, args=(detected_attacks,))
    print_thread.daemon = True
    print_thread.start()

    # Start packet sniffing
    start_sniffing('ens33')

if __name__ == "__main__":
    main()

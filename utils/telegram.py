import requests

# Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.get(telegram_url, params=params)
        response.raise_for_status()
        print(f"Telegram message sent successfully: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Telegram message: {e}")

def handle_detected_attack(attack_type, src_ip, count):
    detected_attacks.append({
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Attack Type": attack_type,
        "Source IP": src_ip,
        "Details": f"Packets Count: {count}"
    })

    # Send Telegram message
    send_telegram_message(f"Warning!!! Detected {attack_type} Attack from IP: {src_ip}")

    # Update last detected attack
    global last_detected_attack
    last_detected_attack = attack_type

if __name__ == "__main__":
    send_telegram_message("Testing Telegram message")

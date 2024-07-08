import scapy.all as scapy
from scapy.layers.inet import IP, TCP, UDP, ICMP, Raw
from collections import defaultdict
from datetime import datetime
from telegram import handle_detected_attack, send_telegram_message

detected_attacks = []
last_detected_attack = None

def detect_attack(packet, model, scaler, label_encoder):
    global last_detected_attack, detected_attacks

    if IP in packet:
        src_ip = packet[IP].src
        features = extract_features(packet)
        if features:
            scaled_features = scaler.transform([features])
            prediction = model.predict(scaled_features)
            attack_label = label_encoder.inverse_transform(prediction)[0]

            if attack_label != 'normal.':
                handle_detected_attack(attack_label, src_ip, 1)

def extract_features(packet):
    if IP in packet:
        return [
            packet[IP].len,
            packet[IP].proto,
            packet[IP].tos,
            packet[IP].ttl,
            len(packet),
            packet[IP].flags,
            1 if packet.haslayer(TCP) else 0,
            1 if packet.haslayer(UDP) else 0,
            1 if packet.haslayer(ICMP) else 0,
            1 if packet.haslayer(Raw) else 0
        ]
    return None

def start_sniffing(interface):
    model, scaler, label_encoder = load_saved_model()
    print(f"Starting packet capture on interface {interface}...")
    scapy.sniff(iface=interface, prn=lambda x: detect_attack(x, model, scaler, label_encoder), store=0)

if __name__ == "__main__":
    start_sniffing('ens33')

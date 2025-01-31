import mido
import time
from pythonosc.udp_client import SimpleUDPClient

# Set up OSC client for SuperCollider
osc_client = SimpleUDPClient("127.0.0.1", 57120)

# Open MIDI input device
midi_input = mido.open_input()  # Auto-select first available MIDI device

print("Listening for MIDI input...")

# Stream MIDI data in real time
try:
    for msg in midi_input:
        if msg.type == 'note_on' or msg.type == 'note_off':
            velocity = msg.velocity if msg.type == 'note_on' else 0
            osc_client.send_message("/midi_note", [msg.note, velocity, msg.time])
            print(f"Sent: {msg.type} - Note: {msg.note}, Velocity: {velocity}")
except KeyboardInterrupt:
    print("MIDI stream stopped.")

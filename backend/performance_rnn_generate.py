import note_seq
import mido
import time
from pythonosc.udp_client import SimpleUDPClient
from note_seq.protobuf import music_pb2

# Initialize the OSC client
osc_client = SimpleUDPClient("127.0.0.1", 57120)

# Function to send MIDI in real-time with note-off events
def send_midi_live(note_sequence):
    for note in note_sequence.notes:
        # Send Note-On
        osc_client.send_message("/midi_note", [note.pitch, note.velocity, 1])
        time.sleep(note.start_time)
        
        # Send Note-Off
        osc_client.send_message("/midi_note_off", [note.pitch, 0])
        time.sleep(note.end_time - note.start_time)

# Generate a simple performance sequence (Modify for real model output)
sequence = music_pb2.NoteSequence()
notes = [
    (60, 80, 0.0, 0.5),  # C4
    (62, 80, 0.5, 1.0),  # D4
    (64, 80, 1.0, 1.5),  # E4
    (65, 80, 1.5, 2.0),  # F4
]

for pitch, velocity, start, end in notes:
    note = sequence.notes.add()
    note.pitch = pitch
    note.velocity = velocity
    note.start_time = start
    note.end_time = end

sequence.total_time = 2.0

print("Sending MIDI in real-time...")
send_midi_live(sequence)
print("Performance complete!")

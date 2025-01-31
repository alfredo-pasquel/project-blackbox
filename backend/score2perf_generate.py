import tensorflow.compat.v1 as tf
import note_seq
from note_seq.protobuf import generator_pb2
from magenta.models.score2perf import music_encoders
from magenta.models.shared import sequence_generator_bundle
import os

# Disable TensorFlow 2 behavior
tf.disable_v2_behavior()

# Path to the Score2Perf model
BUNDLE_PATH = "models/checkpoints/score2perf.mag"

print("Loading Score2Perf model...")
bundle = sequence_generator_bundle.read_bundle_file(BUNDLE_PATH)

# Load the performance encoder
encoder = music_encoders.MidiPerformanceEncoder(
    steps_per_second=100,
    num_velocity_bins=32,
    min_pitch=21,
    max_pitch=108,
    add_eos=True
)

# Create a primer sequence (this can be an empty NoteSequence)
primer_sequence = note_seq.protobuf.music_pb2.NoteSequence()
primer_sequence.notes.add(pitch=60, velocity=80, start_time=0.0, end_time=0.5)  # C4
primer_sequence.notes.add(pitch=64, velocity=80, start_time=0.5, end_time=1.0)  # E4
primer_sequence.notes.add(pitch=67, velocity=80, start_time=1.0, end_time=1.5)  # G4
primer_sequence.total_time = 1.5

# Generate MIDI sequence options
generator_options = generator_pb2.GeneratorOptions()
generator_options.generate_sections.add(start_time=1.5, end_time=10.0)  # Generate 8.5 seconds

# Generate music
print("Generating polyphonic music...")
encoded_primer = encoder.encode_note_sequence(primer_sequence)

# Placeholder for AI-generated MIDI
generated_sequence = note_seq.protobuf.music_pb2.NoteSequence()
generated_sequence.CopyFrom(primer_sequence)  # Start with the primer

# Simulate AI-generated notes (for testing, replace with real AI output)
for i in range(8):
    generated_sequence.notes.add(
        pitch=60 + i, velocity=90, start_time=i, end_time=i + 1
    )

# Save to MIDI file
midi_path = "models/generated.mid"
note_seq.sequence_proto_to_midi_file(generated_sequence, midi_path)
print(f"Generated MIDI saved to {midi_path}")

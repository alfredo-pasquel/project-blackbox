import note_seq
from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.melody_rnn.melody_rnn_model import default_configs, MelodyRnnModel
from magenta.models.shared import sequence_generator_bundle
import tensorflow.compat.v1 as tf
import mido
import time

tf.disable_v2_behavior()  # Disable TensorFlow 2.x behavior for Magenta

# Path to the downloaded MelodyRNN model checkpoint
BUNDLE_PATH = "models/checkpoints/basic_rnn.mag"
print("Loading MelodyRNN model...")

# Load the model bundle
bundle = sequence_generator_bundle.read_bundle_file(BUNDLE_PATH)

# Define the MelodyRNN Model using its configuration
config = default_configs['basic_rnn']  # Use the correct key for your model
model = MelodyRnnModel(config)

# Initialize the MelodyRNN sequence generator with the model and bundle
generator = melody_rnn_sequence_generator.MelodyRnnSequenceGenerator(
    model=model,
    details=bundle.generator_details,
    steps_per_quarter=config.steps_per_quarter,
    checkpoint=None,
    bundle=bundle
)

# Create a primer melody (starting notes)
primer_sequence = note_seq.protobuf.music_pb2.NoteSequence()
primer_sequence.notes.add(pitch=60, velocity=80, start_time=0.0, end_time=0.5)  # C4
primer_sequence.notes.add(pitch=62, velocity=80, start_time=0.5, end_time=1.0)  # D4
primer_sequence.total_time = 1.0

# Set generation options
print("Generating MIDI sequence...")
generator_options = note_seq.protobuf.generator_pb2.GeneratorOptions()
generator_options.generate_sections.add(
    start_time=1.0,
    end_time=16.0  # Generate 16 seconds of music
)

# Ensure the generator is initialized
generator.initialize()

# Generate the melody
generated_sequence = generator.generate(primer_sequence, generator_options)

# Save the generated MIDI file
midi_path = "models/generated_melody.mid"
note_seq.sequence_proto_to_midi_file(generated_sequence, midi_path)
print(f"Generated MIDI saved to {midi_path}")

# Send the generated MIDI sequence to Logic Pro via IAC Driver
print("Sending MIDI to Logic Pro...")
with mido.open_output('IAC Driver Bus 1') as port:
    for note in generated_sequence.notes:
        msg_on = mido.Message('note_on', note=int(note.pitch), velocity=int(note.velocity))
        port.send(msg_on)
        time.sleep(note.end_time - note.start_time)  # Hold the note duration
        msg_off = mido.Message('note_off', note=int(note.pitch), velocity=0)
        port.send(msg_off)

print("AI-generated melody played in Logic Pro successfully!")

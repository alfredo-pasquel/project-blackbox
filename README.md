# Project Blackbox

**Project Blackbox** is an AI-powered music creation app designed to generate MIDI sequences in real-time and send them to a Digital Audio Workstation (DAW) for playback and manipulation. It leverages Google Magenta's MelodyRNN and TensorFlow to generate procedurally crafted music based on user inputs and predefined configurations. The project comprises a frontend and backend, each handling distinct responsibilities to ensure seamless functionality and user interaction.

---

## Features
- **AI Music Generation**: Utilizes pretrained models like `basic_rnn` to create dynamic, expressive MIDI sequences.
- **Live MIDI Playback**: Sends generated MIDI sequences to DAWs like Logic Pro via the IAC Driver.
- **Customizable Inputs**: Allows users to define primer sequences and generation parameters.
- **Seamless Integration**: Frontend communicates with the backend for generating and previewing melodies in real time.
- **Modular Design**: Backend and frontend are decoupled for easy maintenance and scalability.

---

## Tech Stack

### Backend
- **Python**: Core language for AI model management and MIDI generation.
- **TensorFlow**: Framework for loading and running Magenta models.
- **Magenta**: Library for music and art generation.
- **Mido**: Library for MIDI communication.
- **Flask (or FastAPI)**: For serving backend APIs.

### Frontend
- **React**: Framework for building the user interface.
- **TailwindCSS**: For styling components with ease.
- **Web MIDI API** (future): For browser-based MIDI interaction.

---

## Setup Instructions

### Prerequisites
1. Python 3.8 or later
2. Node.js and npm
3. Logic Pro (or another DAW with IAC Driver enabled)
4. Virtual MIDI Driver (e.g., IAC on macOS)
5. Google Magenta pretrained models

### Backend Setup
1. Clone the repository and navigate to the backend directory:
   ```bash
   git clone <repository-url>
   cd backend
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```bash
   python3 app.py
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

---

## Usage
1. **Generate MIDI**:
   - Access the frontend interface and provide primer sequences or custom parameters.
   - Click "Generate" to create music based on the selected model.

2. **Live Playback**:
   - Ensure your DAW is set to receive MIDI input from the IAC Driver.
   - Listen to AI-generated melodies live.

3. **Customize Models**:
   - Modify the backend to use different Magenta pretrained models (e.g., `lookback_rnn`, `attention_rnn`).

---

## Directory Structure
```
project-blackbox/
|-- backend/
|   |-- models/                # Magenta models and utilities
|   |-- app.py                 # Main backend server file
|   |-- requirements.txt       # Python dependencies
|
|-- frontend/
|   |-- src/                   # React components
|   |-- public/                # Static assets
|   |-- package.json           # Frontend dependencies
|
|-- README.md                  # Project overview
```

---

## Future Enhancements
- **Web MIDI Integration**: Enable browser-based MIDI playback without needing a DAW.
- **Expanded Models**: Incorporate additional pretrained Magenta models for diverse musical styles.
- **User Profiles**: Save preferences, primer sequences, and generated outputs.
- **Collaboration Tools**: Allow multiple users to co-create music in real time.

---

## License
This project is licensed under the Apache License 2.0. See the `LICENSE` file for more details.

---

## Contributors
- **Alfredo Pasquel**

Feel free to reach out for any questions, suggestions, or contributions!


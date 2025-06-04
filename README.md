# Voice Chat Assistant

This repository contains a simple example of a voice-based assistant in Python.
The assistant uses a **local** language model (via the `transformers` library),
and relies on `speech_recognition` for microphone input and `pyttsx3` for
text-to-speech. The model is downloaded automatically on first run.

## Plan

1. Install dependencies (Python 3.10 or later):
   ```bash
   pip install -r requirements.txt
   ```
   - `pyaudio` is required by `speech_recognition` for microphone access.
2. Run `python voice_assistant.py`.
3. Speak into the microphone; the assistant will recognize your speech,
   generate a reply using the local model, and read it aloud.
4. Say `команда <shell command>` to execute a system command.
5. Say "выход" (or "quit"/"exit") to end the conversation.

This is a minimal example; you can expand it with a GUI,
custom wake word detection, or a local language model.

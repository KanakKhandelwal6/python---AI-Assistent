# Jarvis Voice Assistant

## Project Overview

Jarvis is a simple voice-activated assistant built using Python. It uses speech recognition to listen for commands, and based on these commands, it can open popular websites or play music from a predefined library.

## Features

* Voice activation using the wake word "Jarvis".
* Can open popular websites (Google, YouTube, LinkedIn, and ChatGPT).
* Plays music from a predefined music library using voice commands.

## Requirements

* Python 3.x
* SpeechRecognition (`pip install SpeechRecognition`)
* Pyttsx3 (`pip install pyttsx3`)
* Webbrowser (built-in Python module)
* MusicLibrary (custom module)

## Installation

1. Clone the repository.

```bash
git clone <your-repo-url>
```

2. Install the required Python libraries.

```bash
pip install SpeechRecognition pyttsx3
```

## Configuration

1. Ensure that your system has a working microphone.
2. Customize the musiclibrary module to contain your preferred music and their corresponding links.

## Usage

1. Run the script:

```bash
python jarvis.py
```

2. Say "Jarvis" to activate the assistant.
3. Provide your commands, such as:

   * "Open Google"
   * "Play \[song name]"

## Customizing Music Library

* The `musiclibrary` module is a dictionary that maps song names to their URLs.
* You can add more songs by updating this dictionary.

## Troubleshooting

* Ensure your microphone is working properly.
* If speech recognition does not work, verify your internet connection and ensure you have installed the `SpeechRecognition` package.
* Adjust the timeout and phrase time limit values in the script if it does not recognize your speech properly.

## Contributing

Feel free to submit a pull request if you want to add more features.

## License

This project is open source and free to use.

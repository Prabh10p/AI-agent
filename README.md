# Jarvis Virtual Assistant

Welcome to the **Jarvis Virtual Assistant** repository! This project is a voice-activated assistant named "Jarvis," designed to assist users in performing various tasks through natural language commands.

---

## Table of Contents
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Purpose](#purpose)
  - [Main Features](#main-features)
- [Explanation and Details](#explanation-and-details)
  - [How the Project Works](#how-the-project-works)
  - [Communication Between Backend and Frontend](#communication-between-backend-and-frontend)
- [Setup and Libraries](#setup-and-libraries)
  - [System Requirements](#system-requirements)
  - [Installation Steps](#installation-steps)
  - [Required Libraries](#required-libraries)
- [License](#license)
- [Contact](#contact)

---

## Introduction

### Overview
Jarvis is a voice-activated assistant that integrates multiple functionalities to assist users in performing daily tasks. It can play YouTube videos, search on Google, open applications, and interact with users in natural language. The project uses **Python** for backend logic, **HTML, CSS, Bootstrap, and JavaScript** for the frontend interface, and **Eel** to connect both backend and frontend.

### Purpose
The purpose of this project is to provide an intelligent assistant that allows users to perform tasks through voice commands, such as searching for information, opening applications, playing videos, and interacting with web platforms. The project aims to deliver an interactive and user-friendly experience.

### Main Features
- **Voice Recognition**: Understands spoken commands and responds accordingly.
- **YouTube Video Playback**: Automatically plays videos based on search terms.
- **Web Search**: Executes Google searches and opens relevant links.
- **Application Launch**: Opens system-installed applications via voice commands.
- **Interactive Frontend**: Provides real-time user feedback using a web interface.
- **AI Chatbot Integration**: Uses Groq API for intelligent responses.

---

## Explanation and Details

### How the Project Works
1. **Voice Command Input**:
   - The user speaks a command, which is captured by a microphone and converted into text using Google’s Speech Recognition API.

2. **Command Processing**:
   - The backend (Python) processes the command to determine the appropriate action, such as playing a video, opening an application, or performing a search.

3. **Frontend Interaction**:
   - The frontend provides real-time feedback, such as displaying the spoken command or showing search results. It is built using **HTML, CSS, Bootstrap, and JavaScript**.

4. **Backend Operations**:
   - The backend uses several Python libraries for specific functionalities:
     - `playsound==1.2.2` for audio feedback.
     - `pyaudio` for capturing voice input.
     - `speech_recognition` for converting speech to text.
     - `pywhatkit` for playing YouTube videos.
     - `webbrowser` for Google searches.
     - `os` for launching installed applications.
     - `pyttsx3` for text-to-speech responses.
     - `groq` for AI chatbot functionality.
     - `time` for execution delays.
     - `eel` for connecting the backend with the frontend.

### Communication Between Backend and Frontend
The frontend and backend communicate using **Eel**, a Python library that enables seamless interaction between web technologies and Python.

---

## Setup and Libraries

### System Requirements
- Python 3.7 or higher
- A working microphone
- Chrome or another modern web browser
- Node.js (optional, for socket/web server integrations)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Prabh10p/AI-agent.git
   cd AI-agent
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the application:
   ```bash
   python main.py
   ```

### Required Libraries
Each required library and its purpose is listed below:

| Library            | Purpose                                                                 |
|--------------------|-------------------------------------------------------------------------|
| `playsound==1.2.2` | Play audio files (e.g., welcome sound, feedback).                      |
| `pyaudio`          | Capture microphone input for speech recognition.                      |
| `speech_recognition` | Convert spoken commands to text using Google's Speech-to-Text API.   |
| `pyttsx3`          | Text-to-speech for giving verbal responses.                           |
| `pywhatkit`        | Play YouTube videos based on text/voice input.                        |
| `webbrowser`       | Open links and perform web-based searches.                            |
| `os`               | Launch applications installed on the system.                         |
| `eel`              | Create an interactive web interface; connects frontend and backend.   |
| `groq`             | Interface with Groq API for intelligent LLM-based answers.           |
| `time`             | Manage execution delays for smoother UX.                             |

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For any questions or suggestions, feel free to open an issue or contact the maintainer:
[Prabhjot Singh](https://github.com/Prabh10p)
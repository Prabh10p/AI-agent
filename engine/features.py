import os
import webbrowser
from playsound import playsound
import eel
import time
import psutil
import pyautogui
from engine.command import speak, takecommand
from engine.config import *
import pywhatkit as kit
from engine.helper import extract_yt_term
from groq import Groq  # Import Groq for language model API
import platform
from datetime import datetime
import requests 

# Initialize Groq client with API key
client = Groq(
    api_key="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"
)

@eel.expose
def playAssistantSound():
    music_dir = "www/assets/audio/start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "").strip().lower()
    query = query.replace("open", "").strip().replace("search", "").strip()

    if "play" in query or "on youtube" in query:
        search_term = query.replace("on youtube", "").replace("play", "").strip()
        if search_term:
            try:
                speak(f"Playing {search_term} on YouTube")
                kit.playonyt(search_term)
            except Exception as e:
                speak(f"Sorry, I couldn't play {search_term}. Error: {e}")
        else:
            speak("What would you like to play on YouTube?")
    elif "on google" in query:
        search_term = query.replace("on google", "").strip()
        if search_term:
            url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
            speak(f"Searching for {search_term} on Google")
            webbrowser.open(url)
        else:
            speak("What would you like to search for on Google?")
    else:
        try:
            speak(f"Opening {query}")
            os.system(f'open -a "{query}"')  # macOS-specific
        except Exception:
            if query:
                url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
                speak(f"Searching for {query} on Google")
                webbrowser.open(url)
            else:
                speak("What would you like to search for?")

def chatBot(query):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": query}],
        model="llama3-8b-8192",
    )
    response = chat_completion.choices[0].message.content
    print(response)
    speak(response)
    return response
def get_system_performance():
    """Fetch and display system performance data like CPU, memory, and disk usage."""
    try:
        # Get CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        # Get memory usage
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        # Get disk usage
        disk = psutil.disk_usage('/')
        disk_usage = disk.percent
        
        # Display the stats in a human-readable way
        speak(f"System Performance: CPU usage is {cpu_usage}%")
        speak(f"Memory usage is {memory_usage}% of {memory.total / (1024 ** 3):.2f} GB")
        speak(f"Disk usage is {disk_usage}% of {disk.total / (1024 ** 3):.2f} GB")
        
    except Exception as e:
        speak("Sorry, I couldn't fetch the system performance data.")
        print(f"Error: {e}")
def systemCommands(query):
    """Handles system-level commands like restart, shutdown, and system info."""
    if "restart system" in query:
        try:
            os.system("shutdown /r /t 0" if platform.system() == "Windows" else "sudo reboot")
            speak("Restarting the system.")
        except Exception as e:
            speak(f"Failed to restart the system: {e}")
    elif "shutdown system" in query:
        try:
            os.system("shutdown /s /t 0" if platform.system() == "Windows" else "sudo shutdown now")
            speak("Shutting down the system.")
        except Exception as e:
            speak(f"Failed to shut down the system: {e}")
    elif "system info" in query:
        info = f"System: {platform.system()}, Version: {platform.version()}, Processor: {platform.processor()}"
        speak(info)
        return info
    elif "time" in query:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    else:
        speak("System command not recognized.")

@eel.expose
def automateTask(task_query):
    task_query = task_query.lower()

    try:
        # **1. Typing Text**
        if "type" in task_query:
            message = task_query.replace("type", "").strip()
            pyautogui.write(message)
            pyautogui.press('enter')
            speak(f"Typed: {message}")
        
        # **2. Take Screenshot**
        elif "screenshot" in task_query:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot saved as screenshot.png")
        
        # **3. Scrolling**
        elif "scroll down" in task_query:
            pyautogui.scroll(-500)
            speak("Scrolled down")
        elif "scroll up" in task_query:
            pyautogui.scroll(500)
            speak("Scrolled up")
        
        # **4. Adjusting Volume**
        elif "volume up" in task_query:
            pyautogui.press("volumeup", presses=5)
            speak("Volume increased")
        elif "volume down" in task_query:
            pyautogui.press("volumedown", presses=5)
            speak("Volume decreased")
        elif "mute" in task_query:
            pyautogui.press("volumemute")
            speak("Volume muted")
        
        # **5. Lock Screen**
        elif "lock screen" in task_query:
            if os.name == "nt":  # Windows
                os.system("rundll32.exe user32.dll,LockWorkStation")
            elif os.name == "posix":  # macOS/Linux
                os.system("/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession -suspend")
            speak("Screen locked.")
        
        # **6. Open Applications**
        elif "open" in task_query:
            app_name = task_query.replace("open", "").strip()
            if os.name == "nt":  # Windows
                os.system(f"start {app_name}")
            elif os.name == "posix":  # macOS/Linux
                os.system(f"open -a {app_name}")
            speak(f"Opening {app_name}.")
        
        # **7. Close Applications**
        elif "close" in task_query:
            app_name = task_query.replace("close", "").strip()
            if os.name == "nt":  # Windows
                os.system(f"taskkill /IM {app_name}.exe /F")
            elif os.name == "posix":  # macOS/Linux
                os.system(f"pkill {app_name}")
            speak(f"Closed {app_name}.")
        
        # **8. File Operations**
        elif "create file" in task_query:
            file_name = task_query.replace("create file", "").strip() + ".txt"
            with open(file_name, "w") as file:
                file.write("File created by the assistant.")
            speak(f"Created file: {file_name}")
        elif "delete file" in task_query:
            file_name = task_query.replace("delete file", "").strip()
            if os.path.exists(file_name):
                os.remove(file_name)
                speak(f"Deleted file: {file_name}")
            else:
                speak(f"File {file_name} not found.")
        
        # **9. Send Keystrokes**
        elif "press" in task_query:
            key = task_query.replace("press", "").strip()
            pyautogui.press(key)
            speak(f"Pressed {key}.")
        
        # **10. System Restart/Shutdown**
        elif "restart system" in task_query:
            # Using `sudo` without a password
            os.system("sudo /sbin/reboot")
            speak("Restarting system.")
        elif "shutdown system" in task_query:
            # Using `sudo` without a password
            os.system("sudo /sbin/shutdown -h now")
            speak("Shutting down system.")
        
        # **11. Fetch Date and Time**
        elif "time" in task_query:
            current_time = datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}.")
        elif "date" in task_query:
            current_date = datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}.")
        
        # **12. Open Websites**
        elif "open website" in task_query:
            site_name = task_query.replace("open website", "").strip()
            webbrowser.open(f"https://{site_name}")
            speak(f"Opening website {site_name}.")
        
        # **13. Search Google**
        elif "search" in task_query:
            search_term = task_query.replace("search", "").strip()
            url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}"
            webbrowser.open(url)
            speak(f"Searching for {search_term} on Google.")
        
        # Default Response
        else:
            speak("Task not recognized. Please try again.")
    except Exception as e:
        speak(f"An error occurred: {e}")


@eel.expose
def allCommands(message=1):
    """Routes commands to the appropriate function."""
    if message == 1:
        query = takecommand()  # Take voice command
        if not query:
            eel.DisplayMessage("I didn't catch that. Could you repeat?")
            return
        eel.senderText(query)  # Display user command in UI
    else:
        query = message
        eel.senderText(query)
    
    try:
        # Specific command handling
        if "check system performance" in query or "check my computer stats" in query:
            get_system_performance() 
            return
        if "lock screen" in query:
            automateTask(query)
            return
        elif "volume up" in query or "volume down" in query or "mute" in query:
            automateTask(query)
            return
        elif "create file" in query or "delete file" in query:
            automateTask(query)
        
        # Handle current date and time separately
        elif "current date" in query:
            # Call function to get current date
            current_date = datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}.")
        elif "time" in query:
            # Call function to get current time
            current_time = datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}.")
        
        elif "screenshot" in query or "automate" in query:
            automateTask(query)
        elif "open" in query or "play" in query or "on youtube" in query:
            openCommand(query)
        elif "restart" in query or "shutdown" in query or "system info" in query:
            systemCommands(query)
        else:
            chatBot(query)
    except Exception as e:
        print(f"Error occurred: {e}")

    eel.ShowHood()

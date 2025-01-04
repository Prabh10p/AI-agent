// settings.js

// Dark mode toggle functionality
const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

darkModeToggle.addEventListener('change', () => {
    if (darkModeToggle.checked) {
        body.classList.add('dark-mode');
        localStorage.setItem('darkMode', 'true'); // Save dark mode preference
    } else {
        body.classList.remove('dark-mode');
        localStorage.setItem('darkMode', 'false');
    }
});

// Load dark mode setting on page load
window.addEventListener('load', () => {
    if (localStorage.getItem('darkMode') === 'true') {
        darkModeToggle.checked = true;
        body.classList.add('dark-mode');
    }
});

// Voice Settings (Dummy Functionality)
const voiceSelect = document.getElementById('voiceSelect');
voiceSelect.addEventListener('change', () => {
    const selectedVoice = voiceSelect.value;
    console.log(`Selected voice: ${selectedVoice}`);
    // You can implement TTS engine logic here (like changing voice in your app)
});

// Login Button (Dummy Functionality)
const loginButton = document.getElementById('loginButton');
loginButton.addEventListener('click', () => {
    alert("Login functionality here!");
});

// Open/Close Settings Modal
const settingsButton = document.getElementById('settingsButton');
const settingsModal = document.getElementById('settingsModal');
const closeSettingsButton = document.getElementById('closeSettingsButton');

settingsButton.addEventListener('click', () => {
    settingsModal.style.display = 'block';
});

closeSettingsButton.addEventListener('click', () => {
    settingsModal.style.display = 'none';
});

# Python Alarm Clock

This is a simple Python-based alarm clock where you can set a specific time in the format `HH:MM:SS`, and when the time arrives, a sound is played as an alert.

## Features
- Set a custom alarm time.
- Displays the current time in the terminal.
- Plays a sound when the alarm time is reached.
- Colored output in the terminal using `colorama`.

## Libraries Used
- `pygame` for playing the alarm sound.
- `colorama` for terminal output coloring.
- `time` and `datetime` for managing time.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/paomfarv/clialarmclock.git
    cd clialarmclock
    ```

2. Install the required libraries:
    ```bash
    pip install pygame colorama
    ```

3. Place your preferred alarm sound file (e.g., `Alarmsound.mp3`) in the same directory as the script.

4. Run the script:
    ```bash
    python clialarmclock
    ```

## Usage
1. Run the script and set the alarm time when prompted.
2. Wait for the alarm to trigger at the set time. Press `Enter` to stop the sound.

## License
MIT License. Feel free to fork and contribute!


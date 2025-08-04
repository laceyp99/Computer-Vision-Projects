# Playlist Hand Gesture Control

A computer vision application that uses hand gestures to control media playback and system volume through webcam input. Built with OpenCV and MediaPipe for real-time hand tracking and gesture recognition.

## Features

- **Volume Control**: Use one finger gesture with hand movement to adjust system volume
- **Play/Pause**: Open palm gesture (4+ fingers) to toggle media playback
- **Track Navigation**: Two-finger gesture with hand positioning to skip to next/previous track
- **Real-time Hand Tracking**: Live webcam feed with hand landmark visualization
- **Gesture Feedback**: Visual indicators showing current gesture mode and system status

## Demo

The application recognizes the following gestures:

| Gesture | Action | Description |
|---------|--------|-------------|
| 1 Finger | Volume Control | Move hand up/down to increase/decrease volume |
| 4+ Fingers (Open Palm) | Play/Pause | Toggle media playback |
| 2 Fingers + Right Position | Next Track | Skip to next song (press 'L' key) |
| 2 Fingers + Left Position | Previous Track | Skip to previous song (press 'J' key) |

## Requirements

- Python 3.10
- Webcam
- Windows OS (for volume control functionality)

## Dependencies

Install the required packages using pip:

```bash
pip install opencv-python
pip install mediapipe
pip install pycaw
pip install keyboard
pip install pyautogui
pip install comtypes
```

Or create a virtual environment and install from the project directory:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt  # (if available)
```

## Installation

1. Clone this repository:
```bash
git clone https://github.com/laceyp99/Computer-Vision-Projects.git
cd "Computer-Vision-Projects/Playlist Hand Gesture Control"
```

2. Install dependencies (see Requirements section above)

3. Run the application:
```bash
python main.py
```

## Usage

1. **Start the Application**: Run `python main.py`
2. **Position Yourself**: Ensure your hand is visible in the webcam feed
3. **Use Gestures**:
   - Hold up **1 finger** and move your hand up/down for volume control
   - Show **open palm (4+ fingers)** to play/pause media
   - Hold up **2 fingers** and position your hand on the right side of the screen to skip forward
   - Hold up **2 fingers** and position your hand on the left side of the screen to skip backward
4. **Exit**: Press 'q' to quit the application

## How It Works

### Hand Detection
- Uses MediaPipe Hands for real-time hand landmark detection
- Processes webcam feed at 30fps with mirrored display
- Tracks 21 hand landmarks with configurable confidence thresholds

### Gesture Recognition
- **Finger Counting**: Compares finger tip positions to PIP joints (landmarks 8, 12, 16, 20)
- **Volume Control**: Tracks wrist Y-coordinate movement over time using a rolling average
- **Position Detection**: Uses wrist X-coordinate to determine left/right hand positioning

### System Integration
- **Volume Control**: Uses PyCaw library to interface with Windows Core Audio APIs
- **Media Control**: Leverages keyboard library for media key simulation
- **Track Navigation**: Sends 'J' and 'L' key presses (common media player shortcuts)

## File Structure

```
Playlist Hand Gesture Control/
├── main.py          # Main application with gesture recognition logic
├── actions.py       # System integration functions (volume, media control)
├── README.md        # Project documentation
└── __pycache__/     # Python cache files
```

## Configuration

### Gesture Sensitivity
You can adjust gesture sensitivity by modifying these parameters in `main.py`:

- `min_detection_confidence=0.7`: Hand detection confidence threshold
- `min_tracking_confidence=0.7`: Hand tracking confidence threshold
- `cooldown_duration = 1.0`: Time between gesture actions (seconds)
- `volume_level += 6`: Volume change increment per gesture

### Position Thresholds
- `right_threshold = frame.shape[1] * 0.8`: Right side boundary (80% of screen width)
- `left_threshold = frame.shape[1] * 0.2`: Left side boundary (20% of screen width)

## Troubleshooting

### Performance Optimization

- Close unnecessary applications to improve webcam performance
- Ensure good lighting for better hand detection
- Keep hand within webcam frame for consistent tracking
# Cold Turkey Blocker Activator

A simple Python script that activates the pro version of Cold Turkey Blocker.

## Requirements

- Python 3.x
- Cold Turkey Blocker must be installed on your system
- Windows operating system

## Usage

1. Make sure Cold Turkey Blocker is installed on your system
2. Run the script:
   ```
   python coldturkeyblocker-activator.py
   ```
3. The script will:
   - Check if Cold Turkey Blocker is installed
   - If installed, activate the pro version
   - Prompt you to restart Cold Turkey Blocker after activation
4. Press any key to exit the script

## How it Works

The script modifies Cold Turkey Blocker's SQLite database to enable pro features. It:
- Connects to Cold Turkey's database at `C:/ProgramData/Cold Turkey/data-app.db`
- Updates the pro status in the settings
- Saves the changes to the database

## Note

This script is for educational purposes only. Please support software developers by purchasing legitimate licenses for their products.

## Requirements File

Check `requirements.txt` for any required Python packages.

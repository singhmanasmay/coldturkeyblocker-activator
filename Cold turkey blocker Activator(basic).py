# Import required modules
import sqlite3  # For database operations
import json     # For parsing JSON data
import os       # For file/path operations
import msvcrt   # For handling keyboard input on Windows

init= True
if os.path.exists(os.path.join(os.environ['WINDIR'],'SYSTEM32')):
    system32exists = True
else: system32exists = False

if init:
    init = False
    print('\n'.join(['██████╗░░█████╗░██╗░░░░░███████╗██████╗░░░███╗░░░█████╗░███╗░░██╗',
                     '██╔══██╗██╔══██╗██║░░░░░██╔════╝██╔══██╗░████║░░██╔══██╗████╗░██║',
                     '██████╦╝███████║██║░░░░░█████╗░░██████╔╝██╔██║░░██║░░██║██╔██╗██║',
                     '██╔══██╗██╔══██║██║░░░░░██╔══╝░░██╔══██╗╚═╝██║░░██║░░██║██║╚████║',
                     '██████╦╝██║░░██║███████╗███████╗██║░░██║███████╗╚█████╔╝██║░╚███║',
                     '╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝','https://github.com/singhmanasmay','\n']))
    print(f'system32 exists= {system32exists}\n')
if not system32exists:
    print('Unsupported OS\nPlease ensure you are running this script on a Windows system.\nPress any key to continue...')
    msvcrt.getch()  # Wait for user input before closing
    quit()

# Define the path to Cold Turkey's SQLite database
DB_PATH = r"C:/ProgramData/Cold Turkey/data-app.db"

# Check if the database file exists
if os.path.exists(DB_PATH):
    # Connect to the SQLite database
    connector = sqlite3.connect(DB_PATH)
    cursor = connector.cursor()
    
    # Retrieve settings data from the database and parse JSON
    data = json.loads(cursor.execute("SELECT value FROM settings WHERE key = 'settings'").fetchone()[0])

    # Check if the program is already activated
    if data["additional"]["proStatus"] != "pro":
        # Update the activation status to pro
        data["additional"]["proStatus"] = "pro"
        # Save changes back to the database
        cursor.execute("""UPDATE settings SET value = ? WHERE "key" = 'settings'""", (json.dumps(data),))
        connector.commit()
        print('Cold turkey blocker activated.\nPlease restart cold turkey blocker.\nPress any key to continue...')
    else:
        print('Cold turkey blocker already activated.\nPress any key to continue...')

    # Close the database connection
    connector.close()

else:
    print('Cold turkey blocker is not installed.\nPress any key to continue...')

# Wait for user input before closing
msvcrt.getch()
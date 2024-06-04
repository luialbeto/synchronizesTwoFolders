# synchronizesTwoFolders
Synchronizes Two Folders with Python

Quick Start

- git clone this repo
- run the following command (change the path to referred folder)-> sudo python synchronizes.py /path/to/synchronizesTwoFolders /path/to/synchronizesTwoFolders/replica 60 /path/to/synchronizesTwoFolders/logfile.log

Notes:
-  The main function directly calls synchronize_folders with the parsed arguments
-   The setup_logging function is called within synchronize_folders to ensure proper logging configuration before synchronization starts
-   The synchronize_folders function takes all necessary parameters (source, replica, interval, log_file)

Have fun! 

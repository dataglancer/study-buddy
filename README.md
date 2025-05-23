# Study Buddy

A simple terminal-based flash-card-style quiz. Nothing fancy.

Features:
- Randonly grabs a term and shuffles the correct definition with 3 other random definitions to select from. 
- Tracks grade with simple % correct per session. 


The terms and results use terminal color package 'colorama', you might need to install this on you local system's environment.

## Usage

Set permissions after the first use:
1. `chmod +x study_buddy.py`  

Run pointing at your terms csv fil
2. `./study_buddy.py path/to/terms.csv`

# Startup 
Select either quiz or flashcard mode. 

# Quiz mode
Randonmly selects a term and presents the correct answer along with 3 randonly chosen definitions.

# Flashcard mode
Presents a term and waits for any key press to present the definition. 

## CSV format
Standard UTF-8 CSV format. No headers. 

Example:

Term, Definition 




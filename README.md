# Study Buddy

A simple terminal-based flash-card-style quiz. Nothing fancy.

Features:
- Randonly grabs a term and shuffles the correct definition with 3 other random definitions to select from. 
- Tracks grade with simple % correct per session. 


The terms and results use terminal color package 'colorama', you might need to install this on you local system's environment.

## Usage

1. `chmod +x study_buddy.py`  
2. `./study_buddy.py path/to/terms.csv`

## CSV format
Standard CSV format. No headers. Example:

Term, Definition 




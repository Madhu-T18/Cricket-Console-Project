# 🏏 Cricket Tournament Manager

A Python console-based project built using all 4 OOP concepts with SQLite database.

## OOP Concepts Used

| Concept | Where Used |
|---|---|
| Abstraction | Person abstract base class using ABC |
| Encapsulation | Private __variables with @property |
| Inheritance | Batsman, Bowler, AllRounder inherit from Player |
| Polymorphism | get_role() and display_stats() overridden in each class |

## Folder Structure
```
Cricket-Console/
├── main.py
├── database/
│   └── db_manager.py
├── models/
│   ├── person.py
│   ├── player.py
│   └── team.py
├── match/
│   └── match.py
├── exceptions/
│   └── errors.py
└── manager/
    └── tournament_manager.py
```

## Features

- Add Teams and Players
- Play Match with auto simulation
- Points Table
- Player Stats
- Match Results with Man of the Match
- SQLite persistent storage

## How to Run
```bash
git clone https://github.com/Madhu-T18/Cricket-Console-Project
cd Cricket-Console-Project
python main.py
```

No external libraries needed — only built-in sqlite3, random, abc

## Tech Stack

- Language: Python 3
- Database: SQLite3
- Concepts: OOP, Exception Handling, File Persistence

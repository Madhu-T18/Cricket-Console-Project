🏏 Cricket Tournament Manager
A Python console-based Cricket Tournament Manager built using all 4 OOP concepts — Encapsulation, Inheritance, Polymorphism, and Abstraction — with SQLite database for persistent storage.

📌 OOP Concepts Used
ConceptWhere UsedAbstractionPerson abstract base class using ABC and @abstractmethodEncapsulationPrivate __variables in all classes with @property gettersInheritanceBatsman, Bowler, AllRounder inherit from Player → PersonPolymorphismget_role() and display_stats() overridden in each player class

📁 Folder Structure
Cricket-Console/
│
├── main.py                          ← Entry point, main menu
│
├── database/
│   ├── __init__.py
│   └── db_manager.py                ← DatabaseManager class (SQLite CRUD)
│
├── models/
│   ├── __init__.py
│   ├── person.py                    ← Abstract base class Person
│   ├── player.py                    ← Player, Batsman, Bowler, AllRounder
│   └── team.py                      ← Team class
│
├── match/
│   ├── __init__.py
│   └── match.py                     ← Match simulation logic
│
├── exceptions/
│   ├── __init__.py
│   └── errors.py                    ← Custom exceptions
│
├── manager/
│   ├── __init__.py
│   └── tournament_manager.py        ← Main controller, all menu actions
│
├── cricket_tournament.db            ← Auto-created SQLite database
└── README.md

⚙️ Features

Add Teams
Add Players (Batsman / Bowler / All-Rounder)
Play Match (auto simulation with random scores)
View Points Table
View Player Stats (Top Batsmen & Bowlers)
View Match Results with Man of the Match
View All Squads
Persistent data storage using SQLite


🗄️ Database Tables
TableDescriptionteamsStores all team namesplayersStores player name, role, runs, wickets, matchesmatchesStores match results, scores, Man of the Matchpoints_tableStores played, won, lost, points per team

🚀 How to Run
1. Clone the repository 
git clone https://github.com/Madhu-T18/Cricket-Console-Project
cd Cricket-Console
3. Run the project
bashpython main.py

No external libraries needed — only built-in sqlite3, random, abc


🎮 How to Use
1. Add Team       → Enter team name (e.g. Rcb, Csk)
2. Add Player     → Select team, enter player name, choose role
                    1. Batsman   2. Bowler   3. All-Rounder
3. Play Match     → Enter Team 1 and Team 2 names
4. Points Table   → View rankings
5. Player Stats   → Top 5 batsmen and bowlers
6. Match Results  → All played matches with scores
7. View Squads    → All players in each team
0. Exit

🧱 Class Structure
Person  (ABC - Abstract)
└── Player
    ├── Batsman       (simulate_innings)
    ├── Bowler        (simulate_bowling)
    └── AllRounder    (both)

Team
Match
DatabaseManager
TournamentManager
TournamentError (Custom Exception)
├── TeamNotFoundError
└── NotEnoughPlayersError

🛠️ Tech Stack

Language: Python 3
Database: SQLite3 (built-in)
Concepts: OOP, Exception Handling, File Persistence
IDE: VS Code


👨‍💻 Author
MADHU T
B.Tech AIML | Python OOP Console Project

from manager.tournament_manager import TournamentManager

def main():
    print("\n  🏏  CRICKET TOURNAMENT MANAGER  🏏\n")
    mgr = TournamentManager()
    mgr.restore_session()

    options = [
        ("1", "Add Team",        mgr.add_team),
        ("2", "Add Player",      mgr.add_player),
        ("3", "Play Match",      mgr.play_match),
        ("4", "Points Table",    mgr.view_points_table),
        ("5", "Player Stats",    mgr.view_player_stats),
        ("6", "Match Results",   mgr.view_match_results),
        ("7", "View Squads",     mgr.view_squads),
        ("0", "Exit",            None),
    ]

    while True:
        print("\n  ┌──────────────────────────┐")
        for k, label, _ in options:
            print(f"  │  {k}. {label:<22}│")
        print("  └──────────────────────────┘")

        choice = input("  Choice: ").strip()
        if choice == "0":
            mgr.close()
            print("  Goodbye! 🏏"); break

        action = next((fn for k, _, fn in options if k == choice and fn), None)
        if action:
            try:
                action()
            except Exception as e:
                print(f"  ✘  {e}")
        else:
            print("  ✘  Invalid choice.")

if __name__ == "__main__":
    main()

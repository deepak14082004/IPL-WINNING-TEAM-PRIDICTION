# ipl_live_win_predictor.py

import math  # In case you expand the logic
import pandas as pd  # For future data usage
import numpy as np   # For numerical calculations

def predict_win_probability(batting_team, bowling_team, target, score, overs, wickets):
    # Constants
    total_overs = 20
    balls_bowled = int(overs * 6)
    balls_left = (total_overs * 6) - balls_bowled
    runs_left = target - score
    current_run_rate = score / overs if overs > 0 else 0
    required_run_rate = runs_left / (balls_left / 6) if balls_left > 0 else float('inf')

    print("\n--- Match Situation ---")
    print(f"Batting Team       : {batting_team}")
    print(f"Bowling Team       : {bowling_team}")
    print(f"Target             : {target}")
    print(f"Score              : {score}/{wickets} in {overs} overs")
    print(f"Runs Left          : {runs_left}")
    print(f"Balls Left         : {balls_left}")
    print(f"Current Run Rate   : {current_run_rate:.2f}")
    print(f"Required Run Rate  : {required_run_rate:.2f}")

    # Simple heuristic-based win probability
    win_prob = 50

    # Adjust probability based on scoring rate
    if required_run_rate > current_run_rate:
        win_prob -= (required_run_rate - current_run_rate) * 5
    else:
        win_prob += (current_run_rate - required_run_rate) * 4

    # Penalize for wickets lost
    win_prob -= wickets * 3

    # Clamp between 0 and 100
    win_prob = max(0, min(100, win_prob))

    print("\n--- Win Probability ---")
    print(f"{batting_team} win chance : {win_prob:.2f}%")
    print(f"{bowling_team} win chance : {100 - win_prob:.2f}%")


# Main driver
if __name__ == "__main__":
    print("🏏 IPL Live Win Predictor\n")
    batting_team = input("Enter Batting Team: ")
    bowling_team = input("Enter Bowling Team: ")
    target = int(input("Enter Target Score: "))
    score = int(input("Enter Current Score: "))
    overs = float(input("Enter Overs Completed: "))
    wickets = int(input("Enter Wickets Lost: "))

    predict_win_probability(batting_team, bowling_team, target, score, overs, wickets)

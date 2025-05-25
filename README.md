🏏 IPL Live Win Predictor – Python CLI Tool
This is a simple Python-based command-line tool that predicts the win probability for a batting team in an IPL match based on the current match situation.

🔮 Features
Input real-time match details:

Batting and Bowling teams

Target score

Current score

Overs completed

Wickets lost

Calculates:

Runs left

Balls remaining

Current and required run rate

Predicted win probability using a basic heuristic formula


$ python ipl_live_win_predictor.py

🏏 IPL Live Win Predictor

Enter Batting Team: CSK
Enter Bowling Team: MI
Enter Target Score: 180
Enter Current Score: 90
Enter Overs Completed: 10
Enter Wickets Lost: 3

--- Match Situation ---
Batting Team       : CSK
Bowling Team       : MI
Target             : 180
Score              : 90/3 in 10.0 overs
Runs Left          : 90
Balls Left         : 60
Current Run Rate   : 9.00
Required Run Rate  : 9.00

--- Win Probability ---
CSK win chance     : 41.00%
MI win chance      : 59.00%



🛠 Technologies Used
Python 3.x

Standard Python libraries (math, pandas, numpy – for future extensibility)

🚀 Future Enhancements
Integrate live data APIs

Add a machine learning model trained on historical match data

Build a web version using Flask or Streamlit

Add graphical win probability curve over time

🤝 Contributing
Contributions, ideas, and feedback are welcome! Feel free to fork the repo, raise issues, or submit pull requests.

📄 License
This project is open-source and available under the MIT License.

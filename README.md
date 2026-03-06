
The Internet Speed Test Application is a simple Python program that allows users to measure their internet connection speed directly from the command line.
It calculates:

Download speed (how fast data is received from the internet)

Upload speed (how fast data is sent to the internet)

Ping/Latency (response time to a server)

This tool is useful for quickly checking network performance, troubleshooting connectivity issues, or comparing internet plans.

Features

Measures Download Speed in Mbps

Measures Upload Speed in Mbps

Displays Ping (Latency) in milliseconds

Lightweight and easy to run

Built entirely in Python with minimal dependencies

Technologies Used

Python 3.x – Core programming language

speedtest-cli
 – Python library to access Speedtest.net

Installation
1. Clone the repository
git clone https://github.com/dronamadhuri/speedtest-app.git
2. Navigate to the project folder
cd speedtest-app
3. Install dependencies

If you don’t have speedtest-cli installed globally, you can install it using:

pip install -r requirements.txt

Or directly:

pip install speedtest-cli
Run the Application

Simply run:

python speed_test.py

The program will display the internet speed in real-time.

Example Output
Checking Internet Speed...
Download Speed: 85.32 Mbps
Upload Speed: 41.18 Mbps
Ping: 12.3 ms

Usage Tips

Make sure you are connected to the internet before running the script.

Run multiple times at different times of the day to get accurate averages.

Use a wired connection for more precise measurements if possible.

Contributing

Feel free to fork this project and submit pull requests.
Suggestions, bug reports, and improvements are always welcome.

Author

Drona Madhuri Dadi
CSE (AI & ML) Student
Keshav Memorial Institute of Technology

print("A online webpage with Front-end login based GPS tracker system.")
print("- Designed using HTML, CSS, and SQLite")
print("- Tracks the location of the bus route with latitude and longitude from Google Maps APIs.")
print("Other contributors")

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "CICD PIPELINE SAMPLE FOR A PROJECT "

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)

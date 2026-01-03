from dashboard import launchDashboard
from data import loadYears

if __name__ == "__main__":
    loadYears()
    
    app = launchDashboard()
    app.run(debug=True)
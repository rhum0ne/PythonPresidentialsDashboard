from src.dashboard import launchDashboard
from src.data import loadYears

if __name__ == "__main__":
    loadYears()
    
    app = launchDashboard()
    app.run(debug=True)
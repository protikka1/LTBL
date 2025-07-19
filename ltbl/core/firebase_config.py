# Make sure you have installed pyrebase4: pip install pyrebase4
# If you still get 'Import "pyrebase" could not be resolved',
# try restarting your IDE or Python environment.
try:
    # If you see "Import 'pyrebase' could not be resolved",
    # ensure you installed pyrebase4:
    # pip install pyrebase4
    # If using a virtual environment, make sure it's activated in your IDE/
    # terminal.
    import pyrebase  # 'pyrebase4' installs as 'pyrebase'
except ImportError as e:
    raise ImportError(
        "pyrebase is not installed or not found in your environment. "
        "Please run 'pip install pyrebase4' and ensure your IDE or terminal "
        "is using the correct Python interpreter/virtual environment."
    ) from e

firebaseConfig = {
    "apiKey": "Yda150ce7e0795876538249ae8",
    "authDomain": "groovy-overview-465805-g6.firebaseapp.com",
    "databaseURL": "https://groovy-overview-465805-g6firebaseio.com",
    "projectId": "groovy-overview-465805-g6",
    "storageBucket": "Ygroovy-overview-465805-g6.appspot.com",
    "messagingSenderId": "275766846255",
    "appId": "Y1:275766846255:web:d19db1c6dabf6ef892b7da",
    "measurementId": "YOUR_MEASUREMENT_ID"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

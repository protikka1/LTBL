# Make sure you have installed pyrebase4: pip install pyrebase4
# If you still get 'Import "pyrebase" could not be resolved',
# try restarting your IDE or Python environment.
try:
    # 'pyrebase4' installs as 'pyrebase'
    import pyrebase
    # Make sure 'pyrebase4' is installed: pip install pyrebase4
except ImportError as e:
    raise ImportError(
        "pyrebase is not installed or not found in your environment. "
        "Please run 'pip install pyrebase4' and ensure your IDE or terminal "
        "is using the correct Python interpreter/virtual environment."
    ) from e

firebaseConfig = {
  "apiKey": "AIzaSyBnCU7Sp4Y-OIrfE3T-xi3I96Tm3rWiyJw",
  "authDomain": "groovy-overview-465805-g6.firebaseapp.com",
  "projectId": "groovy-overview-465805-g6",
  "storageBucket": "groovy-overview-465805-g6.firebasestorage.app",
  "messagingSenderId": "275766846255",
  "appId": "1:275766846255:web:d19db1c6dabf6ef892b7da",
  "measurementId": "G-H545KBNY66"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
db = firebase.database()
storage = firebase.storage()

# backend/config_template.py
# Copy this file to backend/config.py and fill values there.
# Do NOT commit backend/config.py to your public repo.

# DB settings
DB_TYPE = "sqlite"   # "sqlite" or "mysql"

# If using sqlite (recommended for demo)
SQLITE_DB_PATH = "data/parking_demo.db"

# If using mysql (only for production / not required for demo)
MYSQL = {
    "host": "localhost",
    "user": "your_mysql_user",
    "password": "your_mysql_password",
    "database": "car",
    "port": 3306,
}

# Notification / SMS (demo-safe placeholder)
FAST2SMS_API_KEY = "YOUR_FAST2SMS_API_KEY"  # replace locally if you want actual SMS (do not commit)

# UPI / payment
UPI_ID = "your_upi@bank"


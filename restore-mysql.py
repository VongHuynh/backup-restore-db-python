import os
import pipes

# MySQL database details for the restore process
DB_HOST = '<your_db_host>'
DB_USER = 'your_db_user'
DB_USER_PASSWORD = 'your_db_password'
DB_NAME = 'your_db_name'

BACKUP_PATH = os.path.join(os.getcwd(), 'db_backup')
# Function to restore a MySQL database from a backup file
def restore_database(filename):
    restore_cmd = "mysql -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " < " + pipes.quote(filename)
    os.system(restore_cmd)

# Prompt user to enter the backup filename
backup_file = input("Enter the backup file name (including the file extension): ")

# Check if the backup file exists
backup_path = os.path.join(BACKUP_PATH, backup_file)
if os.path.exists(backup_path):
    # Perform the database restore
    print("Starting database restore...")
    restore_database(backup_path)
    print("Database restore completed successfully.")
else:
    print("Backup file not found. Please make sure the file exists in the backup directory.")

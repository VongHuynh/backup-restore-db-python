# Import required python libraries
 
import os
import time
import datetime
import pipes
 
DB_HOST = '<your_db_host>'
DB_USER = 'your_db_user'
DB_USER_PASSWORD = 'your_db_password'
DB_NAME = 'your_db_name'

BACKUP_PATH = os.path.join(os.getcwd(), 'db_backup')
# Getting current DateTime to create the separate backup folder like "20180817-123433".
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH

def backup_script(file_name):
    dumpcmd = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + file_name + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
    os.system(dumpcmd)

def compress_file(file_name):
    gzipcmd = "gzip " + pipes.quote(TODAYBACKUPPATH) + "/" + file_name + ".sql"
    os.system(gzipcmd)
 
# Checking if backup folder already exists or not. If not exists will create it.
if not os.path.exists(BACKUP_PATH):
    os.makedirs(BACKUP_PATH)
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)
 
# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
print ("checking for databases names file.")
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print ("Databases file found...")
    print ("Starting backup of all dbs listed in file " + DB_NAME)
else:
    print ("Databases file not found...")
    print ("Starting backup of database " + DB_NAME)
    multi = 0
 
# Starting actual database backup process.
if multi:
   in_file = open(DB_NAME,"r")
   flength = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(DB_NAME,"r")
 
   while p <= flength:
       db = dbfile.readline()   # reading database name from file
       db = db[:-1]         # deletes extra line
       backup_script(db)
       #compress_file(db)
       p = p + 1
   dbfile.close()
else:
   db = '/backup_'+DB_NAME+'_'+DATETIME
   backup_script(db)
   #compress_file(db)
print ("Backup script completed")
print ("Your backups have been created in '" + TODAYBACKUPPATH + "' directory")
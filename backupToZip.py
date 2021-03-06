# Tool name         :backupToZip
# Module name       :backupToZip.py
# Detail            :This's the tool to copy all directories to Zip file
# Implementer       :R.Ishikawa
# Version           :1.3
# Last update       :2019/11/12

#Version History
 #1 Create New                                        R.I  Ver.1.0  2017/12/01
 #2 Set path and some comments                        R.I  Ver.1.1  2017/12/24
 #3 Set mv operation & command line arguments         R.I  Ver.1.2  2018/06/02
 #4 Set check directories including args[1] & args[2] R.I  Ver.1.3  2019/11/12 

import zipfile, os, shutil
import sys

args = sys.argv
argc = len(args)

# The procedure in the case arguments' length is not enough(#3)
if(argc != 3):
   print('')
   print('backupToZip Usage:')
   print('args[1]: Set abusolute path included files and directories you want to back up')
   print('args[2]: Set abusolute path you want to put zipfile')
   print('')
   quit()

def backup_to_zip(folder):
           # Back up all directories to Zip file
           folder = os.path.abspath(folder) # set absolute path

           number = 1
           while True:
                      zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
                      if not os.path.exists(zip_filename):
                                 break
                      number = number + 1

           # Create Zip file
           print('Creating {}...'.format(zip_filename))
           backup_zip = zipfile.ZipFile(zip_filename, 'w')
 	   
 	   # Searching directory tree and compressing file
           for foldername, subfolders, filenames in os.walk(folder):
                      print('Adding files in {}...'.format(foldername))
                      # Add current directory to Zip file
                      backup_zip.write(foldername)
                      # Add all files of current directory to Zip file
                      for filename in filenames:
                                 new_base = os.path.basename(folder) + '_'
                                 if filename.startswith(new_base) and filename.endswith('.zip'):
                                            continue
                                 backup_zip.write(os.path.join(foldername, filename))
           backup_zip.close()
           
           # Set abusolute path you want to put zipfile
           shutil.move(zip_filename,args[2])
           print('Done. ')


if os.path.exists(args[1]) and os.path.exists(args[2]):
   # Set path included files and directories you want to back up
   backup_to_zip(args[1])
else:
   # If paths including args[1] and args[2] are not exist
   # The following message is raised
   print('Directory not found. ')

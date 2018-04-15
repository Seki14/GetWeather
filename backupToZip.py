# Tool name       :backupToZip
# Module name     :backupToZip.py
# Detail          :This's the tool to copy all directories to Zip file
# Implementer     :R.Ishikawa
# Version         :1.1
# Last update     :2017/12/24

#Version History
 #1 Create New                  R.Ishikawa    Ver.1.0
 #2 Set path and some comments  R.Ishikawa    Ver.1.1

import zipfile, os
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
 	   print('Done. ')

# Set path included files and directories you want to back up
backup_to_zip('/Users/RyoISHIKAWA/Desktop/')

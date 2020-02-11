
''' 

A simple HTML To TEXT converter: Converts all HTML FILES in Current Folder TO TEXT FILES.
Developed By M.Anish only. Ensure that you read NOTES at end of this code before use.

'''

import os

#Code to Notify User that Program has started.
print('\nProcess Started...\n')

#List to store contents of HTML file. 
data=[]

#Loop to check for HTML files in current Folder.
for i in os.listdir():
   if i[-3:].lower()=='htm' or i[-4:].lower()=='html':
       
       #Code to Display Current file which is being Processed.       
       print('Processing '+i) 
       
       #Code to create output text file.
       fp=open(i+'.txt','w')
       
       #Code to store HTML file contents as characters in data list.
       with open(i,'r') as f:
          for line in f.readlines():
              for word in line:
                  data.append(word)
 
       #Loop to remove all HTML TAGS. 
       x=0
       for z in data:
           if data[x]=='<':
              data.pop(x)
              while(data[x]!='>'):
                    data.pop(x)
           x+=1
 
       #Loop to remove all '>' present in HTML File.
       while '>' in data:
           data.remove('>')  
  
       #Loop to write data into text File.
       for y in data:
           fp.write(y)
       
       #Close Files and clear data stored in data list.       
       fp.close() 
       data.clear()       

#Code To Notify User that All Tasks Have been Completed!
print('\nTask Completed!\n')
          
x=input('Press any Key to continue...')

'''
Note: This Program loads entire HTML file in memory. 
we assume that HTML file is not large enough to fill your RAM.

This Program doesn't check for malformed or malicious HTML Files and maynot be safe to use in such situations.

This program only removes HTML TAGS from HTML Files however scripts and Style sheet codes may be left behind...
Please Compare Your HTML file content and Text File content after use.
This tool is not perfect.

'''

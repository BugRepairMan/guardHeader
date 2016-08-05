#!/usr/bin/python3

import glob,os,sys

global search_dir

def clearContent(pfile):
    pfile.seek(0)
    pfile.truncate()

def guard(fileName):
    file = open(fileName, 'r+')
    content = file.read()
    
    fileNameUp = fileName.split(".")[0].upper() + '_H'
    guardBegin = '#ifndef ' + fileNameUp + '\n'    \
            '#define ' + fileNameUp + '\n\n' 
    guardEnd = '\n#endif'
    newContent = guardBegin + content + guardEnd
    
    clearContent(file) 
    file.write(newContent)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('Please provide a directory')
    else:
        search_dir = sys.argv[1]
    
    # enter search directory
    os.chdir(search_dir)

    for file in glob.glob("*.h"):
        guard(file)

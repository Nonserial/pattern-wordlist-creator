## Pattern Wordlist Creator  --  combine wordlists containing only unique lines
# Copyright Nonserial Spacewalker 2016

import os
import sys

def import_wlist(filename):
    try:
    	# get unique values
    	d = open(filename, "r")
    	wlist = d.read().split("\n")
    	wlist_container = len(wlist)-1
    	d.close()
    except:
	sys.exit("\n\n\nFile ERROR: Failed to open file: '" + sys.argv[i+1] + "'\n--> Please check file-paths and provide only text-based files!\n")

    wlist.pop()
    
    return wlist, wlist_container


number_args = len(sys.argv) - 1

try:
    if number_args <= 2:
    	if number_args == 1 and ((sys.argv[1] == "--help") or (sys.argv[1] == "-h")):
	    print "\nUsage:\n"\
        	    	"pw_unify.py wordlist1.txt wordlist2.txt\n\n"\
        	    	"You must provide 2 wordlist-files, containing one word or character per row.\n"\
        	    	"The program combines the wordlists. Multiple occurences of words/lines are being ingnored.\n"\
			"\nThe new wordlist is stored in the folder from which you are running the program and named 'wordlist_unify.txt'"
	    raise
	elif number_args == 2:
	    pass
	else:
	    print "\nYou must provide exactly two wordlist-files!\nFind help: run 'python pw_unify.py --help'\n"
	    raise
    else:
	print "\nYou must provide exactly two wordlist-files!\nFind help: run 'python pw_unify.py --help'\n"
	raise
except:
    sys.exit()

wlist1, wlist1_container = import_wlist(sys.argv[1])
wlist2, wlist2_container = import_wlist(sys.argv[2])

# calculate unique values
wlist_diff = sorted(list(set(wlist1+wlist2)))

# calculate total number of possibilities
wlist_diff_container = wlist1_container + wlist2_container


f = open("wordlist_unify.txt", "w")
for item in wlist_diff:
    f.write(item + "\n")
f.close()
sys.exit(str("\nUnify-wordlist created!\n" + str(len(wlist_diff)) + " lines from " + str(wlist_diff_container) + " possibilies written.\n\nWordlist size: " + "{0:.2f}".format(os.stat("wordlist_unify.txt").st_size / (1024*1024.0)) + "MB\n"))

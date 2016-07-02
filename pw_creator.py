## Pattern Wordlist Creator  --  create pattern-based wordlists
# Copyright Nonserial Spacewalker 2016

import sys
import os

def unique_values():
    # get unique values
    d = open("wordlist.txt", "r")
    wlist = d.read().split("\n")
    wlist_container = len(wlist)-1
    d.close()
    wlist.pop()
    wlist_unique = sorted(list(set(wlist)))
    f = open("wordlist.txt", "w")
    for item in wlist_unique:
        f.write(item + "\n")
    f.close()
    sys.exit(str("\nWordlist created!\n" + str(len(wlist_unique)) + " unique lines from " + str(wlist_container) + " possibilies written.\n\nWordlist size: " + "{0:.2f}".format(os.stat("wordlist.txt").st_size / (1024*1024.0)) + "MB\n"))



number_args = len(sys.argv) - 1

try:
    if number_args >= 2:
	pass
    elif number_args == 1 and ((sys.argv[1] == "--help") or (sys.argv[1] == "-h")):
	print "\nUsage:\n"\
        	    	"pw_creator.py file1.txt file2.txt file3.txt ...\n\n"\
        	    	"You can specify up to 6 word-files, containing one word or character per row.\n"\
        	    	"The words in the wordfiles are being permuted to create a wordlist.\n"\
        	    	"This is interesting in the case, you know some sort of pattern of a password.\n"\
			"\nThe new wordlist is stored in the folder from which you are running the program and named 'wordlist.txt'"
	raise
    else:
	print "\nYou must provide at least two word-files!\nFind help: run 'python pw_creator.py --help'\n"
	raise

except:
    sys.exit()


print "\nProvided files: ", number_args, "\n"

for i in range(0, number_args):
    try:
    	# open word-file
    	f = open(sys.argv[i+1], "r")
    	# make list of words in wordfile, split by linebreak
    	wlist = f.read().split("\n")
    	f.close()
    except:
        sys.exit("\n\n\nFile ERROR: Failed to open file: '" + sys.argv[i+1] + "'\n--> Please check file-paths and provide only text-based files!\n")

    # remove empty value on last position
    wlist.pop()
    print "Word-file ", i+1, "'", sys.argv[i+1], "': ", wlist
    exec("var_%d = %s" % (i + 1, wlist))
    


# create empty wordlist
d = open("wordlist.txt", "w+")
d.close()

# open wordlist in append-mode
d = open("wordlist.txt", "a")

# containing words
wlist_container = 0

for word1 in var_1:
    for word2 in var_2:
        word = word1 + word2
        d.write(word + "\n")
d.close()

# when only 2 files provided:
if number_args == 2:
    unique_values()
    
# when more than 2 files provided:
if number_args > 2:
    for i in range(2, number_args):
	# open already created wordlist
    	d = open("wordlist.txt", "r")
    	wlist = d.read().split("\n")
    	wlist.pop()
    	d.close()
    	d = open("wordlist.txt", "w")
    	for word1 in wlist:
            for word2 in eval("var_%d" % (i+1)):
            	word = word1 + word2
            	d.write(word + "\n")
    	d.close()
	i += 1

# get unique values, when more than 2 files provided:
unique_values()

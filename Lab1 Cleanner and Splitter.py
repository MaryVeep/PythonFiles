#python 3.6
#open file specified by user: Team zeta use insulin.txt
validFile = False
while validFile == False:
    try:
        print("insuilin.txt is a provided sequence file")
        targetFile = open(input("Read from what sequence file?: "))
        validFile = True
    except:
        print("File not found.")
dirtySequence = targetFile.read()
#clean the sequence by removing certain substrings
cleanSequence = dirtySequence.replace("ORIGIN", "")
cleanSequence = cleanSequence.replace("\n", "") #remove newlines
cleanSequence = cleanSequence.replace("//", "")
cleanSequence = cleanSequence.replace(" ", "") #remove whitespace
for i in [*range(0,10)]:
    cleanSequence = cleanSequence.replace(str(i), '') #remove digits
subSeqStart = 0
subSeqEnd = 0
sequences = [] #will save cut sequences
#while we haven't reached the end of the sequence
while int(subSeqStart) < len(cleanSequence) - 1:
    validInput = False
    while validInput == False:
        subSeqEnd = input(f"Split where (or type 'end' to go to the end)? (currently at {subSeqStart + 1}, ends at {len(cleanSequence) }): ")
        #attempt to convert the user input to an int
        try:
            subSeqEnd = int(subSeqEnd)
        except:
            print("Unable to convert string to int")
        if subSeqEnd == 'end':
            subSeqEnd = len(cleanSequence)
            validInput = True
        elif type(subSeqEnd) == str and (subSeqEnd != 'end'):
            print("Invalid string input")
            validInput = False
        #if the input is within the range of the sequence and greater than subSeqStart say it's valid input
        elif subSeqEnd <= len(cleanSequence) and subSeqEnd > subSeqStart:
            validInput = True
        #otherwise it's not
        else:
            print("Invalid input")
            validInput = False
    #create a substring from subSeqStart up to subSeqEnd
    subSeq = cleanSequence[subSeqStart:subSeqEnd]
    #add it to the sequences list
    sequences.append(subSeq)
    #set up subSeqEnd for the next subsequence
    subSeqStart = subSeqEnd
    #save any currently open file just in case, since targetFile is reused from the start of the program
    targetFile.close()
    #open a file to write to, creates a new one if not found, overwrites
    targetFile = open(input("Write to what file?: "), "w")
    #write the text of the subsequence to the text file
    targetFile.write(subSeq)
    #save the file
    targetFile.close()
    #print out all currently cut sequences, this can be removed if sequences become too large
    print(sequences)
    #repeat the loop until we reach the end of the sequence

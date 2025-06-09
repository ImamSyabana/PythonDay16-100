#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# membaca template surat  
starting_file = open("Day 24_mails/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode = "r")
starting_contents = starting_file.read()
print(starting_contents)
starting_file.close()


    
# membaca nama nama yang diundang
invited_file = open("Day 24_mails/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt", "r")
for x in invited_file.readlines():
    
    # menghilangkan \n di tiap nama undangan
    invited_names = x.strip("\n")
    
    # membaca template surat 
    with open("Day 24_mails/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode = "r") as starting_file:
        starting_contents = starting_file.read()
    
    # menulis surat masing masing nama undangan
    with open(("Day 24_mails/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt".format(name = invited_names)).strip("\n"), mode = "w") as file:
        file.write((starting_contents.replace("[name]", x.strip("\n"))))
    



invited_file.close()

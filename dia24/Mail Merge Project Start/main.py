#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# def get_name():
#     with open('dia24/Mail Merge Project Start/Input/Names/invited_names.txt') as file:
#         data = file.readlines()
#         return data
#
# with open('dia24/Mail Merge Project Start/Input/Letters/starting_letter.txt') as letter_file:
#     letter = letter_file.read()
#     names = get_name()
#     for name in names:
#         new_letter = letter.replace('[name]', name.strip())
#         with open(f"dia24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name.strip()}.txt", mode='w') as completed_letter:
#             completed_letter.write(new_letter)

with  open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()
    print(names)

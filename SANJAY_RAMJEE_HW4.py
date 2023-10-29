import csv
import time
import tkinter
def chooseOption():
    print('--- --- --- Main Menu --- --- ---')
    option = input('Choose option:\n' \
         '[1] Create new text file\n' \
         '[2] Read text file content\n'
         '[3] Append to text file\n'
         '[4] Search text file\n' \
         '[5] Export to CSV\n' \
         '[6] Exit program\n'
         'option = ')
    return option

option = chooseOption()
while option != '6':
    if option == '1': 
        try:
            name = input('Enter a file name: ')
            file = open(name, 'w')
            file.close()
        except: 
            print('An error occurred during the CREATE operation!')
        
    elif option == '2':  
        name = input('Enter an existing file name: ')
        
        try:
            with open(name, 'r') as file:
                contents = file.read()
                print('File contents: ')
                print(contents)
                file.close()
        except:
            print('An error occurred during the READ operation!')

    elif option == '3':  
        name = input('Enter an existing file name: ')
        try:
            with open (name, 'a') as file:
                writing = input('Enter text to append to file: ')
                file.write(writing)
        except:
            print('An error occurred during the APPEND operation!')

    elif option == '4':  
        name = input('Enter an existing file name: ')
        try:
            with open(name, 'r') as file:
                search = input('Enter the text you want to search for: ')
                contents = file.read()
                index = contents.find(search)
            if index != -1:
                print(f'File found at index {index}')
            else:
                print("No results")
        except:
            print('An error occurred during the FIND operation!')

    elif option == '5':  
        
        readfile = input('Enter the text file name you want to be read: ')
        exportfile = input('Enter the csv file name you want to export to: ')

        try:
            with open(readfile, 'r') as infile:
                lines = infile.readlines()
            list_of_lines = [line.strip().split(',') for line in lines]


            with open(exportfile, 'w') as outfile:
                csv_writer = csv.writer(outfile)
                csv_writer.writerows(list_of_lines)

        except:
            print('An error occurred during the EXPORT operation!')
    else:
        print('Invalid option!')
    time.sleep(1.5)
    print('Going Back to main menu ',end='')
    for i in range(4):
        print('.', end='')
        time.sleep(.4)
    print()
    option = chooseOption()

#----------A Program that substitutes words of a txt file to what user inputs----------#
import sys

def subs():
    buffer = {}
    while True: 
            
        text_word = input("What word from the text?: ").strip()
        sub = input("To what word?: ").strip()

        #Organize substitutions 
        buffer[text_word] = sub 

        if (input("Do you want to continue? (y or n?)").lower()) == 'n':
            break

    return buffer

def main():

    if len(sys.argv) != 2:
        print("Usage: python sub.py text.txt")
        return 1

    text_file = sys.argv[1]
    substitutions = subs()

    buffer = "" 
    with open(text_file,'r') as file:

        for row in file:
            for word in row.split():
                if word in substitutions:
                    buffer += substitutions[word] + " "
                else:
                    buffer += word + " "
            buffer += "\n"

    #instead of ruining the original file.txt --> output it as output.txt
    with open("output.txt", 'w') as file:
        file.write(buffer)

    print("Program finished! Check the text!")

if __name__ == '__main__':
    main()
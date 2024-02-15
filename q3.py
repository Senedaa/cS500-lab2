from operator import index


def main():
    #print the name of the program
    print("==== A list of words ====")

    """
    task 1
    """
    list_of_words = []

    word = input("Enter a word: ")
    while word.lower() != "exit":
        list_of_words.append(word)
        word = input("Enter a word: ")
    
    print("The original List")
    print(list_of_words)

    sorted_list = sorted(list_of_words)
    print("Sorted list is below: ")
    print(sorted_list)

    """
    task 2
    """
    print("The Unique words are:")
    c = True
    for i in range (len(sorted_list)):
        for j in range (0,i):
            if sorted_list[i] == sorted_list[j]:
                c = False
            else:
                c = True
        if c == True:
            print(sorted_list[i], end = ' ')

if __name__ == "__main__":
    main()
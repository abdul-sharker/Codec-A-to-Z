import string
from collections import Counter
from tkinter import Tk, filedialog


def most_frequent_word():

    root=Tk()
    root.withdraw()
    file_path=filedialog.askopenfilename(
    title="Select a text file",
    filetypes=[("Text files","*.txt"),("All files","*.*")]
    )

    if not file_path:
        print("No file selected")
        return
    
    
    try:
        with open (file_path,'r') as file:
            text=file.read()
    
            text=text.translate(str.maketrans('','',string.punctuation)).lower()



            words=text.split()

            word_counter=Counter(words)

            most_common_w = word_counter.most_common(1)[0]

            print(f" Most frequent word: \"{most_common_w[0]}\"  \n Appears: \"{most_common_w[1]}\" times \n")


    except Exception as e:
        print(f"Error: {e}")


most_frequent_word()
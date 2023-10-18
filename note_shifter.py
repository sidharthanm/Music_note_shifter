"""
This script is used to rotate musical notes. It takes an actual note, a shifted note, and a string of notes as input.
It then rotates the notes in the string based on the shift between the actual and shifted note.
"""

# Define the musical notes
notes = 'a,a#,b,c,c#,d,d#,e,f,f#,g,g#'.split(',')

def rotatecount(act, cur):
    """
    Function to calculate the rotation count between two notes.
    """
    a = 1
    val = notes.index(act)
    while True:
        if notes[(a+val)%12] == cur:
            return a
        a += 1

def custom_split(a):
    """
    Function to split a string into individual notes.
    """
    c = 0
    rl = []
    while c < len(a):
        if a[c] in notes:
            rl.append(a[c])
        if a[c] == '#':
            rl[-1] = ''.join((rl[-1], '#'))
        c += 1
    return rl

def rotate(s, v):
    """
    Function to rotate the notes in a string.
    """
    for i in range(len(s)):
        s[i] = notes[(notes.index(s[i])+v)%12]
    return s

if __name__ == "__main__":
    print("Note: Enter notes in lowercase")
    
    # Get the actual note from user
    print("Enter actual note:")
    a = input()
    
    # Get the shifted note from user
    print("Enter shifted note:")
    b = input()
    
    # Calculate the rotation count
    c = rotatecount(a, b)
    
    # Get the string of notes from user
    s = input("Input string: ")
    
    # Split the string into individual notes
    s = custom_split(s)
    
    # Rotate the notes and print the result
    print(rotate(s, c))

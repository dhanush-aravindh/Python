# Escape sequence / characters in python
# \n helps to print the sequence in the new line or it gives us new line
string1 = "I am \nso\ncool"
print(string1)

# \t it creates a space between sequence of statement or characters or it gives few empty spaces(tabs)
String2 = "1.Oil\t2.Stove\t3.Pan\t4.flour\n"
String3 = "1.Oil \t2.Stove \t3.Pan  \t4.flour\n"
String4 = "1.Oil \t 2.Stove \t 3.Pan \t 4.flour\n"
print(String2, String3, String4)

# Using \ to print single quotes within single quotes or double quotes within double quotes
# We can also use """ quotes in the beginning and end of the sequence
# It will print all the double and single quotes in the sequence

print('Donald trump said "It\'s going to be huge".')
print("Donald trump said \"It's going to be huge\".")
print("""Donald trump said "It\'s going to be huge".""")

String5 = """I am a string
which is spanning 
over several lines"""
print(String5)

# Triple quotes is used by the programmer for better readability and spanning over several lines
# Spanning over several lines is not possible in double and single quotes

print("Donald t\"rump said \"It's going to b\"e huge\".")
# many backslash is used which makes it difficult to read

# to stop spanning  the string over lines we can use backslash at the end of each line
String6 = """I am a string \
which is spanning \
over several lines"""
print(String6)

# C:\Users\temp\new_course.pdf
# \U-> Unicode escape sequence
# A unicode escape sequence is a backslash followed by the letter 'u' followed by four hexadecimal digits (0-9a-fA-F).
# It matches a character in the target sequence with the value specified by the four digits.
# For example, ”\u0041“ matches the target sequence ”A“ when the ASCII character encoding is used.
# print("C:\Users\temp\new_course.pdf")
# Two methods are used to rectify the problems caused by escape characters while tracing the path of the file
print("C:\\Users\\temp\\new_course.pdf")
# Method 1: Use backslash infront of the escape characters to print the corresponding values.
print(r"C:\Users\temp\new_course.pdf")
# Method 2 : Introducing r infront of the file name so that it converts everything into a raw string

# \a gives a bell sound--It has been removed in recent versions of python
print("My name is billa \a")
# \b acts like a backspace. It reduces the space between the words and shifts back to one word back in which word
# It is being used
print("Hello \bWorld")
print("Hello    \b\b\b\b\b\bworld")
print("Hello\b\b\b\bworld")
# It first prints the "Hello" word and according to the \b the space and letters in the word get erased
# It can also be overwritten by another word

print("Hello    \b\b\b\b\b\b")
print("Hello\bWorld")  # It has overwritten the letter e.
# \b --> ASCII Backspace (BS)
# \f --> ASCII Formfeed(Ff) It shifts to the next page of the program
print("Hello \fWorld!")

# \r --> Carriage return
print("Hello \rWorld!")
# According to above print statement the world Hello got printed first as soon as interpreter and compiler
# looks \r  it changes the cursor from "Hello _" to the first place again that is "_Hello" and so it reduces the whole
# string to nothing
print("Hellooooooooo \rWorld")
print("Hello \r")
# \r should be followed by any word in order to change the first word
# or else it will print the first word again and again
print("Hel\rlo")
print("\rHello")

# \v --> Vertical Tab. It is depreciated and removed from python
print("Hello \vWorld")
# Output: Hello
#             World

# \ooo --> Octal values. It essentially requires knowledge in ASCII values
# Why we use three \ooo is it requires a minimum three values
# \xhh --> Hexadecimal values. It needs hh --> essentially two values which is preced by x eg:x22,x48..
print("\x48\x65\x6c\x6c\x6f\x20")
print("\110\145\154\154\157")

# \uxxxx --> \u followed by 16 bit hexadecimal value that is 4 times xxxx (Unicode)
# \Uxxxxxxxx--> \U followed by 32 bit hexadecimal value that is 8 times xxxx (Unicode)
# Obselete values are \v \f \a



# Cracking the Caesar code using frequency analysis
The cracker contains 3 main functions

## The 'get_shift_rules' function:
Probably the core function. 
It is supposed to procces the the initial string: removes the spaces and the special character. Then it counts the number of times a letter appears in the string and creates an odered list. It then creates a list of possible permutation based on the frequency of letters in the code and in the selected language.

## The 'dechyper' function:
The actual code cracking is happening here as it shifts the letters based on the permutations list in order to get the string shifted in the right order

## The 'spell_checker' function:
Is supposed to use external libraries to check if the decrypted string contains actual english words, here is where i met some troubles implementing those external libraries so i made a short list of frequent english words(valid_words)

The last function just blends all of the above together and prints the string to have valid words.

![alt text](https://github.com/VladCroitoru/SI-labs/blob/master/Lab%203/results.png "Cracked codes")

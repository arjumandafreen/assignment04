Sentence Generator
Description
This Python script generates sentences based on the user-provided word and part of speech. The user can input a noun, verb, or adjective, and the script will print a sentence using that word in the correct context. The user specifies the part of speech by entering an integer (0 for noun, 1 for verb, or 2 for adjective).

Features
Allows the user to input a word.

Asks the user to specify the part of speech (noun, verb, or adjective).

Generates a sentence with the word placed in the appropriate context.

Handles invalid input for part of speech.

How It Works
User Input: The script prompts the user to input a word and specify its part of speech.

Sentence Generation: Based on the part of speech, the script generates a sentence:

If the word is a noun (0), it creates a sentence with the noun in a collection context.

If the word is a verb (1), it creates a sentence with the verb in an activity context.

If the word is an adjective (2), it creates a sentence with the adjective describing a scene.

Invalid Input Handling: If the user enters an invalid part of speech (anything other than 0, 1, or 2), the script will notify the user and not generate a sentence.

Requirements
Python 3.x

How to Run
Clone or download the repository.

Open a terminal and navigate to the directory where the script is located.

Run the script by typing:


python sentence_generator.py
Follow the prompts to input a word and its part of speech.

The script will generate a sentence based on your input.


Please type a noun, verb, or adjective: dog

Is this a noun, verb, or adjective?

Type 0 for noun, 1 for verb, 2 for adjective: 0

I am excited to add this dog to my vast collection of them!
License
This project is licensed under the MIT License.


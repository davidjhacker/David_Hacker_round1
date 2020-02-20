# lol i've never written a readme before
So here's what this does: I scrape front-page headlines from the Harvard Crimson,
thecrimson.com, and this API that Jonah Fried told me about does 99% of the
work.
## The API
The API (datamuse.com/api/) has a bunch of different word-association features,
but I used one that takes words and finds related words that start with the
letter B. It also has a score that tells you how well-related
each word is to your target word.
## my program
The program takes a number from 1-10 as a command-line argument, where 1
is minimum b-ification and 10 is maximum b-ficiation.
It returns headlines and return them in a .txt where
every successfully-associated word is replaced with its corresponding b-word,
beginning with the 🅱️ emoji. The criteria for a successful association depends
on the number entered by the user - higher numbers = more successful association
= more b.
## other stuff
The .txt displays the actual Crimson headline mapped to its corresponding
🅱️eadline. I changed a few word outputs manually: by default, the API related
"Harvard" to "bought," "of" to "bsf," and "on" to "bpm," which aren't very good
associations, so I instead mapped Harvard to 🅱️arvard and didn't change the
other two words.
## lmk if u get errors or something? idk

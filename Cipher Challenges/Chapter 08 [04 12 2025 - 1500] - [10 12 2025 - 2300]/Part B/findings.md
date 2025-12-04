# Documentation for Ch8. pB

## The Basis;
Okay, so the cipher is a playfair cipher, as indicated by the prescence of filler text, `X` or just duplicate letters. Also, the previous challenge success text stated that it is recommended for us to know the playfair cipher. After a dictionary attack - we landed on a nice word (similar to the theme of "general" from part A) - `COLONEL` - it's over - right? WRONG!!!

## The Issue;
Turns out the input isn't fully decoded, and contains several artifacts - whether it be from fillers or just incorrect letters. So, after some further bruteforcing,`COLONELBABBAGE` gave a slightly nicer output.

An optimisation can be performed on the keyword; remove the duplicate letters!
- `COLONELBABBAGE` -> `COLNEBAG`
This gives the same output - but its progress ... I think.

## The Smaller Issue;
Now we are stuck, the output is still slightly jumbled, and no progress had actually been made.
Either another cipher had to be applied, or the keyword is incomplete or not fully correct.
Further dictionary attacks proved *fruitless*, and a working keyword for another potential cipher layer could not be found.
Moreover, the cipher is **NOT monoalphabetic**, since there cannot be a consistent, universal keymap - *womp womp*

## Next Steps;
- Investigate the "Null Cipher" - a kind of cipher which contains plaintext within ciphertext (our issue!), although a viable pattern has not yet been found
- Investigate variatons of the "Vigenere Cipher" - such as the "Beaufort Cipher"

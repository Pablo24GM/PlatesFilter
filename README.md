# Vanity Plates Filter

In Python, I tried to implement a program that prompts the user for a so called "vanity plate" and then outputs "Valid" if this one meets all the requirements, or "Invalid" if it doesn't. The code handles case-insensitive characters (numbers, letters, etc.).
The requirements for a "vanity plate" are:

1. It must contain a minimum of 2 characters and a maximum of 6 characters.

2. It must only contain all letters or letters and numbers. No periods, spaces, or punctuation marks are allowed.

3. All vanity plates must start with at least two letters.

4. Numbers cannot be used in the middle of a plate, they must come only at the end. For example: "AAA222" would be an acceptable "Valid" vanity plate. However, "AAA22A" would not be acceptable, "Invalid".

5. The first number used in a "Vanity Plate", if any, cannot be the number "0".


## References:

![App Screenshot](https://www.simpsonsarchive.com/bin/license_plates.icon.gif)

I'm still working on this code since it is not filtering all the 5 conditions mentioned before, the last condition, the # 5, is still showing "Valid" to some plates that are not meeting all 5 requirements. Therefore, if you know why, and know how to fix it, feel free to implement the changes you see more convenient. In order to try it out you will need to have (obviously) Python installed on your machine, then just run it through the terminal and that’s it.

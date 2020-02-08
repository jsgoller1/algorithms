# Assignments

## Pre-work

1) Let’s define a border of a string to be a proper prefix that’s also a proper suffix (“proper” means the prefix / suffix isn’t allowed to be the entire string). Write a function that takes a string and returns the length of its longest border. For example, the string "aabbaa" has two borders: "a" and "aa", so its longest border has length 2. Don’t worry about efficiency for now.

2) Design a state machine for checking whether the specific string "ab" appears in some longer string. The state machine should process the longer string one character at a time, and update its state based on the value of that character. Hint: the state machine should have 3 states, depending on how many characters are currently matched (0, 1, or 2).
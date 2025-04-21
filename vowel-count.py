sentence = "Lets Count Some Vowels"

vowels = {"a", "e", "i", "o", "u"}
vowelCount = sum(1 for char in sentence if char in vowels)

print("Your senctence has a total vowel count of: ", vowelCount)    


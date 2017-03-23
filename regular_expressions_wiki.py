import wikipedia
import re

text1 = wikipedia.summary('krakow')
regexp1 = " \(.*?\)"
print("Before: \n")
print(re.split(regexp1, text1))
print("\nAfter:\n")
print(re.sub(regexp1, "", text1))



def find_longest_word(words):
  return max(words, key=len)
print(find_longest_word(["PHP", "Exercises", "Backend"]))
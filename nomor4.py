def palindrome(word):

	rev = ''.join(reversed(word))

	if (word == rev):
		return True
	return False

word = "rotator"
answer = palindrome(word)

print("Is", word, "palindrome?")
if(answer):
	print("Answer = Yes")
else:
	print("Answer = No")
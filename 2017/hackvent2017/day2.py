import base64
with open('day2_wishlist.txt', 'r') as input: 
	solution = input.read()
	for i in range(32):
		solution = base64.b64decode(solution)
	print("solution: " + str(solution))
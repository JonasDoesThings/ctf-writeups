import json, gzip, os, sys, base64

if not os.path.isdir("day9"):
	os.mkdir("day9")

with open("day9_jsonion.json", "r") as file:
	current_content_raw = file.read() 
	
	layer = 0
	while not "HV17" in current_content_raw:
		for sub_layer in json.loads(current_content_raw):
			current_content = sub_layer
			layer_solution = ""

			if current_content['op'] == "map":
				map_to = current_content['mapTo']
				map_from = current_content['mapFrom']
				table = {}

				for i in range(len(map_from)):
					table[map_from[i]] = map_to[i]

				s = ""
				for char in current_content['content']:
					s += table[char]
				
				layer_solution = s
			elif current_content['op'] == "gzip":
				layer_solution = gzip.decompress(base64.b64decode(current_content['content'])).decode("utf-8")
			elif current_content['op'] == "b64":
				layer_solution = base64.b64decode(current_content['content']).decode("utf-8")
			elif current_content['op'] == "nul":
				layer_solution = current_content['content']
			elif current_content['op'] == "xor":
				content_barray = bytearray(base64.b64decode(current_content['content']))
				mask_barray = bytearray(base64.b64decode(current_content['mask']))
				tmp = bytearray(len(content_barray))

				for i in range(len(tmp)):
					tmp[i] = content_barray[i] ^ mask_barray[0]

				layer_solution = tmp.decode("utf-8")
			elif current_content['op'] == "rev":
				layer_solution = current_content['content'][::-1]
			elif current_content['op'] == "flag":
				break
			else:
				print("Wasn't able to go any further, unknown operation " + current_content['op'])
				break


		with open("day9/day9_log_" + str(layer) + ".json", "a") as log:
			log.write(layer_solution)
			current_content_raw = layer_solution
			current_content = json.loads(current_content_raw)[0]
			print("Solved layer " + str(layer) + " with operation " + current_content['op'])
			layer += 1

	print("FOUND THE FLAG!")
	print(current_content_raw)
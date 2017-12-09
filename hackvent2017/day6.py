import urllib.request
import time

#thanks https://stackoverflow.com/a/3368991
def find_between(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return "error"


i = 0
start = time.time()
while True:
	response = urllib.request.urlopen("https://zxing.org/w/decode?u=http%3A%2F%2Fchallenges.hackvent.hacking-lab.com%3A4200%2F")
	text = response.read().decode('utf-8')
	print("[" + str(i) + "] " + find_between(text, "Raw text</td><td><pre>", "</pre></td></tr><tr><td>"))

	if 'HV' in str(text):
		print("FOUND::: " + find_between(text, "Raw text</td><td><pre>", "</pre></td></tr><tr><td>"))
		print("It took " + str(i) + " tries & " + str((float(end) - start)/60))
		break

	response.close()
	i += 1
	time.sleep(1)


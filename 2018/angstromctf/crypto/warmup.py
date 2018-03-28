from pycipher import Affine

for i in range(1, 25):
	for i2 in range(0, 25):
		try:
			s = Affine(a=i, b=i2).decipher("myjd{ij_fkwizq}")
			if "actf" in s.lower():
				print(s)
		except Exception:
			pass

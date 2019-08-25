def addition():
	total = sum(x for x in range(1,1000) if (x % 3 == 0 or x % 5 == 0))
	return str(total)


if __name__ == "__main__":
	print(addition())

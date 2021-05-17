import os
import json

def main():
	all_files = [os.path.join(dp,f) for dp, dn, fn in os.walk('json') for f in fn]
	for filepath in all_files:
		if not filepath.endswith('.json'): continue
		print(filepath)
		with open(filepath, 'r') as f:
			json.load(f)

if __name__ == "__main__":
	main()
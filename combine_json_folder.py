import os
import json
import argparse

def main(name):
	all_files = [(f,os.path.join(dp,f)) for dp, dn, fn in os.walk(f'json/{name}') for f in fn]
	combined = {}
	for filename,filepath in sorted(all_files, key=lambda fnfp: fnfp[0]):
		if not filepath.endswith('.json'):
			continue
		origin_id = filename.split('.')[0]
		print(origin_id)
		with open(filepath, 'r') as f:
			combined[origin_id] = json.load(f)
	
	with open(f'{name}.json', 'w') as f:
		json.dump(combined, f, indent=4, sort_keys=True)



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='combining JSON files')
	parser.add_argument('name')
	args = parser.parse_args()
	main(args.name)
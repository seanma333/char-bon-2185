import json
import os

def get_json_from_directory(directory):
	filenames = [name for name in os.listdir(directory) if name.endswith(".json")]
	all_jsons = {}
	for filename in filenames:
		identifier = filename.split('.')[0]
		with open(f'{directory}/{filename}', 'r') as f:
			file_json = json.load(f)
			all_jsons[identifier] = file_json

	return all_jsons

def main():
	class_dir = "json/classes"
	subclass_dir = "json/classes/subclasses"

	classes = get_json_from_directory(class_dir)
	subclasses = get_json_from_directory(subclass_dir)

	all_types = {}
	for class_id,body in classes.items():
		for feature in body['class_features']:
			all_types[feature['type']] = all_types.get(feature['type'], 0) + 1

	for subclass_id,body in subclasses.items():
		for feature in body['class_features']:
			all_types[feature['type']] = all_types.get(feature['type'], 0) + 1

	all_types_list = sorted(list(all_types.keys()))
	for name in all_types_list:
		print(f'{name} - {all_types[name]}')

if __name__ == "__main__":
	main()
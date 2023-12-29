import yaml

f = open("../../config/data.yaml", encoding="utf8")
get_data = yaml.safe_load(f)
print(get_data)
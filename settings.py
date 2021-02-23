import json

_raw = {}
_default = {}

# Set settings
with open(".settings", "r") as f:
	_raw = json.load(f)

# Load defaults
with open(".default", "r") as f:
	_default = json.load(f)

settings = {}

# Find the set setting, if there is none then just use the default
for key in _default.keys():
	try:
		settings[key] = _raw[key]
	except:
		settings[key] = _default[key]
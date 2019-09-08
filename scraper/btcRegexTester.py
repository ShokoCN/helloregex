import re
print('a0')
line = "3N3xWVi6qe6Qy5n6hfC7Bgpgizkd7ehwiz"
match = re.findall(r'[13][a-km-zA-HJ-NP-Z0-9]{26,33}', line)
print(match)


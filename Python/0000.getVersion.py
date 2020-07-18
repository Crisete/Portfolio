import sys

# Get the Python version on our system, in String Format
#
print("String Format")
print("La version de python instalada es: ",sys.version)

# Also we can get on tuples format
print("Tuple Format")
print(sys.version_info)

#Better output
print("Major version: ",sys.version_info.major, "\nMinor version: ", sys.version_info.minor)
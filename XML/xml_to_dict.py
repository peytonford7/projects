import xmltodict

# Create dictionary
data = {
	"root": {
		"child": "Hello, World!"
	}
}

# Convert the dictionary to XML string
xml_string = xmltodict.unparse(data, pretty=True)

# Write the XML string to a file
with open("output.xml", "w") as file:
	file.write(xml_string)

import xml.dom.minidom as minidom

# Create a new XML document
doc = minidom.Document()

# Create a root element
root = doc.createElement("root")
doc.appendChild(root)

# Create a child element
child = doc.createElement("child")
child.appendChild(doc.createTextNode("Hello, World!"))
root.appendChild(child)

# Write to an XML file
with open("output.xml", "w") as file:
	file.write(doc.toprettyxml(indent=" "))

import xml.etree.ElementTree as ET

# Create a root element 
root = ET.Element("root")

# Create a child element
child = ET.SubElement(root, "child")
child.text = "Hello, World!"

# Create an ElementTree object
tree = ET.ElementTree(root)

# Write to an XML file
tree.write("output.xml")

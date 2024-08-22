# This is a study guide for PY4E Chapter 13

# DATA ON THE WEB
----

### - XML (eXtensible Markup Language) is the old version of "Wire Format"

### - JSON is the more modern "common" language used to send data across the web

## XML
- XML uses "Elements" (or Nodes) to share structured data between machines

- XML uses 
* start tag
* end tag
* text content
* Attribute
* Self closing tag

- XML doesnt care about indents
- XML looks very similar to HTML, but more structured with more rules
    
* Tags indicate the beginning and ending of elements. Similar to HTML

* Attributes - Keyword/value pairs on the opening tag of XML

* Serialize / De-Serialize - Convert data in one program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner.

- XML uses a TREE structure with parent and children nodes that are further defined by attribute nodes
"""

## XML Schema

- A contract that has constraints for structure and content aggrements across the web.
    
- Often used to specify a "Contract" between systems - "My system will only accept XML that conforms to this particular Schema"

- If a particular pieces of XML meets the specifications of the Schema - it is said to "validate"


----

## JSON (JavaScript Object Notation)

JSON is very similar to python dictionaries. It often uses dictionaries inside dictionaries.... Which are just key|value pairs within other key|value pairs

## API (Application Programming Interfaces)

- an API is an endpoint where two applications can talk to each other. 

- A RESTful API is an architectural style for an application programming interface that uses HTTP requests to access and use data.

- That data can be used to GET , PUT , POST and DELETE data types, which refers to reading, updating, creating and deleting operations related to resources.
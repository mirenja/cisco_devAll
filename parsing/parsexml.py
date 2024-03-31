# Fill in this file with the code from parsing XML exercise

import xml.etree.ElementTree as ET
import re

xml = ET.parse("myfile.xml")
root = xml.getroot()
#getting the xml namespace
#searches for a pattern enclosed in curly braces  at the beginning of the root tag.
#group(0)returns the entire matched string.
ns =re.match('{.*}',root.tag).group(0)
#format(ns) replaces the curly braces before edit-config with the namespace allowing us to dynamically set the namespace.
editconf = root.find(f"{ns}edit-config")
defop = editconf.find(f"{ns}default-operation")
testop = editconf.find("{}test-option".format(ns))

print(f"{ns}\n {defop}")
print(f"the default operation contains: {defop.text}")
print(f"the testop operations contains:{testop.text}")

# ********************results
# {urn:ietf:params:xml:ns:netconf:base:1.0}
#  <Element '{urn:ietf:params:xml:ns:netconf:base:1.0}default-operation' at 0x7f33754b4310>
# the default operation contains: merge
# the testop operations contains:set

import xml.etree.ElementTree as ET

def build_xml_tag(root, data={}):
    for tag_name, tag_value in data.items():
        tag = ET.SubElement(root, tag_name)
        if isinstance(tag_value, dict):
            build_xml_tag(tag, tag_value)
        else:
            tag.text = str(tag_value)

def response_xml(data={}):
    root = ET.Element('xml')
    build_xml_tag(root, data)
    return ET.tostring(root, encoding='unicode')

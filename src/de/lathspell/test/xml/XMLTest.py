import io
import unittest
import xml.etree.ElementTree as etree

class XMLTestTest(unittest.TestCase):
    """
    * Bessere Performance bei gleicher API bietet die auf libxml2 basierende
      python3-lxml: from lxml import etree
    """

    def setUp(self):
        self.xml = """
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

  <title>Example Feed</title>
  <link href="http://example.org/"/>
  <updated>2003-12-13T18:30:02Z</updated>
  <author>
    <name>John Doe</name>
  </author>
  <id>urn:uuid:60a76c80-d399-11d9-b93C-0003939e0af6</id>

  <entry>
    <title>Atom-Powered Robots Run Amok</title>
    <link href="http://example.org/2003/12/13/atom03"/>
    <id>urn:uuid:1225c695-cfb8-4ebb-aaaa-80da344efa6a</id>
    <updated>2003-12-13T18:30:02Z</updated>
    <summary>Some text.</summary>
  </entry>

</feed>
        """
        self.xml = self.xml.lstrip()
        self.xmlfile = io.StringIO(self.xml)

    def testParsing(self):
        tree = etree.parse(self.xmlfile)
        # @type tree etree.ElementTree
        self.assertIsInstance(tree, etree.ElementTree)

        root = tree.getroot()
        self.assertIsInstance(root, etree.Element)

        root_tag = root.tag
        self.assertEqual('{http://www.w3.org/2005/Atom}feed', root_tag)

        children = [child for child in root]
        self.assertEqual('{http://www.w3.org/2005/Atom}id', children[4].tag)
        self.assertEqual('http://example.org/', children[1].attrib['href'])
        self.assertEqual('John Doe', children[3][0].text)

        all_entries = root.findall('{http://www.w3.org/2005/Atom}entry')
        self.assertEqual(1, len(all_entries))

        # xpath gibt es nur mit lxml:
        # NSMAP = {'atom': 'http://www.w3.org/2005/Atom'}
        # entries = tree.xpath("//atom:entry", namespaces=NSMAP)

    def testGenerating(self):
        feed = etree.Element('{http://www.w3.org/2005/Atom}feed',
                attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
        feed_xml = etree.tostring(feed)
                
        self.assertEqual(b'<ns0:feed xmlns:ns0="http://www.w3.org/2005/Atom" xml:lang="en" />', feed_xml)


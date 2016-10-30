import unittest
from xml.dom.minidom import parseString
from TaggedRecipeParser import TaggedRecipeParser

def createCueMLDom(recipes=[], spans=[]):
    return '<TEI> \
                <teiHeader>...</teiHeader> \
                <text> \
                    <body>' \
                        + '\n'.join(recipes) \
                        + ' \
                        <spanGrp>' \
                            + '\n'.join(spans) + '\
                        </spanGrp> \
                    </body> \
                </text> \
            </TEI>'


class TaggedRecipeParserTest(unittest.TestCase):
        
    def testFindRecipesInDom(self):
        recipe = '<recipe type="Suppen." rcp-id="B-8"></recipe>'
        dom = parseString(createCueMLDom([recipe]))
        self.assertEqual(1, len(TaggedRecipeParser(dom).getRecipes()))

if __name__ == "__main__":
    unittest.main()

from informationExtraction.dictBasedExtractor import dictBasedEnrichment
from informationExtraction.ruleBasedExtractor import applyRulesToWordProperties
import string
import time
from xml.dom.minidom import parseString

class Extractor():
    
    def __init__(self, ingE, unitE, cueMLPrefix="cue:"):
        self.ingE = ingE
        self.unitE = unitE
        self.cueMLPrefix = cueMLPrefix

    def extractSentence(self, sentence, rcp):
        xmlStrings = []
        wps = dictBasedEnrichment(sentence, self.ingE, self.unitE)
        improvedWps = applyRulesToWordProperties(wps, rcp)
        for wp in improvedWps:
            if wp.lemma not in string.punctuation:
                xmlStrings.append(" ")
            xmlStrings.append(wp.toXml(self.cueMLPrefix))
        
        return "".join(xmlStrings)

    def extractRecipe(self, plainTextRcp):
        """ Returns a string, which is a valid cueML recipe with extracted information. """
        xmlStrings = ['<{}recipe type="{}" rcp-id="{}" xmlns:{}="http://cueML/ns">'
                      .format(self.cueMLPrefix, plainTextRcp.rcpType, plainTextRcp.rcpId, self.cueMLPrefix[:-1])]
        
        xmlStrings.append('<head>{}</head>'.format(self.extractSentence(plainTextRcp.name, plainTextRcp)))
        xmlStrings.append('<p>')
        for sentence in plainTextRcp.instructionSentences:
            try:
                xmlStrings.append(self.extractSentence(sentence, plainTextRcp))
            except Exception as e:
                print(str(e))
                print("Error in Extractor.extractRecipe('{}')".format(sentence))
        xmlStrings.append('</p>')        
        xmlStrings.append("</{}recipe>".format(self.cueMLPrefix))

        return "".join(xmlStrings)
    
    def extractRecipesToXml(self, rcps, ergFilePath):
        startTime = time.time()     
      
        xmlString = ['<TEI xmlns="tei">\
            <teiHeader>\
            <fileDesc>\
                 <titleStmt>\
                    <title>Title</title>\
                 </titleStmt>\
                 <publicationStmt>\
                    <p>Publication Information</p>\
                 </publicationStmt>\
                 <sourceDesc>\
                    <p>Information about the source</p>\
                 </sourceDesc>\
              </fileDesc>\
            </teiHeader>\
        <text><body>']
        for rcp in rcps:
            xmlString.append(self.extractRecipe(rcp))
        xmlString.append("</body></text></TEI>")
        
        with open(ergFilePath, 'w') as f:
            f.write(parseString(" ".join(xmlString)).toprettyxml())
          
        print('--- Needed for extracting and writingTo "{}": {} seconds ---'.format(ergFilePath, time.time() - startTime))
        

    
    
    
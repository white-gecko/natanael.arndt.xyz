.INTERMEDIATE : bibtex2rdf.jar white_gecko.bib

default: bibtex2rdf.jar white_gecko.bib keep_log
	rm bibtex2rdf.log

keep_log:
	java -jar bibtex2rdf.jar -schema schema.map -baseuri https://natanael.arndt.xyz/bib/ -enc UTF-8 white_gecko.bib white_gecko_bib.rdf
	rapper -i rdfxml -o turtle white_gecko_bib.rdf > white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Arndt_Natanael>/<http:\/\/aksw.org\/NatanaelArndt>/g' white_gecko_bib.ttl
	sed -i -e 's/Joint_proceedings_of_the_3rd_Workshop_on_Managing_the_Evolution_and_Preservation_of_the_Data_Web_(MEPDaW_2017)_and_the_4th_Workshop_on_Linked_Data_Quality_(LDQ_2017)_co-located_with_14th_European_Semantic_Web_Conference_(ESWC_2017)>/Joint_proceedings_of_MEPDaW_2017_and_LDQ_2017_co-located_with_ESWC_2017>/g' white_gecko_bib.ttl
	cat data.ttl white_gecko_bib.ttl > graph.ttl
	rapper -i turtle -o turtle graph.ttl > bib.ttl
	rm white_gecko_bib.rdf white_gecko_bib.ttl graph.ttl

bibtex2rdf.jar:
	wget https://www.l3s.de/~siberski/bibtex2rdf/bibtex2rdf.jar

white_gecko.bib:
	wget https://www.bibsonomy.org/bib/user/white_gecko -O white_gecko.bib

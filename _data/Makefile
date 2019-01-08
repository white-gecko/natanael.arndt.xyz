.INTERMEDIATE : bibtex2rdf.jar white_gecko.bib

default: bibtex2rdf.jar white_gecko.bib keep_log
	rm bibtex2rdf.log

keep_log:
	java -jar bibtex2rdf.jar -schema schema.map -baseuri https://natanael.arndt.xyz/bib/ -enc UTF-8 white_gecko.bib white_gecko_bib.rdf
	rapper -i rdfxml -o turtle white_gecko_bib.rdf > white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Arndt_Natanael>/<http:\/\/aksw.org\/NatanaelArndt>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Martin_Michael>/<http:\/\/aksw.org\/MichaelMartin>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Radtke_Norman>/<http:\/\/aksw.org\/NormanRadtke>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Abicht_Konrad>/<http:\/\/aksw.org\/KonradAbicht>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Tramp_Sebastian>/<http:\/\/aksw.org\/SebastianTramp>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Meissner_Roy>/<http:\/\/aksw.org\/RoyMeissner>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Marx_Edgard>/<http:\/\/aksw.org\/EdgardMarx>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Riechert_Thomas>/<http:\/\/aksw.org\/ThomasRiechert>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Frischmuth_Philipp>/<http:\/\/aksw.org\/PhilippFrischmuth>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Auer_Sören>/<http:\/\/aksw.org\/SoerenAuer>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Frommhold_Marvin>/<http:\/\/aksw.org\/MarvinFrommhold>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Kontokostas_Dimitris>/<http:\/\/aksw.org\/DimitrisKontokostas>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Valdestilhas_Andre>/<http:\/\/aksw.org\/AndreValdestilhas>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Nareike_Andreas>/<http:\/\/aksw.org\/AndreasNareike>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Nuck_Sebastian>/<http:\/\/aksw.org\/SebastianNuck>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Klimek_Bettina>/<http:\/\/aksw.org\/BettinaKlimek>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Junghanns_Kurt>/<http:\/\/aksw.org\/KurtJunghanns>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Ackermann_Markus>/<http:\/\/aksw.org\/MarkusAckermann>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Brümmer_Martin>/<http:\/\/aksw.org\/MartinBruemmer>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Stadler_Claus>/<http:\/\/aksw.org\/ClausStadler>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Lehmann_Jens>/<http:\/\/aksw.org\/JensLehmann>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Ermilov_Timofey>/<http:\/\/aksw.org\/TimofeyErmilov>/g' white_gecko_bib.ttl
	sed -i -e 's/<https:[^<>]*_Seige_Leander>/<http:\/\/aksw.org\/Partner\/LeanderSeige>/g' white_gecko_bib.ttl
	sed -i -e 's/Joint_proceedings_of_the_3rd_Workshop_on_Managing_the_Evolution_and_Preservation_of_the_Data_Web_(MEPDaW_2017)_and_the_4th_Workshop_on_Linked_Data_Quality_(LDQ_2017)_co-located_with_14th_European_Semantic_Web_Conference_(ESWC_2017)>/Joint_proceedings_of_MEPDaW_2017_and_LDQ_2017_co-located_with_ESWC_2017>/g' white_gecko_bib.ttl
	sed -i -e "s/Joint_Proceedings_of_the_Posters_and_Demos_Track_of_the_12th_International_Conference_on_Semantic_Systems_-_SEMANTiCS2016_and_the_1st_International_Workshop_on_Semantic_Change_&_Evolving_Semantics_(SuCCESS'16)>/Joint_PD_SEMANTiCS2016_and_SuCCESS16>/g" white_gecko_bib.ttl
	cat data.ttl white_gecko_bib.ttl > graph.ttl
	rapper -i turtle -o turtle graph.ttl > bib.ttl
	rm white_gecko_bib.rdf white_gecko_bib.ttl graph.ttl

bibtex2rdf.jar:
	wget https://www.l3s.de/~siberski/bibtex2rdf/bibtex2rdf.jar

white_gecko.bib:
	wget https://www.bibsonomy.org/bib/user/white_gecko -O white_gecko.bib

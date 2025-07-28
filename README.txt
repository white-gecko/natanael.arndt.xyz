# My Homepage

https://natanael.arndt.xyz/


# To update ttl files

    cd _data
    ./extract.py --file bib.ttl --base https://natanael.arndt.xyz/ --selection selection.sparql
    cd ..
    rm -r ttl/bib 
    cp -r _data/bib ttl/

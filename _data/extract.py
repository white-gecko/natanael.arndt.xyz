#!/usr/bin/env python3

import rdflib
import argparse
import os

# taken from https://github.com/RDFLib/rdflib/issues/123
def one(self, triple):
    """
    Return one matching "triple" or "None"
    """
    for statement in self.triples(triple):
        return statement

def exists(self, triple):
    """
    Return "True" if "triple" exists in the graph, "False" otherwise
    """
    statement = one(self, triple)
    if statement is not None:
        return True
    return False

def bnc(self, triple, *av, **kw):
        """
        Return the BNode closure(s) for triples that are matched
        by the given "triple". Any additional positional or keyword
        arguments are passed to the constructor for the new graph.
        """
        result = rdflib.Graph(*av, **kw)
        for s,p,o in self.triples(triple):
            result.add((s,p,o))
            if isinstance(o, rdflib.BNode) and not exists(result, (o, None, None)):
                result += bnc(self, (o, None, None))
        return result

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--endpoint', dest='endpoint')
parser.add_argument('--file', dest='file')
parser.add_argument('--base', dest='base', help="The base for generating the files")

args = parser.parse_args()
print(args.endpoint)
print(args.file)
print(args.base)

if args.endpoint:
    print("Sorry endpoint not yet supported")

if not args.file or not args.base:
    raise Exception("You need to specify a file and a base.")

graph = rdflib.Graph()
graph.parse(args.file, format="turtle")

i = 0
for sub in graph.subjects():
    i += 1
    if not sub.startswith(args.base):
        print("skip")
        continue
    destTtl = sub.replace(str(args.base), "", 1) + ".ttl"
    destJson = sub.replace(str(args.base), "", 1) + ".json"
    if i > 50:
        print("{} write to {}".format(sub, destTtl))
        i = 0
    resGraph = rdflib.Graph()
    triples = bnc(graph, (sub, None, None))
    resGraph += triples
    if not os.path.exists(os.path.dirname(destTtl)):
        os.makedirs(os.path.dirname(destTtl))
    try:
        resGraph.serialize(destTtl, format='turtle')
    except Exception as e:
        print(e)

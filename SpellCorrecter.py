#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lucene,sys,os
import traceback


path=os.getcwd()
lucene.initVM()
dict=lucene.File("./myindex")
directory = lucene.FSDirectory.open(dict)
sp = lucene.SpellChecker(directory)
dictionary= lucene.File("%s/pipimovieUTF8.txt"%path)
sp.indexDictionary(lucene.PlainTextDictionary(dictionary))
suggestions = sp.suggestSimilar("天汽预报", 2)
for item in suggestions:
    print item
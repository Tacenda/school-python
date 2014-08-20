__author__ = 'emilnielsen'

# This Python file uses the following encoding: utf-8
#!/usr/bin/python
# -*- coding: utf-8 -*-

math = (4*39)
print " 4 * 39 = ",math

print("Hvad hedder du?")
navn = raw_input("Mit navn er: ");

print "Hej",navn,"Hvordan gaar det?"

hvordan = None

def sporgsmal():

    print (
    """
    Svar muligheder:
    1) Det gaar godt
    2) Baade og
    3) Ikke saa skide godt
    """)
    hvordan = raw_input("Skriv tallet paa dit svar: ")

    return

sporgsmal()

if hvordan == ("1"):
    print("1")
elif hvordan == ("2"):
    print("2")
elif hvordan == ("3"):
    print("3")
else:
    print("Svar dog paa spoergsmaalet!")
    sporgsmal()
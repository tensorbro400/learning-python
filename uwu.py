print("""This program will translate any string of text into "uwu" with
 100 percent accuracy""")
text = input("Enter text to translate: ")
text = text.casefold()
text = text.replace("r", "w")
text = text.replace("l", "w")
print("")
print("""\ntranslated: "{}" 乂❤‿❤乂""".format(text)) 
print("")
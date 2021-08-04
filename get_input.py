#a function to take an article as input and return first/last sentences 
#of paragraphs on first 2 pages


#1 get an input 
article = open('../articles/moredocsinscience.pdf')

#2 change into text if needed using PyPDF2 
reader = PyPDF2.PdfFileReader(article)  



#3 find the first paragraph of page 1
#
for line in article: 
	line = line.rstrip() #strips right-hand side whitespace 
	if line.startswith(#can I use regex upper case with line break before it?)
		print(line)

#4 get the first sentence of the paragraph and return it 
#5 get the last sentence of the paragraph and return it 
#6 repeat for the rest of the paragraphs 
# --> limit to first page or two worth of paragraphs to test concept? 
#7 break the loop after X paragraphs 
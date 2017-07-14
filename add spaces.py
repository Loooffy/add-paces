#D:/程設/GitHub/format-tools/source/test.txt
#D:/程設/GitHub/format-tools/source/tree-exported-Thu-Jul-06-2017.txt

from fileIO import get_data, post_data

inputFile="D:/程設/GitHub/format-tools/source/tree-exported-Thu-Jul-06-2017.txt"
outputFile="D:/程設/GitHub/format-tools/source/output.txt"

data=get_data(inputFile)

data_split=data.split(']],')
data_out='\n\n'.join(data_split)

post_data(outputFile,data_out)
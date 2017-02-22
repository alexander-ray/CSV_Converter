import sys
import math

# Apply transformation
def getRealValue(initial):
    initial = float(initial)
    # Undo transformation to go back to "real" values
    final = ((math.atan(initial) + (math.pi/2)) * 100) / math.pi
    # Round to 2 decimal places, include trailing zeros
    return "%.2f" % round(final, 2)
   
# Removes quotes from beginning and end of string
def stripQuotes(string):
    if string.startswith('"') and string.endswith('"'):
        string = string[1:-1] # Remove first and last chars
    return string

def csvToJson(filename):
    f = open(filename, 'r')
    
    # Setting up list of column headers
    headers = f.readline()
    headers = headers.rstrip()
    headers = headers.split(",")

    lines = f.readlines() # Populate list with all non-header lines
    lastLine = len(lines) - 1
    print("[") 
    for i, line in enumerate(lines):
        line = line.rstrip()
        fields = line.split(",") # List of all fields, split by comma
        print("{")
        
        lastField = len(fields) - 1
        for j, field in enumerate(fields):
            fieldName = stripQuotes(headers[j])
            printVal = '"' + fieldName + '":"'
            if fieldName == 'Courage' or fieldName == 'Stupidity':
                printVal += getRealValue(stripQuotes(fields[j]))
            else:
                printVal += stripQuotes(fields[j])
            # Check if comma needs to be added    
            if j == lastField:
                printVal += '"'
            else:
                printVal += '",'
            print(printVal)  
       
       # Check if comma needs to be added    
        if i == lastLine:
            print("}")
        else:
            print("},")
    
    print("]")

def csvToXml(filename):
    f = open(filename, 'r')
    
    # Setting up list of column headers
    headers = f.readline()
    headers = headers.rstrip()
    headers = headers.split(",")

    # populate list with all non-header lines
    lines = f.readlines()
    
    for line in lines:
        line = line.rstrip()
        # List of all fields, split by comma
        fields = line.split(",")
        print("<person>")
        for i, field in enumerate(fields):
            fieldName = stripQuotes(headers[i])
            printVal = "    <" + fieldName + ">"
            
            if fieldName == 'Courage' or fieldName == 'Stupidity':
                printVal += getRealValue(stripQuotes(fields[i]))
            else:
                printVal += stripQuotes(fields[i])
            
            printVal += "</" + fieldName + ">"
            print(printVal)  
        print("</person>")

def main():
    # If converting to JSON
    if len(sys.argv) == 2:
        csvToJson(sys.argv[1])
    # If converting to XML
    elif len(sys.argv) == 3 and sys.argv[2] == "xml":
        csvToXml(sys.argv[1])
    else:
        print("Incorrect input format, please check documentation")

if __name__ == "__main__": main()

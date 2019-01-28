def initialize():
    # read in bank file
    file = open("bank.txt", 'r')
    data = [line.strip().split(',',2) for line in file]
    file.close()
    return data    
   
def createCategories(): 
    # read in categories file
    # categories contains the classifications for the data
    # categories[key][0] will contain the classified data
    # categories[key][1] will contain words that classify the data into the key
    try:
        file = open("Categories.txt", 'r')
        categories = {line.strip():[[],[]] for line in file}
        file.close()
    except IOError:
        return {"Food":[[],[]]}
    
    # open each text file for each category
    # if not available, program will automatically create file
    # at the end
    for key in categories:
        try:
            file = open(key+".txt", 'r')    
            for line in file:
                if line!='':
                    categories[key][1].append(line.strip())
            file.close() 
        except IOError:
            pass
    return categories
        

def printKeys(lookup):
    for i in range(len(lookup)):
        print(i+1,':',lookup[i])

def process(categories, data):

    # lookup table will make it easier for user input
    lookup = [key for key in categories]    
    
    for i in range(1,len(data)):
        stop = False
        for key in categories:
            for word in categories[key][1]:
                if word in data[i][2]:
                    print("${:.2f}".format(float(data[i][1].strip('-'))), data[i][2], '('+key+')')
                    categories[key][0].append(data[i]) 
                    data[i].append(key)
                    stop = True
                    break
            if stop: break
        else:
            print()
            printKeys(lookup)
            print()
            print("${:.2f}".format(float(data[i][1].strip('-'))), data[i][2])
            while True:
                op = input("Category #: ").split(' ',1)  
                try:
                    if op[0]=='STOP': return [categories,data,lookup]
                    k = lookup[int(op[0])-1]
                    categories[k][0].append(data[i]) 
                    if len(op)>1: categories[k][1].append(op[1])
                    data[i].append(k)
                    break
                except ValueError:
                    pass
                except IndexError:
                    pass
        
    return [categories,data,lookup]

def export(categories):
    file = open("Budget.txt", 'w')
    for key in categories:
        file.write(key+'\n')
        for d in categories[key][0]:
            file.write(str(d)+'\n')
        file.write('\n')
    file.close()
        
    for key in categories: 
        file = open(key+".txt", 'w')
        for word in categories[key][1]:
            file.write(word+'\n')
        file.close()        
        
def makeDaily(data,lookup):
    
    file = open("Daily.csv", 'w')   
    
    table = {key:0 for key in lookup}
    
    # headers
    file.write("Date")
    for i in range(len(lookup)):
        file.write(","+lookup[i])
    file.write('\n')
    
    table[data[1][3]]-=min(0,float(data[1][1]))
    
    for d in range(2,len(data)):
        if len(data[d])==3: break
        if data[d][0]!=data[d-1][0]:
            file.write(data[d-1][0])
            for i in range(len(lookup)):
                file.write(","+str(table[lookup[i]]))
                table[lookup[i]] = 0
            file.write('\n')
        table[data[d][3]]-=min(0,float(data[d][1]))
        
    file.close()
    
def makeMonthly(data,lookup):
    
    file = open("Monthly.csv", 'w')   
    
    table = {key:0 for key in lookup}
    
    # headers
    file.write("Month/Year")
    for i in range(len(lookup)):
        file.write(","+lookup[i])
    file.write('\n')
    
    table[data[1][3]]-=min(0,float(data[1][1]))
    
    for d in range(2,len(data)):
        if len(data[d])==3: break
        if data[d][0].split('/')[0]!=data[d-1][0].split('/')[0]:
            file.write(data[d-1][0].split('/')[0]+'/'+data[d-1][0].split('/')[2])
            for i in range(len(lookup)):
                file.write(","+str(table[lookup[i]]))
                table[lookup[i]] = 0
            file.write('\n')
        table[data[d][3]]-=min(0,float(data[d][1]))
    file.write(data[-1][0].split('/')[0]+'/'+data[-1][0].split('/')[2])
    for i in range(len(lookup)):
        file.write(","+str(table[lookup[i]]))
        table[lookup[i]] = 0
    file.write('\n')        
        
    file.close()
    

def start():
    
    data = initialize()
    categories = createCategories()
    result = process( categories, data )
    export(result[0])
    
    makeDaily(result[1],result[2])
    makeMonthly(result[1],result[2])


start()
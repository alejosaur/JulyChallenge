def operate(a, operation, b):
    if(operation == "plus"):
        return(float(a) + float(b))
    elif(operation == "minus"):
        return(float(a) - float(b))
    elif(operation == "multiplied"):
        return(float(a) * float(b))
    elif(operation == "divided"):
        if(int(b) != 0):
            return(float(a) / float(b))
        else:
            print("\nAre you dividing by 0?\nDo you think life is a game?")

def checkOdds(tkns):
    for i in range(0,len(tkns),2):
        try:
            float(tkns[i])
        except:
            return False
            
    for i in range(1,len(tkns),2):
        if(not(tkns[i] == "plus" or tkns[i] == "minus" or tkns[i] == "multiplied" or tkns[i] == "divided")):
            return False
            
    return True
    
while(True):
    print("\nWrite the expression you want to evaluate, or \"exit\" to exit: ", end="")
    baseString = input().lower();
    
    if(baseString != "exit"):
        tokens = baseString.split(' ');

        while("what" in tokens):
            tokens.remove("what")
        while("is" in tokens):
            tokens.remove("is")
        while("by" in tokens):
            tokens.remove("by")
                
        if(checkOdds(tokens)):
            valid = True;
            while(len(tokens)>1 and valid):
                result = operate(tokens[0], tokens[1], tokens[2])
                tokens.pop(0)
                tokens.pop(0)
                tokens[0] = result
                valid = checkOdds(tokens);
            
            if(valid):
                if(tokens[0]-int(tokens[0]) == 0.0):
                    print("\nThe result is:", int(tokens[0]))
                else:
                    print("\nThe result is:", tokens[0])
        else:
            print("\nPlease check the input :(")
    else: 
        break
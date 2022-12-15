
def arithmetic_arranger(problems,sumtotal=False):
    
    if len(problems)>5:
        return 'Error: Too many problems.'
        quit()
    
    maxlen=[]
    topnum=[]
    undernum=[]     
    lines=[]
    sumline=[]
    operator=['+','-']
    for i in problems:
        num=[]
        b=str(i.split()[0].strip())
        c=str(i.split()[2].strip())
        op=i.split()[1]
        try:
            num1=int(i.split()[0])
            num2=int(i.split()[2])
        except:
            return 'Error: Numbers must only contain digits.'
            quit()

        if op not in operator:
            return 'Error: Operator must be "+" or "-".'
            quit()

        if len(b) > 4 or len(c) > 4:
            return 'Error: Numbers cannot be more than four digits.'  
            quit()

        if op in '+':
            sum=num1+num2
            num.insert(3,str(sum))
        elif op in '-': 
            sum =num1-num2
            num.insert(3,str(sum))

        s=max(num1,num2,sum)        
        j=int(len(str(s)))
        maxlen.append(j)

        line=('-'*j)+'--'+' '*4
        b=' '*2+b.rjust(j)+' '*4
        c=op+' '+c.rjust(j)+' '*4

        num.insert(0,b)
        num.insert(1,c)
        num.insert(2,line)

        if sum < 0:
            
            if len(num[3])==5:
                suml=' '+num[3].rjust(j)+' '*4
            elif len(num[3])<5:
                suml=' '*2+num[3].rjust(j)+' '*4

        else:
            suml=' '*2+num[3].rjust(j)+' '*4
        topnum.append(b)
        undernum.append(c)
        lines.append(line)
        sumline.append(suml)

    for i in topnum:
        o=print(f'{i}',end='')
    print('')

    for i in undernum:
        p=print(f'{i}',end='')
    print('')
    for i in lines:
        q=print(f'{i}',end='')
    print('')
    if sumtotal==True:
        for i in sumline:
            r=print(f'{i}',end='')


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
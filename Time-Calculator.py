



def add_time(time=0,add=0,week=0):
    all_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    #time
    t=time.split()
    meridiem=str(t[1])
    t0=t[0].split(':')
    hr=int(t0[0])
    min=int(t0[1])
    #add
    ad=add.split()
    ad0=ad[0].split(':')
    hr_add=int(ad0[0])
    min_add=int(ad0[1])
    
    days=int(hr_add/24)
    hr2=int(hr_add%24)
    
    print(hr,min,hr_add,min_add)
    div=int((min+min_add)/60)
    rest=(min+min_add)%60
    if div>0 or hr2>0:
        hr=hr+hr2+div
    print(hr)
    if hr>12:
        hr=hr-12 
        if meridiem =='AM':
            meridiem ='PM'      
        else:
            meridiem ='AM'
            t1=str(hr)+':'+str(rest)+' '+meridiem+' '+'(next day)'
            print(t1)
            for i,x in enumerate(all_week):
                if week==x:
                    y=i+1
                if i==y:
                    week=x
    print(week)
        
    t1=str(hr)+':'+str(rest)+' '+meridiem

    



add_time("11:30 PM","2:32", "Monday")
    
    
    

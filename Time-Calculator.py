



def add_time(time=0,add=0,week=0):
    all_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    measure={}
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
    
    min_to_hr=int((min+min_add)/60)
    rest=(min+min_add)%60

    hr=hr+min_to_hr+hr_add

    measure['days']=int(hr/24)    
    
    for i,x in enumerate(all_week):
        if week==x:
            y=i+measure['days']            
        if i==y:
            measure['week']=x
            
    if measure['days'] == 1:
        measure['total_days']='(next day)'
        
    if measure['days'] > 1:
        measure['total_days']='('+str(measure['days'])+ ' days later'+')'

    
    hr=int(hr%24)
    if hr>=13:
        hr=hr-12 
        if meridiem =='AM':
            meridiem ='PM'      
        else:
            meridiem ='AM'
            

    t1=str(hr)+':'+str(rest)+' '+meridiem
    print(t1)

        
    t1=str(hr)+':'+str(rest)+' '+meridiem

    print(measure)

add_time("11:30 AM","50:32", "Monday")
    
    
    

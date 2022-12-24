



def add_time(time=0,add=0,week=0):
    all_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    t=time.split()
    t0=t[0].split(':')
    hr=int(t0[0])
    min=int(t0[1])
    ad=add.split()
    ad0=ad[0].split(':')
    hr_add=int(ad0[0])
    min_add=int(ad0[1])
    print(hr,min,hr_add,min_add)
    div=int((min+min_add)/60)
    rest=(min+min_add)%60
    if div>0:
        hr=hr+hr_add+div
    t1=str(hr)+':'+str(rest)   
    print(t1)

    





add_time("11:30 AM","2:32", "Monday")
    
    
    
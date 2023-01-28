


class add_time(): 
    def __init__(self,hours=0,add=0,week=0,hr=0,min=0,hr_add=0,min_add=0):
        self.hours=hours
        self.add=add
        self.week=week
        self.hr=hr
        self.min=min
        self.hr_add=hr_add
        self.min_add=min_add
        self.measure={}
        self.all_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    def __split_hours(self):
        t=self.hours.split()
        meridiem=str(t[1])
        t0=t[0].split(':')
        self.hr=int(t0[0])
        self.min=int(t0[1])
        return self.hr,self.min
    
    def __split_add(self):
        ad=self.add.split()
        ad0=ad[0].split(':')
        self.hr_add=int(ad0[0])
        self.min_add=int(ad0[1])
        return self.hr_add,self.min_add
    
    def transform_time(self):
        self.__split_hours()
        self.__split_add()
        min_to_hr=int((self.min+self.min_add)/60)
        rest=(self.min+self.min_add)%60
        return min_to_hr,rest
    
    def days(self):
        
        hr=self.hr+min_to_hr+self.hr_add
        measure['days']=int(hr/24)
        
    def transform_week(self):
        for i,x in enumerate(self.all_week):
            if x == self.week:
                numweek=i
        return numweek
        
        
    def __str__(self):
        return f'{self.hr}'  


        


a=add_time("11:30 AM","60:32", "Wednesday")



    

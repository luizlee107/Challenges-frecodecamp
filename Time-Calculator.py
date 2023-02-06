class add_time(): 
    def __init__(self,hours=0,add=0,week=0,hr=0,min=0,meridiem=0,hr_add=0,min_add=0,days=0,total_days=0):
        self.hours=hours
        self.add=add
        self.week=week
        self.hr=hr
        self.min=min
        self.meridiem=meridiem
        self.hr_add=hr_add
        self.min_add=min_add
        self.days=days
        self.total_days=total_days
        self.all_week=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    def __split_hours(self):
        t=self.hours.split()
        self.meridiem=str(t[1])
        t0=t[0].split(':')
        self.hr=int(t0[0])
        self.min=int(t0[1])
        return self.hr,self.min,self.meridiem
    
    def __split_add(self):
        ad=self.add.split()
        ad0=ad[0].split(':')
        self.hr_add=int(ad0[0])
        self.min_add=int(ad0[1])
        return self.hr_add,self.min_add

    def __transform_time(self):
        self.__split_hours()
        self.__split_add()
        min_to_hr=int((self.min+self.min_add)/60)
        rest_min=(self.min+self.min_add)%60
        self.min=rest_min
        return min_to_hr,self.min
    
    def __total_days_hours(self):
        min_to_hr=self.__transform_time()[0]
        total_hrs=self.hr+min_to_hr+self.hr_add
        self.days=int(total_hrs/24)
        
        self.hours=total_hrs%24
        return self.days,self.hours
        
    def __change_meridiem(self):
        self.__total_days_hours()

        if self.hours >= 13 and self.hours < 24:
            self.hours=self.hours-12 
            if self.meridiem =='AM':
                self.meridiem ='PM' 
             
        return self.hours,self.meridiem
    
    def __format_string(self):
        self.week = self.week[0].upper() + self.week[1:].lower()    
        return self.week
    
    def __transform_week(self):
        self.__change_meridiem()
        
        if self.week !=0:
            self.__format_string()
            for i,x in enumerate(self.all_week):
                if x == self.week:
                    numweek=i            
            cont=0 
            while True:        
                for x in range(numweek,len(self.all_week)):
                    cont=cont+1
                    if cont == self.days+1:
                        self.week=self.all_week[x]
                        break
                if cont == self.days+1:
                    break        
        return self.week
    
    def __total_days(self):
        self.__transform_week()
        if self.days == 1:
            self.total_days=str('(next day)')
        if self.days > 1:
            self.total_days='('+str(self.days)+ ' days later'+')'
            
        return self.total_days
        
    def __str__(self):
        self.__total_days()
            
        if self.days == 0 and self.week != 0:
            return f'{self.hours}' + ':' + '{:02.0f}'.format(self.min) +f' {self.meridiem}'+f', {self.week}'
        if self.days == 0:
            return f'{self.hours}' + ':' + '{:02.0f}'.format(self.min) +f' {self.meridiem}'
        if self.days > 0 and self.week !=0:
            return f'{self.hours}' + ':' + '{:02.0f}'.format(self.min) +f' {self.meridiem}'+f', {self.week}'+f' {self.total_days}'
        if self.days > 0 and self.week ==0:
            return f'{self.hours}' + ':' + '{:02.0f}'.format(self.min) +f' {self.meridiem}'+f' {self.total_days}'
           

a=add_time("11:30 AM","113:32")
print(a)






    

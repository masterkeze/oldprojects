class point():
    
    def __init__(self,title='',date='',value=0.0):
        self.title = title
        self.date = date
        self.value = value

    def set_title(self,title):
        self.title = title

    def set_date(self,date):
        self.date = date

    def set_value(self,value):
        self.value = value

    def show_point(self):
        print(self.title,':',self.date,':',self.value)

class Event:

    def __init__(self, year, month, day, day_num, title, description):
        self.year = year
        self.month = month
        self.day = day
        self.day_num = day_num
        self.title = title
        self.description = description
        return
    
    # display a single event, formatted
    def display_event(self):
        if not (self.day==""):
            print(self.title + "  ~  " + self.day + " " + str(self.day_num) + " " + self.month + " " + str(self.year))

        else:
            print(self.title + "  ~  " + str(self.day_num) + " " + self.month + " " + str(self.year))

        print("\t" + self.description + "\n")
        return
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month

    def get_title(self):
        return self.title

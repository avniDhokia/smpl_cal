import csv
import os

from Event import Event

class Calendar:

    def __init__(self, calendar_name):
        self.calendar_name = calendar_name
        self.years_with_events = []
        self.event_list = []
    
    def get_name(self):
        return self.calendar_name

    # display the events of a calendar, formatted
    def display_events(self):
        print("\n~~~~~~~~~~~~~~~~~~~~~~~c a l e n d a r~~~~~~~~~~~~~~~~~~~~~~~")

        for year in self.years_with_events:
            print("\t\t\t\t\t\t\t" + str(year))
            for e in self.event_list:
                if e.get_year() == year:
                    e.display_event()
        
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return

    # check if an event with the given title already exists in this calendar
    def event_with_title_exists(self, title):
        
        for event in self.event_list:
            if event.get_title() == title:
                return True
        
        return False

    # add a new event to a calendar, and save to file
    def add_event(self, year, month, day, day_num, title, description):

        new_event = Event(year, month, day, day_num, title, description)
        self.event_list.append(new_event)

        counter = 0

        # slot in a new event so that all events remain chronological
        for y in self.years_with_events:
            if year == y:
                return

            if year < y:               

                self.years_with_events = self.years_with_events[0:counter] + [year] + self.years_with_events[counter:]
                return

            counter = counter + 1

        self.years_with_events.append(year)
        return

    # read a calendar and all its events from a .csv file
    def read_calendar(self):
        filename = self.calendar_name + ".csv"

        if (os.path.isfile(filename)):
            
            with open(filename, newline='') as csvfile:
                csv_reader = csv.reader(csvfile)

                for row in csv_reader:

                    # readable version of row data
                    year = row[0]
                    month = row[1]
                    day = row[2]
                    day_num = row[3]
                    title = row[4]
                    description = row[5]

                    if (year=="~"):
                        year = ""
                    if (month=="~"):
                        month = ""
                    if (day=="~"):
                        day = ""
                    if (day_num=="~"):
                        day_num = ""
                    if (title=="~"):
                        title = ""
                    if (description=="~"):
                        description = ""

                    self.add_event(year, month, day, day_num, title, description)
        
        else:
            print("warning: calendar with name '" + self.calendar_name + "' not found. (this is not a problem if you are only adding a new event)")
        
        return

    # save a calendar and all its events to a .csv file
    def save_calendar(self):
        # csv_fields = ["year", "month", "day", "day num", "title", "description"]

        filename = self.calendar_name + ".csv"

        with open(filename, 'w') as csvfile:
            
            csv_writer = csv.writer(csvfile)

            for event in self.event_list:
                if (event.year==""):
                    event.year = "~"
                if (event.month==""):
                    event.month = "~"
                if (event.day==""):
                    event.day = "~"
                if (event.day_num==""):
                    event.day_num = "~"
                if (event.title==""):
                    event.title = "~"
                if (event.description==""):
                    event.description = "~"
                    
                csv_writer.writerow([event.year, event.month, event.day, event.day_num, event.title, event.description])

        return

    # delete a calendar's event
    def delete_event(self, title):
    
        event_index = 0
        for event in self.event_list:

            if event.get_title() == title:
                self.event_list.pop(event_index)
                self.save_calendar()

                return
        
            event_index = event_index + 1
        
        print("event with title '" + title + "' not found")
        return

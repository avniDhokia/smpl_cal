#!/usr/bin/python3

import os
import argparse

from Calendar import Calendar


# # #  non-cli methods  # # #

# save all calendar names to a file
def save_all_calendars(filename, calendar_names_list):
    if len(calendar_names_list) == 0:

        with open(filename, 'w') as file:
            file.write("")

        return
    
    with open(filename, 'w') as file:
        for cal_name in calendar_names_list:
            file.write(cal_name + "\n")
        
    return

# append the calendar names file
def append_calendar_names(filename, calendar_name):
    
    with open(filename, 'a') as file:
        file.write(calendar_name + "\n")
        
    return

# return a list with all calendar names
def read_calendar_names(filename):
    if (os.path.isfile(filename)):
        calendar_list = []
        file = open(filename, 'r')
        line = file.readline()

        while line:
            calendar_list.append( line.strip() )
            line = file.readline()
        
        return calendar_list

    else:
        print("calendar name file does not exist, but will now be created.")
        with open(filename, 'w') as file:
            file.write("")

        return []

# delete the .csv calendar file
def destroy_calendar_file(calendar_name):
    if (calendar_exists(calendar_name)):
        os.remove(calendar_name + ".csv")
    else:
        print("calendar of name '" + calendar_name + "' not found, so could not be deleted")
    
    return

#check if the file for a calendar exists, given the name of the calendar
def calendar_exists(calendar_name):
    filename = calendar_name + ".csv"
    if (os.path.isfile(filename)):
        return True
    else:
        return False


# # #  cli methods  # # #

# create a new calendar
def create_calendar(args, calendar_names_filename):
    if args.calendar_name:
        
        if calendar_exists(args.calendar_name[0]):
            print("a calendar with name '" + args.calendar_name[0] + "' already exists")
            return
            
        new_calendar = Calendar(args.calendar_name[0])
        new_calendar.save_calendar()

        append_calendar_names(calendar_names_filename, args.calendar_name[0])

        return

# view a calendar
def view_calendar(args, calendar_names_filename):
    if args.calendar_name:
        
        if calendar_exists(args.calendar_name[0]):
            
            calendar = Calendar(args.calendar_name[0])
            calendar.read_calendar()
            calendar.display_events()
            return
        else:
            print("calendar with name '" + args.calendar_name[0] + "' not found")
            return

# list all created calendars
def ls(args, calendar_names_filename):
    calendar_names = read_calendar_names(calendar_names_filename)

    if len(calendar_names) == 0:
        print("there are no calendars")
        return
        
    print("calendar names:")
    for cal_name in calendar_names:
        print("\t" + cal_name)
    
    return

# add an event to a calendar
def add_event(args, calendar_names_filename):

    if args.calendar_name and args.event_title:

        # if the calendar does not exist, add it to the list of known calendars
        if not calendar_exists(args.calendar_name[0]):
            append_calendar_names(calendar_names_filename, args.calendar_name[0])

        cal = Calendar(args.calendar_name[0])
        cal.read_calendar()      


        # if an event with the given calendar already exists, do not add new event
        if not cal.event_with_title_exists(args.event_title[0]):

            # input event infortmation
            description = input("enter event DESCRIPTION:  ")
            year = input("YEAR: ")
            month = input("MONTH: ")
            day = input("Mon/Tue/Wed/Thu/Fri/Sat/Sun: ")
            day_num = input("DAY OF MONTH: ")
            print("")
        
            cal.add_event(year, month, day, day_num, args.event_title[0], description)
            cal.save_calendar()

        else:
            print("could not create event - an event with title '" + args.event_title[0] + "' already exists")

        return
        
# delete an event
def delete_event(args, calendar_names_filename):
    if args.calendar_name:
    
    	confirm = input("are you sure you want to delete the event '" + args.event_title[0] + "'? [y/n] ")
    	
    	if confirm=="y" or confirm == "Y":
    
            if calendar_exists(args.calendar_name[0]):
                new_cal = Calendar(args.calendar_name[0])
                new_cal.read_calendar()

                new_cal.delete_event(args.event_title[0])

    else:
	    print("cancelled")

    return

# destroy a calendar
def destroy_calendar(args, calendar_names_filename):
    if args.calendar_name:
    	confirm = input("are you sure you want to destroy the calendar '" + args.calendar_name[0] + "'? [y/n] ")

    if confirm=="y" or confirm=="Y":
        calendar_names_list = read_calendar_names(calendar_names_filename)
        index = 0

        # check if calendar name exists
        # if it does, remove it from the list using the index
        for cal_name in calendar_names_list:
            if cal_name == args.calendar_name[0]:
                calendar_names_list.pop(index)
                destroy_calendar_file(cal_name)

                save_all_calendars(calendar_names_filename, calendar_names_list)
                return
            
            index = index + 1

        print("calendar with name '" + args.calendar_name[0] + "' not found")
    else:
        print("cancelled")
    
    return

# edit an event
def edit_event(args, calendar_names_filename):
    if args.calendar_name:

        if calendar_exists(args.calendar_name[0]):
            cal = Calendar(args.calendar_name[0])
            cal.read_calendar() 

            delete_event(args, calendar_names_filename)
            add_event(args, calendar_names_filename)
        else:
            print("event with title '" + args.event_title[0] + "' does not exist")

        return



def main():

    # can change these to whatever user wants
    calendar_storage_filename = "all_calendar_names.txt"
    this_filename = "smpl_cal" # ignoring .py
    

    # setup parser for all functioning
    parser = argparse.ArgumentParser(prog = this_filename, usage = "./%(prog)s.py {create,destroy,view,add,edit,delete} ..")

    # set up subparser
    subparsers = parser.add_subparsers()


    # create_calendar command
    create_calendar_parser = subparsers.add_parser("create", help="create a new calendar")
    create_calendar_parser.add_argument('calendar_name', nargs=1, help="the name of the calendar")
    create_calendar_parser.set_defaults(func=create_calendar)

    # destroy_calendar command    
    destroy_calendar_parser = subparsers.add_parser("destroy", help="destroy a calendar")
    destroy_calendar_parser.add_argument('calendar_name', nargs=1, help="the name of the calendar")
    destroy_calendar_parser.set_defaults(func=destroy_calendar)

    # ls command    
    ls_parser = subparsers.add_parser("ls", help="list all created alendars")
    ls_parser.set_defaults(func=ls)

    # view_calendar command    
    view_calendar_parser = subparsers.add_parser("view", help="view a calendar and its events")
    view_calendar_parser.add_argument('calendar_name', nargs=1, help="the name of the calendar")
    view_calendar_parser.set_defaults(func=view_calendar)

    # add_event command
    add_event_parser = subparsers.add_parser("add", help="add an event to a calendar")
    add_event_parser.add_argument('calendar_name', nargs=1, help="the name of the calendar")
    add_event_parser.add_argument('event_title', nargs=1, help="the title of the event you want to add")
    add_event_parser.set_defaults(func=add_event)

    
    # edit_event command
    edit_event_parser = subparsers.add_parser("edit", help="edit an event in a calendar")
    edit_event_parser.add_argument('calendar_name', nargs=1, help="the name of the calendar")
    edit_event_parser.add_argument('event_title', nargs=1, help="the title of the event you want to edit")
    edit_event_parser.set_defaults(func=edit_event)

    # delete_event command    
    delete_event_parser = subparsers.add_parser("delete", help="delete an event from a calendar")
    delete_event_parser.add_argument('calendar_name', nargs=1, help="the name of the calendar")
    delete_event_parser.add_argument('event_title', nargs=1, help="the title of the event you want to delete")
    delete_event_parser.set_defaults(func=delete_event)


    args = parser.parse_args()
    args.func(args, calendar_storage_filename)

if __name__=="__main__":
    main()

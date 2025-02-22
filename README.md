# smpl_cal
A simple terminal calendar application, written in Python.

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)


## Features
- create and destroy calendars
- add, view and delete events from calendars


## Requirements
- Python
- `argparse` (in Python's standard library)


## Installation
1. Clone repository, ensuring `smpl_cal.py`, `Event.py` and `Calendar.py` are all present.
2. Run using
```bash
  ./smpl_cal.py -h
```


## Usage
To run, use ```bash
./smpl_cal.py {create,destroy,view,add,edit,delete} ..```


Positional Arguments:
- `create`: create a new calendar
- `destroy`: destroy a calendar
- `ls`: list all created alendars
- `view`: view a calendar and its events
- `add`: add an event to a calendar
- `edit`: edit an event in a calendar
- `delete`: delete an event from a calendar

Options:
  `-h`, `--help`: show this help message and exit

Examples:
- Creating a new calendar:
```bash
./smpl_cal.py create calendarName
```

- Listing all calendars:
```bash
./smpl_cal.py ls
```

- Adding a new event:
```bash
./smpl_cal.py add calendarName newEventTitle
```

- Viewing events:
```bash
./smpl_cal.py view calendarName
```


## License
This project is licensed under the MIT License.

# Write a program that creates a dictionary containing course numbers and the room numbers of the rooms where
# the courses meet. The dictionary should have the following key-value pairs:
#
# Key-Value Pairs: Room Number
# Course Number (key) / Room Number (value)
# CSC101 / 3004
# CSC102 / 4501
# CSC103 / 6755
# NET110 / 1244
# COM241 / 1411
#
# The program should also create a dictionary containing course numbers and the names of the instructors that
# teach each course. The dictionary should have the following key-value pairs:
#
# Key-Value Pairs: Instructors
# Course Number (key) / Instructor (value)
# CSC101 / Haynes
# CSC102 / Alvarado
# CSC103 / Rich
# NET110 / Burke
# COM241 / Lee
#
# The program should also create a dictionary containing course numbers and the meeting times of each course.
# The dictionary should have the following key-value pairs:
#
# Key-Value Pairs: Meeting Time
# Course Number (key) / Meeting Time (value)
# CSC101 / 8:00 am
# CSC102 / 9:00 am
# CSC103 / 10:00 am
# NET110 / 11:00 am
# COM241 / 1:00 pm
#
# The program should let the user enter a course number and then it should display the course's room number,
# instructor, and meeting time.

def print_details(course_num):
    print(f"\nDetails for {course_num.upper()}")
    print("Room:", rooms[course_num.upper()])
    print("Instructor:", instructors[course_num.upper()])
    print("Meeting Time:", meeting_time[course_num.upper()])


rooms = {"CSC101": 3004, "CSC102": 4501, "CSC103": 6755, "NET110": 1244, "COM241": 1411}
instructors = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich", "NET110": "Burke", "COM241": "Lee"}
meeting_time = {"CSC101": "8:00 am", "CSC102": "9:00 am", "CSC103": "10:00 am", "NET110": "11:00 am",
                "COM241": "1:00 pm"}
keep_searching = True

while keep_searching:
    print("Which course would you like to look up?")
    for key in rooms.keys():
        print(key)
    course = input("Enter course number: ")

    if course.upper() in rooms.keys():
        print_details(course)
    else:
        print("\nThe course you entered is not in your list of courses. Would you like to add it?")
        add_course = input("Y or N: ")

        if add_course.upper() == "Y":
            rooms[course.upper()] = input("Enter room number: ")
            instructors[course.upper()] = input("Enter instructor: ")
            meeting_time[course.upper()] = input("Enter meeting time: ")

            print_details(course)

    print("\nWould you like to look up another course?")
    choice = input("Y or N: ")

    if choice.upper() == "N":
        keep_searching = False

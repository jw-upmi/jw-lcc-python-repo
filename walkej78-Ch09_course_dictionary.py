# define dictionary function -- dictionary is the prompt to return
def course_dictionary(dictionary):
    # create course_room dictionary
    course_room = {'CS101':'3004', 
                   'CS102':'4501', 
                   'CS103':'6755', 
                   'NT110':'1244',
                   'CM241':'1411'}
    # create course_instructor dictionary
    course_instructor = {'CS101':'Haynes', 
                   'CS102':'Alvarado', 
                   'CS103':'Rich', 
                   'NT110':'Burke',
                   'CM241':'Lee'}
    # create course_meeting_time dictionary
    course_meeting_time = {'CS101':'8:00 a.m.', 
                   'CS102':'9:00 a.m.', 
                   'CS103':'10:00 a.m.', 
                   'NT110':'11:00 a.m.',
                   'CM241':'1:00 p.m.'}
    # what do you want to return?
    if dictionary == 'course_room':
        return course_room
    elif dictionary =='course_instructor':
        return course_instructor
    elif dictionary == 'course_meeting_time':
        return course_meeting_time
    else:
        # n_f is used in course_lookup for not found error
        return 'n_f'
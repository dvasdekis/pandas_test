import sys
import pd_q2 as pd


# Table1 contains the attendance data at a school for students for each day.
# It contains the fields below as a tuple (date, student_id, attendance).
#
# date          | student_id | attendance
# --------------|------------|-------------
# 2017-04-20'   | 1          | True
#

# Table2 contains the student profile data keeping track of attributes
# of each student at the school.
#
# Table 2
# student_id | school_id | grade_level | date_of_birth | hometown
# -----------|-----------|-------------|---------------|-----------
# A          | X         | 10
# B          | Y         | 7
# C          | Y         | 8

######################################################
## Question 2
######################################################
# Given given a table that contains students personal information including student_id and school_id.
# Which grade level currently has the most students in this school district?

def countStudents(table1, table2):
    """
    This function takes attendance and student data
    Returns integer grade with most students
    """
    ## TODO by student

    df1 = pd.DataFrame(table1, columns=["date", "student_id", "attendance"])
    df2 = pd.DataFrame(table2, columns=["student_id", "school_id", "grade_level", "date_of_birth", "hometown"])
    df2_glgrouped = df2.groupby("grade_level")['student_id'].count()
    df2_max = df2_glgrouped
    grade = df2_max
    return grade


######################################################
## SUBMISSION CODE - DO NOT CHANGE
######################################################
def submit(out):
    print(out)


def main():
    table1, table2 = getData()  # readline()
    out = countStudents(table1, table2)
    submit(out)


def getData():
    table1 = [('2017-04-20', 'STU01', True)
        , ('2017-04-19', 'STU01', True)
        , ('2017-04-18', 'STU01', True)
        , ('2017-04-17', 'STU01', True)
        , ('2017-04-16', 'STU01', True)
        , ('2017-04-15', 'STU01', True)
        , ('2017-04-14', 'STU01', True)
        , ('2017-04-13', 'STU01', True)
        , ('2017-04-12', 'STU01', True)
        , ('2017-04-11', 'STU01', True)
        , ('2017-04-10', 'STU01', True)
        , ('2017-04-09', 'STU01', True)
        , ('2017-04-08', 'STU01', True)
        , ('2017-04-07', 'STU01', True)
        , ('2017-04-06', 'STU01', True)
        , ('2017-04-05', 'STU01', True)
        , ('2017-04-04', 'STU01', True)
        , ('2017-04-03', 'STU01', True)
        , ('2017-04-02', 'STU01', True)
        , ('2017-04-01', 'STU01', True)
        , ('2017-04-20', 'STU02', True)
        , ('2017-04-19', 'STU02', False)
        , ('2017-04-18', 'STU02', True)
        , ('2017-04-17', 'STU02', True)
        , ('2017-04-16', 'STU02', True)
        , ('2017-04-15', 'STU02', False)
        , ('2017-04-14', 'STU02', True)
        , ('2017-04-13', 'STU02', True)
        , ('2017-04-12', 'STU02', True)
        , ('2017-04-11', 'STU02', False)
        , ('2017-04-10', 'STU02', True)
        , ('2017-04-09', 'STU02', True)
        , ('2017-04-08', 'STU02', True)
        , ('2017-04-07', 'STU02', False)
        , ('2017-04-06', 'STU02', True)
        , ('2017-04-05', 'STU02', True)
        , ('2017-04-04', 'STU02', True)
        , ('2017-04-03', 'STU02', True)
        , ('2017-04-02', 'STU02', True)
        , ('2017-04-01', 'STU02', True)
        , ('2017-04-20', 'STU03', True)
        , ('2017-04-19', 'STU03', True)
        , ('2017-04-18', 'STU03', True)
        , ('2017-04-17', 'STU03', True)
        , ('2017-04-16', 'STU03', True)
        , ('2017-04-15', 'STU03', True)
        , ('2017-04-14', 'STU03', True)
        , ('2017-04-13', 'STU03', True)
        , ('2017-04-12', 'STU03', False)
        , ('2017-04-11', 'STU03', False)
        , ('2017-04-10', 'STU03', False)
        , ('2017-04-09', 'STU03', False)
        , ('2017-04-08', 'STU03', False)
        , ('2017-04-07', 'STU03', True)
        , ('2017-04-06', 'STU03', True)
        , ('2017-04-05', 'STU03', True)
        , ('2017-04-04', 'STU03', True)
        , ('2017-04-03', 'STU03', True)
        , ('2017-04-02', 'STU03', True)
        , ('2017-04-01', 'STU03', True)
        , ('2017-04-20', 'STU04', True)
        , ('2017-04-19', 'STU04', True)
        , ('2017-04-18', 'STU04', True)
        , ('2017-04-17', 'STU04', True)
        , ('2017-04-16', 'STU04', True)
        , ('2017-04-15', 'STU04', True)
        , ('2017-04-14', 'STU04', True)
        , ('2017-04-13', 'STU04', True)
        , ('2017-04-12', 'STU04', True)
        , ('2017-04-11', 'STU04', True)
        , ('2017-04-10', 'STU04', True)
        , ('2017-04-09', 'STU04', True)
        , ('2017-04-08', 'STU04', True)
        , ('2017-04-07', 'STU04', True)
        , ('2017-04-06', 'STU04', False)
        , ('2017-04-05', 'STU04', False)
        , ('2017-04-04', 'STU04', False)
        , ('2017-04-03', 'STU04', False)
        , ('2017-04-02', 'STU04', False)
        , ('2017-04-01', 'STU04', True)]

    table2 = [('STU01', 'SC01', 8, '1986-10-12', 'Sydney')
        , ('STU02', 'SC01', 12, '1986-10-13', 'Sydney')
        , ('STU03', 'SC02', 12, '1986-10-14', 'Sydney')
        , ('STU04', 'SC02', 8, '1986-10-15', 'Sydney')
        , ('STU05', 'SC02', 10, '1986-10-16', 'Sydney')
        , ('STU06', 'SC01', 12, '1986-10-17', 'Sydney')
        , ('STU07', 'SC01', 11, '1986-10-18', 'Sydney')
        , ('STU08', 'SC02', 12, '1986-10-19', 'Canberra')
        , ('STU09', 'SC02', 9, '1986-10-20', 'Canberra')
        , ('STU10', 'SC02', 8, '1986-10-21', 'Canberra')
        , ('STU11', 'SC02', 8, '1986-10-22', 'Canberra')
        , ('STU12', 'SC02', 11, '1986-10-23', 'Canberra')
        , ('STU13', 'SC02', 11, '1986-10-24', 'Melbourne')
        , ('STU14', 'SC02', 11, '1986-10-25', 'Melbourne')
        , ('STU15', 'SC02', 12, '1986-10-26', 'Melbourne')
        , ('STU16', 'SC02', 12, '1986-10-27', 'Melbourne')
        , ('STU17', 'SC02', 11, '1986-10-28', 'Melbourne')]

    return table1, table2


if __name__ == '__main__':
    main()

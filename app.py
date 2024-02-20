# student id:s3973503
# Name:Prathiksha Chamarajanagar Padmaprasad
# Highest part attempted:High Distiction
# Problems in code:None

# Importing the necessary libraries
import os
import sys
from datetime import datetime

# Create class called course to store all the corse related info
class Course:
    def __init__(self,course_id,course_name,course_credit,course_offered):
        self.__course_id=course_id
        self.__course_name=course_name
        self.__course_credit=course_credit
        self.__course_offered=course_offered
    
    # Getter method to get course_id
    @property
    def course_id(self):
        return self.__course_id

    # Setter method to set course id   
    @course_id.setter
    def course_id(self, course_id):
        self.__course_id = course_id
    
    # Getter method to get course_name
    @property
    def course_name(self):
        return self.__course_name
    
    # setter method to set course_name
    @course_name.setter
    def course_name(self, course_name):
        self.__course_name = course_name

    # getter method to get course_credit
    @property
    def course_credit(self):
        return self.__course_credit
    
    # setter method to set course credit
    @course_credit.setter
    def course_credit(self, course_credit):
        self.__course_credit = course_credit

    # getter method to get course_offered
    @property
    def course_offered(self):
        return self.__course_offered
    
    # setter method to get course_offered
    @course_offered.setter
    def course_offered(self, course_offered):
        self.__course_offered = course_offered

    # function to calculate nfinishing,nongoing,average of the course
    def compute_statistics(self):
        nfinishing=0
        nongoing=0
        sum=0
        for student in Results.list_of_students:
            course_obj = Results.results_of_students[student]
            if self in course_obj:
                if course_obj[self]!="--": 
                        nfinishing+=1
                        sum+=course_obj[self]
                elif course_obj[self]=="--":
                    nongoing+=1  
        average=round(sum/nfinishing,2) 
        return [nfinishing,nongoing,average]



# Creating a calss called core and making it as child class and inheriting all the details from main class course 
class Core(Course):
    def __init__(self,course_id,course_name,course_credit):
        super().__init__(course_id,course_name,course_credit,"ALL")

# Creating a calss called core and making it as child class and inheriting all the details from main class course 
class Elective(Course):
    def __init__(self,course_id,course_name,course_offered):
        super().__init__(course_id,course_name,6,course_offered)

# Create a class called student to store all the student related information
class Student:
    def __init__(self,student_id,student_name,student_mode):
        self.__student_id= student_id
        self.__student_name= student_name
        self.__student_mode= student_mode

    # getter method to get student id  
    @property
    def student_id(self):
        return self.__student_id
    
    # setter method to get student id  
    @student_id.setter  
    def student_id(self, student_id):
        self.__student_id = student_id
    
    # getter method to get student name 
    @property
    def student_name(self):
        return self.__student_name
    
    # setter method to get student name  
    @student_name.setter  
    def student_name(self, student_name):
        self.__student_name = student_name

    # getter method to get student mode 
    @property
    def student_mode(self):
        return self.__student_mode

    # setter method to get student mode  
    @student_mode.setter  
    def student_mode(self, student_mode):
        self.__student_mode = student_mode
    
    # Function to calculate statistic of students
    def compute_statistics_students(self):
        nfinishing=0
        nongoing=0
        sum=0
        gpa=0
        weighted_gpa=0
        credits=0
        course_obj = Results.results_of_students[self]
        for course, result in course_obj.items():
            course_credit = int(course.course_credit)
            if result != "--":
                nfinishing+=1
                sum=sum+result
                if result>=79.5:
                    gpa+=4
                    weighted_gpa+= (4*course_credit)
                    credits+= course_credit
                elif result>=69.5 and result< 79.5:
                    gpa+=3
                    weighted_gpa+= (3*course_credit)
                    credits+= course_credit
                elif result>=59.5 and result< 69.5:
                    gpa+=2
                    weighted_gpa+= (2*course_credit)
                    credits+= course_credit
                elif result>=49.5 and result< 59.5:
                    gpa+=1
                    weighted_gpa+= (1*course_credit)
                    credits+= course_credit
                else:
                    gpa+=0
                    weighted_gpa+= (0*course_credit)
                    credits+= course_credit
            elif result == "--":
                nongoing+=1
        average_weighted_gpa = round(weighted_gpa / credits,2)
        average_gpa = round(gpa/nfinishing,2)
        average_of_student=round(sum/nfinishing,2)

        enrolled = ""
        if self.student_mode == "FT":
            if nfinishing + nongoing < 4:
                enrolled = " (!)"
        elif self.student_mode == "PT":
            if nfinishing + nongoing < 2:
                enrolled = " (!)"

        return [nfinishing,nongoing,average_of_student,average_gpa,enrolled, average_weighted_gpa]

# Create a class called Post Graduate which is child class of student and inheriting all the properties from student class
class PostGraduate(Student):
    def __init__(self,student_id,student_name,student_mode):
        super().__init__(student_id,student_name,student_mode) 

# Create a class called Under Graduate which is child class of student and inheriting all the properties from student class
class UnderGraduate(Student):
    def __init__(self,student_id,student_name,student_mode):
        super().__init__(student_id,student_name,student_mode)

# Create a class called results to store the results wit respect to course and student   
class Results:
    list_of_courses=[]
    list_of_students=[]
    results_of_students={}
    
    # function to find the course is there or not in the list of courses
    def __find_course(self,course_id):
        for course in Results.list_of_courses:
            if course.course_id == course_id:
                return course
        return None
    # function to find the course is there or not in the list of courses
    def __find_student(self,student_id):
        for student in Results.list_of_students:
            if student.student_id == student_id:
                return student
        return None
    
     #Function to read the course file   
    def read_course(self,course_details_path):
        try:
            f = open(course_details_path, 'r')
        except:
            print("Course file does not exist")
            sys.exit(1)

        try:
            for line in f.readlines():
                course_details=line.split(",")
                
                if not (course_details[0].strip().startswith('COSC') or course_details[0].strip().startswith('ISYS') or course_details[0].strip().startswith('MATH')): 
                    print("The {} doesn't start with either  COSC, ISYS or MATH".format(course_details[0].strip()))
                    sys.exit(1)

                if len(course_details)==4:
                    course=Core(course_details[0].strip(),course_details[2].strip(),course_details[3].strip())
                elif len(course_details)==5:
                    course=Elective(course_details[0].strip(),course_details[2].strip(),course_details[4].strip())
                Results.list_of_courses.append(course)
            f.close()
        except:
            print("Reading course file error")
            sys.exit(1)
    # Function to read the student file
    def read_student(self,student_details_path):
        try:
            f = open(student_details_path, 'r')
        except:
            print("Studnet file does not exist")
            sys.exit(1)

        try:
            for line in f.readlines():
                student_details=line.split(",")

                if not student_details[0].strip().startswith('S'):
                    print("The {} doesn’t start with the letter S;".format(student_details[0].strip()))
                    sys.exit(1)
                    
                if 'UG' == student_details[2].strip():
                    student=UnderGraduate(student_details[0].strip(),student_details[1].strip(),"FT")
                    Results.list_of_students.append(student)
                elif  'PG' == student_details[2].strip():
                    student=PostGraduate(student_details[0].strip(),student_details[1].strip(),student_details[3].strip())
                    Results.list_of_students.append(student)
            f.close()
        except:
            print("Reading student file error")
            sys.exit(1)

    # Function to read results file
    def read_results(self,results_details_path):
        f = open(results_details_path, 'r')
        if os.path.getsize(results_details_path) == 0:
            print("Results file is empty")
            sys.exit(1)

        for line in f.readlines():
            results_details = line.split(",")
            student=self.__find_student(results_details[0].strip())
            course=self.__find_course(results_details[1].strip())

            if results_details[2].strip() != "":
                try:
                    float(results_details[2].strip())
                except:
                    print("Invalid Score in results.txt file")
                    sys.exit(1)

            if results_details[2].strip() == "":
                result="--"
            else:
                result=round(float(results_details[2].strip()),2)  

            if student in Results.results_of_students:
                # Update existing dictionary with new key-value pair
                Results.results_of_students[student][course] = result
            else:
                # Create a new dictionary and assign it as the value for the student key
                Results.results_of_students[student] = {course: result}

        f.close()
    # function to sort the course information using average from highest to lowest
    def __sort_course_info(self):
        Results.list_of_courses.sort(key=lambda course:course.compute_statistics()[2],reverse=True)
    
    # function to sort the student infromation using WPGA(4) from highest to lowest
    def __sort_student_info(self):
        Results.list_of_students.sort(key=lambda student:student.compute_statistics_students()[-1],reverse=True)
   
    # function to display course information
    def __display_course_info(self):
        print("")
        print("Course Information")
        average_core_course=100
        average_elective_course=100
        core_course_id=""
        elective_course_id=""
        print("".join(["{}".format("-") for i in range(105)]))
        print("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format("CourseID","Name","Type","Credit","Semester","Average","Nfinishing","Nongoing"))
        print("".join(["{}".format("-") for i in range(105)]))
        self.__sort_course_info()
        for course in Results.list_of_courses:
            if isinstance(course,Core):
                nfinishing,nongoing,average = course.compute_statistics()
                if average < average_core_course:
                    average_core_course=average
                    core_course_id=course.course_id

                print("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(course.course_id,course.course_name,"c",course.course_credit,"All",average,nfinishing,nongoing))
        print("".join(["{}".format("-") for i in range(105)]))
        print("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format("CourseID","Name","Type","Credit","Semester","Average","Nfinishing","Nongoing"))
        print("".join(["{}".format("-") for i in range(105)]))
        for course in Results.list_of_courses:
            if isinstance(course,Elective):
                nfinishing,nongoing,average = course.compute_statistics()
                if average < average_elective_course:
                    average_elective_course=average
                    elective_course_id=course.course_id
                print("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(course.course_id,course.course_name,"E",course.course_credit,course.course_offered,average,nfinishing,nongoing))
        print("")
        print("COURSE SUMMARY")
        print("The most difficult core course is {} with an average score of {}".format(core_course_id,average_core_course))
        print("The most difficult elective course is {} with an average score of {}".format(elective_course_id,average_elective_course))
   
    # function to write the contenst back to reports file
    def __write_to_reports(self):
        f=open("reports.txt",'a')
        f.write("\n")
        f.write("Course Information\n")
        average_core_course=100
        average_elective_course=100
        core_course_id=""
        elective_course_id=""
        f.write("".join(["{}".format("-") for i in range(105)]))
        f.write("\n")
        f.write("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}\n".format("CourseID","Name","Type","Credit","Semester","Average","Nfinishing","Nongoing"))
        f.write("".join(["{}".format("-") for i in range(105)]))
        f.write("\n")
        for course in Results.list_of_courses:
            if isinstance(course,Core):
                nfinishing,nongoing,average = course.compute_statistics()
                if average < average_core_course:
                    average_core_course=average
                    core_course_id=course.course_id

                f.write("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}\n".format(course.course_id,course.course_name,"c",course.course_credit,"All",average,nfinishing,nongoing))
        f.write("".join(["{}".format("-") for i in range(105)]))
        f.write("\n")
        f.write("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}\n".format("CourseID","Name","Type","Credit","Semester","Average","Nfinishing","Nongoing"))
        f.write("".join(["{}".format("-") for i in range(105)]))
        f.write("\n")
        for course in Results.list_of_courses:
            if isinstance(course,Elective):
                nfinishing,nongoing,average = course.compute_statistics()
                if average < average_elective_course:
                    average_elective_course=average
                    elective_course_id=course.course_id
                f.write("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}\n".format(course.course_id,course.course_name,"E",course.course_credit,course.course_offered,average,nfinishing,nongoing))
        f.write("\n")
        f.write("COURSE SUMMARY\n")
        f.write("The most difficult core course is {} with an average score of {}\n".format(core_course_id,average_core_course))
        f.write("The most difficult elective course is {} with an average score of {}\n".format(elective_course_id,average_elective_course))
        f.close()
   
    # function to display the student information
    def __display_student_info(self):
        dotted_line_range=115
        print("")
        print("STUDENT INFORMATION")
        print("".join(["{}".format("-") for i in range(dotted_line_range)]))
        print("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format("StudentId","Name","Type","Mode","GPA(100)","GPA(4)","WGPA(4)","Nfinishing","Nongoing"))
        print("".join(["{}".format("-") for i in range(dotted_line_range)]))
        average_gpa_ug=0
        average_gpa_pg=0
        gpa_ug_id=""
        gpa_pg_id=""
        self.__sort_student_info()
        for student in Results.list_of_students:
            if isinstance(student,PostGraduate):
                nfinishing,nongoing,average,average_gpa,enrolled, average_weighted_gpa= student.compute_statistics_students()
                if average_gpa > average_gpa_pg:
                    average_gpa_pg = average_gpa
                    gpa_pg_id = student.student_id
                student_name = student.student_name
                if enrolled == " (!)":
                    student_name += enrolled
                average = "{:.2f}".format(average)
                average_gpa =  "{:.2f}".format(average_gpa)
                average_weighted_gpa = "{:.2f}".format(average_weighted_gpa)
                print("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(student.student_id,student_name,"PG",student.student_mode,average,average_gpa,average_weighted_gpa,nfinishing,nongoing))
        print("".join(["{}".format("-") for i in range(dotted_line_range)]))
        print("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format("StudentId","Name","Type","Mode","GPA(100)","GPA(4)","WGPA(4)","Nfinishing","Nongoing"))
        print("".join(["{}".format("-") for i in range(dotted_line_range)]))
        for student in Results.list_of_students:
            if isinstance(student,UnderGraduate):
                nfinishing,nongoing,average,average_gpa,enrolled, average_weighted_gpa = student.compute_statistics_students()
                if average_gpa > average_gpa_ug:
                    average_gpa_ug = average_gpa
                    gpa_ug_id = student.student_id
                student_name = student.student_name
                if enrolled == " (!)":
                    student_name += enrolled
                average = "{:.2f}".format(average)
                average_gpa =  "{:.2f}".format(average_gpa)
                average_weighted_gpa = "{:.2f}".format(average_weighted_gpa)
                print("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(student.student_id,student_name,"UG",student.student_mode,average,average_gpa,average_weighted_gpa,nfinishing,nongoing))
        print("")
        print("STUDENT SUMMARY")
        print("The best PG student is {} with a GPA score of {}.".format(gpa_pg_id, "{:.2f}".format(average_gpa_pg)))
        print("The best UG student is {} with a GPA score of {}.".format(gpa_ug_id, "{:.2f}".format(average_gpa_ug)))
   
    # function to display the student information back to reports
    def __write_student_info(self):
        dotted_line_range=115
        f = open("reports.txt", "a")
        f.write("\n")
        f.write("STUDENT INFORMATION\n")
        f.write("".join(["{}".format("-") for i in range(dotted_line_range)]))
        f.write("\n")
        f.write("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}\n".format("StudentId","Name","Type","Mode","GPA(100)","GPA(4)","WPGA(4)","Nfinishing","Nongoing"))
        f.write("".join(["{}".format("-") for i in range(dotted_line_range)]))
        f.write("\n")
        average_gpa_ug=0
        average_gpa_pg=0
        gpa_ug_id=""
        gpa_pg_id=""
        for student in Results.list_of_students:
            if isinstance(student,PostGraduate):
                nfinishing,nongoing,average,average_gpa,enrolled,average_weighted_gpa= student.compute_statistics_students()
                if average_gpa > average_gpa_pg:
                    average_gpa_pg = average_gpa
                    gpa_pg_id = student.student_id
                student_name = student.student_name
                if enrolled == " (!)":
                    student_name += enrolled
                average = "{:.2f}".format(average)
                average_gpa =  "{:.2f}".format(average_gpa)
                average_weighted_gpa = "{:.2f}".format(average_weighted_gpa)
                f.write("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}\n".format(student.student_id,student_name,"PG",student.student_mode,average,average_gpa,average_weighted_gpa,nfinishing,nongoing))
        f.write("".join(["{}".format("-") for i in range(dotted_line_range)]))
        f.write("\n")
        f.write("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}\n".format("StudentId","Name","Type","Mode","GPA(100)","GPA(4)","WPGA(4)","Nfinishing","Nongoing"))
        f.write("".join(["{}".format("-") for i in range(dotted_line_range)]))
        f.write("\n")
        for student in Results.list_of_students:
            if isinstance(student,UnderGraduate):
                nfinishing,nongoing,average,average_gpa,enrolled,average_weighted_gpa = student.compute_statistics_students()
                if average_gpa > average_gpa_ug:
                    average_gpa_ug = average_gpa
                    gpa_ug_id = student.student_id
                student_name = student.student_name
                if enrolled == " (!)":
                    student_name += enrolled
                average = "{:.2f}".format(average)
                average_gpa =  "{:.2f}".format(average_gpa)
                average_weighted_gpa = "{:.2f}".format(average_weighted_gpa)
                f.write("{:15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}\n".format(student.student_id,student_name,"UG",student.student_mode,average,average_gpa,average_weighted_gpa,nfinishing,nongoing))
        
        f.write("\n")
        f.write("STUDENT SUMMARY\n")
        f.write("The best PG student is {} with a GPA score of {}.\n".format(gpa_pg_id, "{:.2f}".format(average_gpa_pg)))
        f.write("The best UG student is {} with a GPA score of {}.\n".format(gpa_ug_id, "{:.2f}".format(average_gpa_ug)))
        f.write("\n")
    
    # functions to write the results back to reports.txt
    def __write_results(self):
        f = open("reports.txt", "w")
        now = datetime.now()
        formatted_datetime = now.strftime("%d/%m/%Y %H:%M:%S")
        f.write("The report generated time:{}\n".format(formatted_datetime))
        f.write("RESULTS\n")
        f.write("".join(["{}".format("-") for i in range(75)]))
        f.write("\n")
        course_title ="".join("{:<12}".format(value.course_id) for value in Results.list_of_courses)
        f.write("{:15} {:<12}\n".format("Student Ids", course_title))
        f.write("".join(["{}".format("-") for i in range(75)]))
        f.write("\n")
        count_of_results=0
        count_of_pass_results=0

        for student in Results.list_of_students:
            course_obj = Results.results_of_students[student]
            course_title = ""
            for course in Results.list_of_courses:
                if course not in course_obj:
                    course_title = course_title + "".join("{:<12}".format(" ")) 
                else:
                    course_title = course_title + "".join("{:<12}".format(course_obj[course]))
                    if course_obj[course]!="--": 
                        if course_obj[course]>=49.5:
                            count_of_pass_results+=1
                        count_of_results+=1
            f.write("{:15} {:<15}\n".format(student.student_id, course_title))


        f.write("RESULTS SUMMARY\n")
        f.write("There are {} students and {} courses.\n".format(len(Results.list_of_students),len(Results.list_of_courses)))
        pass_rate= round((count_of_pass_results/count_of_results) * 100,2)
        f.write("The average pass rate is {}% \n".format(pass_rate))
    
    # function to display the results
    def __display_results(self):
        print("")
        print("RESULTS")
        print("".join(["{}".format("-") for i in range(75)]))
        course_title ="".join("{:<12}".format(value.course_id) for value in Results.list_of_courses)
        print("{:15} {:<12}".format("Student Ids", course_title))
        print("".join(["{}".format("-") for i in range(75)]))
        count_of_results=0
        count_of_pass_results=0

        for student in Results.list_of_students:
            course_obj = Results.results_of_students[student]
            course_title = ""
            for course in Results.list_of_courses:
                if course not in course_obj:
                    course_title = course_title + "".join("{:<12}".format(" ")) 
                else:
                    course_title = course_title + "".join("{:<12}".format(course_obj[course]))
                    if course_obj[course]!="--": 
                        if course_obj[course]>=49.5:
                            count_of_pass_results+=1
                        count_of_results+=1
            print("{:15} {:<15}".format(student.student_id, course_title))

        print("")
        print("RESULTS SUMMARY ")
        print("There are {} students and {} courses.".format(len(Results.list_of_students),len(Results.list_of_courses)))
        pass_rate= round((count_of_pass_results/count_of_results) * 100,2)
        print("The average pass rate is {}%".format(pass_rate))
    
    # function to call write_to_file functions
    def write_to_file(self):
        try:
            with open('reports.txt', 'r') as file:
                existing_content = file.read()

            self.__write_results()
            self.__write_to_reports()
            self.__write_student_info()
            
            with open('reports.txt', 'a') as file:
                file.write(existing_content)
        except:
            self.__write_results()
            self.__write_to_reports()
            self.__write_student_info()
    # function to call all the display functions
    def display(self):

        self.__display_results()
        self.__display_course_info()
        self.__display_student_info()
# main class to create a result object and call all the functions 
class Main:
    def __init__(self, course_details_path, student_details_path,results_details_path):
        __results=Results()
        __results.read_student(student_details_path)
        __results.read_course(course_details_path)
        __results.read_results(results_details_path)
        __results.display()
        __results.write_to_file()
if __name__ == "__main__":
    # Get the file names from the command line arguments
    if len(sys.argv)==3:
        print("Students file not found")
        print("[usage:] python myschool.py <result file> <course file> <student file>" )
        sys.exit(1)
    elif len(sys.argv)==2:
        print("Courses file not found")
        print("Students file not found")
        print("[usage:] python myschool.py <result file> <course file> <student file>" )
        sys.exit(1)
    elif len(sys.argv) != 4:
        print("Results file not found") 
        print("Courses file not found")
        print("Students file not found")
        
        print("[usage:] python myschool.py <result file> <course file> <student file>" )
        sys.exit(1)
    elif len(sys.argv)==4:
        results_details_path = sys.argv[1]
        course_details_path = sys.argv[2]
        student_details_path = sys.argv[3]
    
    Main(course_details_path,student_details_path,results_details_path)

    # Relection and Analysis:
   
'''The first step of any program is to read the problem statement ,
understand the requirements say inputs of the program and the expected output.
Then break the problem statement into smaller pices and try to solve it one by one.

After gathering all the requirements I started writing a code part by part .
Initailly i started with Part pass  which was just to read all the files(student,course,results) from command line and and print the results
Likewise I moved on to next part. Next part is about course adding more attributes reading and handling the error finally writinig it back to file 
and in the next part that is distiction we have to add attributes to student class and dop some computations and finally priont and write the results back .Hd level we have to sort the table accoring to average and wpga and handled all the errors regarding file input
To anlyze the l;ogic i have divided into parts and took exaples and cracked the logic.
I analyzed the logic and then break down into pieces and started writing code on each part which takes me a lot time to do . I used to do one part for atleast 2 days to make sure I have not missed any specification given in the assignment.
High distinction level is little complicated with reading the files in command line. I have researched how to read the file and mention the paths to the customer object and rthen founf=d out the logic and started writing the code and achieved all the specifications.
After all ,I wrote a class diagram w.r.t to the cl;asses and methods that i have defined in my implementation.
Once the program is fully built,I noted down all the values that needs to be tested and tested all the inputs and outputs 
aacordingly.Meanwhile commented the whole program and finally wrote this analysis. '''
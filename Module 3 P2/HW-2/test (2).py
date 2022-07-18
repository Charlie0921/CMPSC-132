course = cid.course
        Semester.addCourse(self, course)

##################################
else:
        course = catalog.courseOfferings[cid][0]
        self.semesters[semester] = Semester(sem_num).addCourse(catalog.courseOfferings[cid][0])
######################################
course = catalog.courseOfferings[cid][0]
        value = course.cid
##########################################3
Semester(0).courses[semester] = Semester(0).addCourse(catalog.courseOfferings[cid][0])
        self.semesters = Semester(0).courses
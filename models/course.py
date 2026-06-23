class Course:
    def __init__(self, course_id, course_name, trainer_name, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = int(capacity)

    def to_dict(self):
         return {
              'course_id': self.course_id,
              'course': self.course_name, 
              'trainer': self.trainer_name,
              'capacity': self.capacity
         }
    
    #Course management methods

    # add
    # view
    # delete
    # update a course
    # check if course exists
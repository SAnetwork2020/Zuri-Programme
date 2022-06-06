class Student:
    # [assignment] Skeleton class. Add your code here
##    change_name = ""
    change_age = 0
    def __init__(self,name,age,tracks,score):
            self.name = name
            self.age = change_age
            self.score = get_score
            self.tracks = add_track
            
##    def change_name(self):
##        self.name = name
####    def change_age(self):
####        self.age = age
##    def add_track(self):
##        self.tracks = tracks
##    def get_score(self):
##        return score
            
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
##Bob = Student("peter",18, ["UI","UX"], 70)
# Expected methods
##Bob.change_name("Peter")
Bob.change_age(34)
##Bob.add_track("UI/UX")
##Bob.get_score()
print(Bob.tracks)
print(Bob.score)

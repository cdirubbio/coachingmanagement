# GW Barbell Club Powerlifter Management System
from pyfiglet import Figlet
import sys
from Rpe_dictionary import dict1
inpit = input("Use Lifter Profiles? (Y/N): ")
# Dictionary is (Number of Reps)(RPE): So 1x10 @ RPE 6.5 = "106.5"

# RPE Calculator
#   Using dictionary to append reps to rpe
#     Then returning weight * key value of dict
def rpeCalc(weight, rep, rpe):
    if float(rpe) <6:
        return "RPE Too Low, Enter an RPE 6 or Higher"
    kglb = input("KG or LBS: ")
    keyv = str(rep) + str(rpe)
    value_find = dict1[keyv]
    if kglb.lower() == "lb" or kglb.lower() == "lbs" or kglb.lower() == "pounds":
        return f"{round(value_find * weight,2)} LBS \nor \n{round(value_find * weight /2.201, 2)} KG"
    else:
        return f"{round(value_find * weight,2)} KG\nor\n{round(value_find * weight *2.201,2)} LBS"

if inpit == "Y":
    custom_fig = Figlet(font="slant")
    print(custom_fig.renderText("Welcome Back"))

else:
    weight_inp = int(input("Enter Max Weight: "))
    rep_inp = input("Enter Number of Reps for set: ")
    rpe_inp = input("Enter Prescribed RPE: ")
    print(rpeCalc(weight_inp, rep_inp, rpe_inp))
    sys.exit()

class Lifter:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def get_info(self):
        return f"""
            Name: {self.name}
            Age: {self.age}
            Bodyweight: {self.weight}
            SBD Maxes: Total = {self.squat + self.bench +self.dead}
                Squat: {self.squat}: {round(self.squat/self.weight, 2)}x BW
                Bench: {self.bench}: {round(self.bench/self.weight, 2)}x BW
                Deadlift: {self.dead}: {round(self.dead/self.weight, 2)}x BW
        """
    #Squat
    def set_squat_max(self, squat, unit = "LBS"):
        self.squat = squat
        self.unit = unit
    def get_squat_max(self):
        return self.squat
    #Bench
    def set_bench_max(self, bench, unit = "LBS"):
        self.bench = bench
        self.unit = unit
    def get_bench_max(self):
        return self.bench
    #Deadlift
    def set_dead_max(self, dead, unit = "LBS"):
        self.dead = dead
        self.unit = unit
    def get_deadmax(self):
        return self.dead


# TESTTTTTTTS
lifter1 = Lifter("Christian DiRubbio", 19, 190)
lifter1.set_bench_max(315); lifter1.set_squat_max(500); lifter1.set_dead_max(450)

lifter2 = Lifter("Ankush Dwivedi", 19, 145)
lifter2.set_squat_max(245); lifter2.set_bench_max(225); lifter2.set_dead_max(285)

lifter3 = Lifter("Nick Tesar", 19, 260)
lifter3.set_squat_max(725); lifter3.set_bench_max(535); lifter3.set_dead_max(750)

lifter4 = Lifter("Nick Penders", 19, 165)
lifter4.set_squat_max(315); lifter4.set_bench_max(185); lifter4.set_dead_max(455)

lifter5 = Lifter("Tyler Richardson", 19, 169)
lifter5.set_squat_max(260); lifter5.set_bench_max(185); lifter5.set_dead_max(315)

lifter6 = Lifter("Grace Leonard", 19, 130)
lifter6.set_squat_max(215); lifter6.set_bench_max(105); lifter6.set_dead_max(250)

lifter7 = Lifter("John Smith", 22, 180)
lifter7.set_squat_max(400); lifter7.set_bench_max(300); lifter7.set_dead_max(530)

print(lifter1.get_info())
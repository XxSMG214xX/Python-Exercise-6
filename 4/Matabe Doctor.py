class Patient :
    def __init__(self,id,name,family_name,age,height,weight) :
        self.id = id
        self.name = name
        self.family_name = family_name
        self.age = age
        self.height = height
        self.weight  = weight
        self.visits = []
class Hospital :
    def __init__(self) :
        self.patients = {}
        self.schedule = {}
    def add_patient(self,id,name,family_name,age,height,weight) :
        if id in self.patients :
            return 'error: this ID already exists'
        if age < 0 : 
            return 'error: invalid age'
        if height < 0 : 
            return 'error: invalid height'
        if weight < 0 :
            return 'error: invalid weight'
        else:
            new_patient = Patient(id,name,family_name,age,height,weight)
            self.patients[id] = new_patient
            return 'patient added successfully'
    def display_patient(self,id) : 
        if id not in self.patients : 
            return 'error: invalid ID'
        else : 
            patient = self.patients[id]
            return f'patient name: {patient.name}\npatient family name: {patient.family_name}\npatient age: {patient.age}\npatient height: {patient.height}\npatient weight: {patient.weight}'
    def visit(self,id,beginning_time) :
        if id not in self.patients :
            return 'error: invalid id'
        if beginning_time < 9 or beginning_time > 18 or beginning_time % 1 != 0 :
            return 'error: invalid time'
        if beginning_time in self.schedule :
            return 'error: busy time'
        else :
            self.schedule[beginning_time] = id
            self.patients[id].visits.append(beginning_time)
            return 'visit added successfully!'
    def delete_patient(self,id) :
        if id not in self.patients :
            return 'error: invalid id'
        else :
            del self.patients[id]
            for time, patient_id in list(self.schedule.items()) :
                if patient_id == id :
                    del self.schedule[time]
            return 'patient deleted successfully!'
    def display_visits(self) :
        sorted_schedule = self.schedule.items()
        ans = "SCHEDULE:\n"
        for time , patient_id in sorted_schedule :
            patient = self.patients[patient_id]
            ans += f"{time:d}:00 {patient.name} {patient.family_name}\n"
        return ans.strip()
    

hospital = Hospital()
command = input()
command_strip = command.strip()
command_split = (command_strip.split())
while command_split[0] != "exit" or len(command_split) == 0: 
    if command_split[0] == "add" and command_split[1] == "patient" :
        answer = hospital.add_patient(int(command_split[2]), command_split[3], command_split[4], int(command_split[5]), int(command_split[6]), int(command_split[7]))
    elif command_split[0] == "add" and command_split[1] == "visit" :
        answer = hospital.visit(int(command_split[2]),int(command_split[3]))
    elif command_split[0] == "display" and command_split[1] == "visit":
        answer = hospital.display_visits()
    elif command_split[0] == "display" and command_split[1] == "patient":
        answer = hospital.display_patient(int(command_split[2]))
    elif command_split[0] == "delete" and command_split[1] == "patient" :
        answer = hospital.delete_patient(int(command_split[2]))
    elif command_split[0] == "exit":
        pass
    else :
        answer = "invalid command"
    print(answer)
    command = input()
    if command == '' :
        command = 'lsjdnfk'
    command_strip = command.strip()
    command_split = (command_strip.split())

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.appointments = []

class Appointment:
    def __init__(self, doctor, date_time):
        self.doctor = doctor
        self.date_time = date_time

class HealthcareAppointmentSystem:
    def __init__(self):
        self.doctors = []
        self.appointments = []

    def add_doctor(self, name, specialization):
        doctor = Doctor(name, specialization)
        self.doctors.append(doctor)

    def schedule_appointment(self, doctor_name, date_time):
        doctor = next((doc for doc in self.doctors if doc.name == doctor_name), None)
        if doctor:
            appointment = Appointment(doctor, date_time)
            doctor.appointments.append(appointment)
            self.appointments.append(appointment)
            print("Appointment scheduled successfully!")
        else:
            print("Doctor not found.")

    def view_appointments(self):
        for appointment in self.appointments:
            print(f"Doctor: {appointment.doctor.name}, Specialization: {appointment.doctor.specialization}, Date and Time: {appointment.date_time}")

    def cancel_appointment(self, doctor_name, date_time):
        appointment_to_cancel = next((appointment for appointment in self.appointments if appointment.doctor.name == doctor_name and appointment.date_time == date_time), None)
        if appointment_to_cancel:
            self.appointments.remove(appointment_to_cancel)
            appointment_to_cancel.doctor.appointments.remove(appointment_to_cancel)
            print("Appointment canceled successfully!")
        else:
            print("Appointment not found.")

def main():
    healthcare_system = HealthcareAppointmentSystem()

    while True:
        print("\nHealthcare Appointment Management System")
        print("1. Add Doctor")
        print("2. Schedule Appointment")
        print("3. View Appointments")
        print("4. Cancel Appointment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter doctor's name: ")
            specialization = input("Enter doctor's specialization: ")
            healthcare_system.add_doctor(name, specialization)

        elif choice == "2":
            doctor_name = input("Enter doctor's name: ")
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            healthcare_system.schedule_appointment(doctor_name, date_time)

        elif choice == "3":
            healthcare_system.view_appointments()

        elif choice == "4":
            doctor_name = input("Enter doctor's name: ")
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            healthcare_system.cancel_appointment(doctor_name, date_time)

        elif choice == "5":
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
      

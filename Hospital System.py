QUEUE_SIZE = 10
MIN_SPECIALIZATION = 1
MAX_SPECIALIZATION = 20

queue = {i: [] for i in range(MIN_SPECIALIZATION, MAX_SPECIALIZATION + 1)}

def add_patient_to_queue():
    try:
        spec = int(input("Enter specialization (1-20): "))
        if spec < MIN_SPECIALIZATION or spec > MAX_SPECIALIZATION:
            raise ValueError
    except ValueError:
        print("Invalid specialization. Please enter a number from 1 to 20.")
        return

    if len(queue[spec]) >= QUEUE_SIZE:
        print("Sorry, this specialization is full.")
        return

    name = input("Enter patient name: ")

    try:
        status = int(input("Enter patient status (0=normal, 1=urgent, 2=super urgent): "))
        if status < 0 or status > 2:
            raise ValueError
    except ValueError:
        print("Invalid status. Please enter 0 for normal, 1 for urgent, or 2 for super urgent.")
        return

    if status == 0:
        queue[spec].append((name, 0))
    elif status == 1:
        queue[spec].insert(0, (name, 1))
    elif status == 2:
        queue[spec].insert(0, (name, 2))

    print("Patient added successfully!")

def print_patient_queue():
    for spec, patients in queue.items():
        print(f"Specialization {spec}:")
        sorted_patients = sorted(patients, key=lambda x: x[1], reverse=True)
        for patient, status in sorted_patients:
            print(f"Patient: {patient}")

def get_next_patient_from_queue():
    try:
        spec = int(input("Enter specialization (1-20): "))
        if spec < MIN_SPECIALIZATION or spec > MAX_SPECIALIZATION:
            raise ValueError
    except ValueError:
        print("Invalid specialization. Please enter a number from 1 to 20.")
        return

    if len(queue[spec]) == 0:
        print("No patients in this specialization.")
        return

    patient = queue[spec][0]
    queue[spec] = queue[spec][1:]
    print("Next patient:", patient[0])

def remove_patient_from_queue():
    try:
        spec = int(input("Enter specialization (1-20): "))
        if spec < MIN_SPECIALIZATION or spec > MAX_SPECIALIZATION:
            raise ValueError
    except ValueError:
        print("Invalid specialization. Please enter a number from 1 to 20.")
        return

    name = input("Enter patient name: ")

    for patient in queue[spec]:
        if patient[0] == name:
            queue[spec].remove(patient)
            print(name, "has been removed from the queue.")
            return

    print("Patient not found.")

def main():
    while True:
        print("Program options:")
        print("1) Add new patient")
        print("2) Print all patients")
        print("3) Get next patient")
        print("4) Remove a leaving patient")
        print("5) End the program")

        try:
            choice = int(input("Enter your choice (from 1 to 5): "))
            if choice < 1 or choice > 5:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            add_patient_to_queue()

        elif choice == 2:
            print_patient_queue()

        elif choice == 3:
            get_next_patient_from_queue()

        elif choice == 4:
            remove_patient_from_queue()

        elif choice == 5:
            break

if __name__ == '__main__':
    main()

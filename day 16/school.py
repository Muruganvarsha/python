class School:
    def information(self, name, mail, mobile, address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address
        print("\n--- School Information ---")
        print("Name:", name)
        print("Mail:", mail)
        print("Mobile:", mobile)
        print("Address:", address)


class Staff(School):
    def staffinformation(self, name, mail, mobile, address, dept):
        super().information(name, mail, mobile, address)
        self.dept = dept
        print("Department:", dept)


class Student(School):
    def studentinformation(self, name, mail, mobile, address, dept):
        super().information(name, mail, mobile, address)
        self.dept = dept
        print("Department:", dept)


choice = input("Are you a Student or Staff? ").strip().lower()

if choice == "student":
    stu = Student()
    stu.studentinformation("Amit", "amit@gmail.com", "9876543210", "Pune", "Computer Science")
elif choice == "staff":
    stf = Staff()
    stf.staffinformation("Ravi", "ravi@gmail.com", "9123456789", "Mumbai", "Mathematics")
else:
    print("Invalid choice!")



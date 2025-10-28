class Personal:
    def information(self, name, mail, mobile, address):
        print("\n--- Personal Information ---")
        print("Name:", name)
        print("Mail:", mail)
        print("Mobile:", mobile)
        print("Address:", address)

class Educational(Personal):
    def information(self, marks, total, percentage):
        print("\n--- Educational Information ---")
        print("Marks of each subject:", marks)
        print("Total:", total)
        print("Percentage:", percentage, "%")

obj = Educational()

obj.information([80, 85, 90, 95, 88], 438, 87.6)
obj.information("John", "john@gmail.com", "9876543210", "Chennai")

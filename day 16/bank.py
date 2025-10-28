class Personal:
    def information(self, name, mail, mobile, address):
        self.name = name
        self.mail = mail
        self.mobile = mobile
        self.address = address
        print("\n--- Personal Information ---")
        print("Name:", name)
        print("Mail:", mail)
        print("Mobile:", mobile)
        print("Address:", address)


class Educational(Personal):
    def information(self, marks, total, percentage):
        self.marks = marks
        self.total = total
        self.percentage = percentage
        print("\n--- Educational Information ---")
        print("Marks of each subject:", marks)
        print("Total:", total)
        print("Percentage:", percentage, "%")


class Bank(Educational):
    def information(self, acc_num, branch_name, bank_name, ifsc_code, balance):
        self.acc_num = acc_num
        self.branch_name = branch_name
        self.bank_name = bank_name
        self.ifsc_code = ifsc_code
        self.balance = balance
        print("\n--- Bank Information ---")
        print("Account Number:", acc_num)
        print("Branch Name:", branch_name)
        print("Bank Name:", bank_name)
        print("IFSC Code:", ifsc_code)
        print("Available Balance:", balance)


obj = Bank()

obj.information("1234567890", "Main Branch", "State Bank", "SBIN0001234", 25000)
obj.information([85, 90, 88, 92, 80], 435, 87)
obj.information("John", "john@gmail.com", "9876543210", "Delhi")





totals_mark=int(input("enter the total mark:"))
appititude_mark=int(input("enter the appititude marks:"))
gd_mark=int(input("enter the gd mark:"))
if 390<= total_mark <=400:
    salarry=3000
    print("Eligible for job salary:",salary)
elif 370<= total_mark <=400 and appititude_mark>=85:
    salary=28000
elif 370<=total_mark <=400 and gd_mark>=90:
    salary=25000
    print("eligible for a job salary:",salary)
else:
    print("not eligible for the job")
    
 


def problem2():
    count_error = 0
    with open("regression.log","r") as f1, open("summary.log","w") as f2:
        f2.write(f"Testname\t\tStatus\tErrors\n------------------------------------------")
        for line in f1:  
            if "Running" in line:
                f2.write(f"\t{count_error}")
                count_error = 0
                print(line.split()[2])
                f2.write(f"\n{line.split()[2]}")
            if "Status" in line:
                f2.write(f"\t{line.split()[1]}")
            if "Error" in line:
                print(line.split()[1])
                count_error +=1 
            
        f2.write(f"\t{count_error}\n")
            
            
if __name__ == '__main__':
    problem2()
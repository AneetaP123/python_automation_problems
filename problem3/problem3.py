
def problem3():
    with open("test.log") as f:
        for line in f:
            if "UVM_ERROR" in line:
                print(str(int(line.split()[2].split("n")[0])/1000)+ "us")
                break
    count_error = 0
    count_fatal = 0
    count_warning = 0
    count_info = 0
    with open("test.log","r") as f1:
        for line in f1:
            if "UVM_ERROR" in line:
                count_error +=1
            if "UVM_FATAL" in line:
                count_fatal +=1
            if "UVM_WARNING" in line:
                count_warning += 1
            if "UVM_INFO" in line:
                count_info += 1
    with open("summary.log","w") as f2:
        f2.write("Summary\n-----------------------\n")
        f2.write(f"UVM_ERROR : \t{count_error}\n")
        f2.write(f"UVM_FATAL : \t{count_fatal}\n")
        f2.write(f"UVM_WARNING : \t{count_warning}\n")
        f2.write(f"UVM_INFO : \t{count_info}\n")

if __name__ == '__main__':
    problem3()

                

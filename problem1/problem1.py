


def problem1():
    count_error = 0
    count_fatal = 0
    count_warning = 0
    with open("sample.log","r") as f, open("error_summary.log", "w") as f1:
        for line in f:
            if "UVM_ERROR @" in line:
                f1.write(line)
                count_error += 1
            if "UVM_FATAL @" in line:
                f1.write(line)
                count_fatal += 1
            if "UVM_WARNING @" in line:
                f1.write(line)
                count_warning += 1
        f1.write("summary\n")
        f1.write(f"ERROR {count_error}\n")
        f1.write(f"FATAL {count_fatal}\n")
        f1.write(f"WARNING {count_warning}\n")
if __name__ == '__main__':
    problem1()
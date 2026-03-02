Problem:
Write a Python script that:

Reads a large UVM simulation log file

Extracts lines containing:

UVM_ERROR

UVM_FATAL

Writes them into error_summary.log

Prints total count of each

👉 Add enhancement: Also extract the test name from UVM_INFO @ 0: reporter [RNTST] Running test <test_name>
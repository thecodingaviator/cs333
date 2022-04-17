CS333 - Project 7 - README
Parth Parth
04/17/2022

File Structure:
├── Project6
│   ├── README.txt
│   ├── linkedlist.h
│   ├── python
│   │   ├── input.txt
│   │   ├── output.txt
│   │   ├── output1.txt
│   │   ├── task1.py
│   │   ├── task2.py
│   │   ├── task2a
│   │   ├── task3.py
│   │   ├── test.txt
│   │   └── testerr.txt
│   ├── r
│   │   ├── extension_2.R
│   │   ├── word_counter.R
│   ├── task2a.c
│   ├── task2b.c
│   ├── task2c.c
│   ├── test.txt
│   ├── wordCount.c
│   ├── wordCounter.c
│   └── yourLinkedList.c

Config:
Ubuntu 20.04.3 LTS using WSL 2 on Windows 11 - gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1) 

Tasks:

C:

    Task 1:
        
        a.
        
            Compile:
            gcc -o task -pg task.c

            Run:
            ./task

            Analyse:
            gprof task gmon.out > filename.txt

            To time the code for this task, I have used gprof. (Extension 1)

            short: It took 102ms to allocate 100,000,000 shorts. Giving an average
            of 1.02ns per short.
            int: It took 183ms to allocate 100,000,000 ints. Giving an average
            of 1.83ns per int.
            long: It took 204ms to allocate 100,000,000 longs. Giving an average
            of 2.04ns per long.

            Quickly graphing this, it is seen that this is a logarithmic increase 
            in time.

        b.

            Compile:
            gcc -o task -pg task.c

            Run:
            ./task

            To time the code for this task, I have measured time by counting CPU clocks
            and dividing by the number of CPU clocks per second.

            short:
            Time taken for call 1: 7.227651
            Time taken for call 2: 7.279815
            Time taken for call 3: 7.329810
            Time taken for call 4: 7.279838
            Time taken for call 5: 7.389833
            Time taken for call 6: 8.119775
            Time taken for call 7: 8.079803
            Time taken for call 8: 7.999803
            Time taken for call 9: 7.969735
            Time taken for call 10: 7.959787

            int:
            Time taken for call 1: 7.965848
            Time taken for call 2: 8.219873
            Time taken for call 3: 8.179885
            Time taken for call 4: 8.209797
            Time taken for call 5: 9.209830
            Time taken for call 6: 8.919871
            Time taken for call 7: 9.099992
            Time taken for call 8: 9.020000
            Time taken for call 9: 9.059998
            Time taken for call 10: 8.360000

            long:
            Time taken for call 1: 7.290786
            Time taken for call 2: 7.360000
            Time taken for call 3: 7.309995
            Time taken for call 4: 7.270000
            Time taken for call 5: 7.949996
            Time taken for call 6: 8.299999
            Time taken for call 7: 8.259991
            Time taken for call 8: 8.189999
            Time taken for call 9: 8.339994
            Time taken for call 10: 8.230000

        
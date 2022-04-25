CS333 - Project 7 - README
Parth Parth
04/17/2022

File Structure:


Config:
Ubuntu 20.04.3 LTS using WSL 2 on Windows 11 - gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1) 

Tasks:

C:

    Task 1:
        
        a.
        
            Compile:
            gcc -o task task.C

            Run:
            ./task

            Output and analysis:

            All arrays have been allocated 100,000 times so as to get
            a good, non-zero estimate of time. To time the code for this
            task, I have measured time by counting CPU clocks and
            dividing by the number of CPU clocks per second.

            small: Array of 10 ints.

                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.004500
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.004068
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.003801
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.004250
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.004106

                Dropping the smallest and highest time and averaging them,
                we get: 0.004141s for 100000 arrays.

            medium: Array of 1000 ints.

                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.196502
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.136970
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.120278
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.188968
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.152734

                Dropping the smallest and highest time and averaging them,
                we get: 0.159557s for 100000 arrays.

            large: Array of 100,000 ints.

                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.226599
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.168613
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.312020
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.154722
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call: 0.254957

                Dropping the smallest and highest time and averaging them,
                we get: 0.216723s for 100000 arrays.

            It can be thus concluded that the bigger the chunk of memory, 
            the longer it takes to allocate memory for it

            Extension 1:

            Compile:
            gcc -o task -pg task.c

            Run:
            ./task

            Analyse:
            gprof task gmon.out > filename.txt

            To time the code for this task, I have used gprof.
            However, gprof was giving me 0 time for all calls, so the code for this is in the profiler folder.

        b.

            Compile:
            gcc -o task task.c

            Run:
            ./task

            Output and analysis:
            To time the code for this task, I have measured time by counting CPU clocks
            and dividing by the number of CPU clocks per second.

            

            
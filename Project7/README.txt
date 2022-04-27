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

            medium: Array of 1,000 ints.

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
            the longer it takes to allocate memory for it. This is because it just
            takes longer for C to allocate larger chunks of memory/mark larger chunks
            as allocated.

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

            small: Array of 10 ints.
                Time taken for call 1: 0.001601
                Time taken for call 2: 0.001719
                Time taken for call 3: 0.001405
                Time taken for call 4: 0.001342
                Time taken for call 5: 0.001140
                Time taken for call 6: 0.001383
                Time taken for call 7: 0.001605
                Time taken for call 8: 0.001539
                Time taken for call 9: 0.001651
                Time taken for call 10: 0.001492

            medium: Array of 1,000 ints.
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call 1: 0.003138
                Time taken for call 2: 0.002975
                Time taken for call 3: 0.002983
                Time taken for call 4: 0.003115
                Time taken for call 5: 0.004581
                Time taken for call 6: 0.006730
                Time taken for call 7: 0.007251
                Time taken for call 8: 0.005332
                Time taken for call 9: 0.004301
                Time taken for call 10: 0.004970

            large: Array of 100,000 ints.
                parth@DESKTOP-1VEVFJK:~/cs333/Project7$ ./task
                Time taken for call 1: 0.002913
                Time taken for call 2: 0.002531
                Time taken for call 3: 0.004375
                Time taken for call 4: 0.007323
                Time taken for call 5: 0.006507
                Time taken for call 6: 0.005803
                Time taken for call 7: 0.007814
                Time taken for call 8: 0.006167
                Time taken for call 9: 0.006902
                Time taken for call 10: 0.005441

            For the small size, the times are almost the same. however, for the
            other two sizes, times go up to 1.5x for medium and 2x for large. I
            talked to Stephanie about it and we do not have any idea of what's going
            on.

            When comparing sizes, it takes more time as the sizes increase.
            
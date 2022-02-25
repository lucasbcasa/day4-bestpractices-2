# Exercises for Day 4
Cython, MPI parallelization, plotting with matplotlib, testing and documentation of code

## 2. MPI parallelization

#### a. Write a simple MPI script ```mpi_ranks.py``` that prints the rank of the different processes when running 
```
mpirun python mpi_ranks.py
```

ANS: I have written the script and saved it under ```mpi_ranks.py```. However, I have to execute it with ```mpiexec -n # python mpi_ranks.py```.

#### b. Write a small script ```mpi_sum.py``` which calculates the sum over all ranks and prints the result from the process with rank 0.
Hint: Have a look at the tutorials from the mpi4py documentation page: [https://mpi4py.scipy.org/docs/usrman/tutorial.html](https://mpi4py.scipy.org/docs/usrman/tutorial.html)

ANS: I have implemented a solution that sums all the ranks, prints it from the root and compares with the expected answer $(N x (N-1)/2)$. For execution convenience I also made a bash script that can be run with ```./run_mpi.sh N```, with N the number of processes.
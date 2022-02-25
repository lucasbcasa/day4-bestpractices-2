#mpi_sum.py

"""
Given N processes, calculates the sum of all the ranks (from 0 to N-1)
Result should be ((N) x (N-1)) / 2
"""
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Get the number of steps necessary
N = 2**((size-1).bit_length())

partial = rank

# Keep track of the last active rank (so that the process doesn't hang)
last = False
if rank == (size-1):
    last = True

# Loop over cycles
for c in range(N):
    # If the rank is such that the process should pass a result forward, do that
    if (rank/(2**c) + 1)%2==0:
        # Destination should be 2**c ranks below it
        dest = rank - 2**c
        comm.send((partial, last), dest=dest)
    # If the rank is such that the process should receive a result from another, do that
    if ((rank/(2**c))%2==0) & (not last):
        # Source should be 2**c ranks above it
        source = rank + 2**c
        # Process might become the last one
        (value, last) = comm.recv(source=source)
        partial += value

if rank==0:
    print("Process {} calculated a final sum of {}".format(rank, partial))
    print("Expected answer: ", size * (size-1) // 2)
    if size * (size-1) / 2 == partial: print("Yay!")
    else: print("Nay!")
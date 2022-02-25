#!/bin/bash

echo "Running mpi_sum.py with $1 processes."

mpiexec -n $1 python mpi_sum.py
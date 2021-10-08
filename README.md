# SCA4SD
[Structural Control Analysis of System Dynamics Models]

Python scripts for conducting Structural Control Analysis (SCA) on System Dynamics Models

# Info

Author: Tim

Email: tianyi.li@cuhk.edu.hk

Version history: 20211008 - v1.0.2 submission

Current version: 1.0.2

Reference: Li, T. & Oliva, R. (2021), Structural Control Analysis of System Dynamics Models.

# Usage

--> Input system equations matrix in input_file.py

--> Conduct SCA analysis: python3 SCA_SD.py

--> Collect output files from /output

# Output file

Matrix_A.csv --> 0-1 adjacency matrix of the system

Matrix_R.csv --> 0-1 reachability matrix of the system

PorC.csv --> overall PorC value for each variable 

Control_matrix.csv --> control input (1)/parameter (-1)/inaccessible (0) identification for each leaf variable toward each stock variable

Dilation_record.csv --> identifaction of dilation (1)/no dilation (0) for each control input, not applicable (-1) to each parameter






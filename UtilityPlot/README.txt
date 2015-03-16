Tom Diehl 1-16-15


This program takes in 4 csv files with 3 columns formatted:

"mm-dd-yy hr:min:sec , data1 , data2"

It then plots column 1 vs 2 or 1 vs 3 in sublpots with and allows
the ability to interact with the plots using zoom and pan. The 
original purpose was to plot bandwitdh and latency, but with
changes to axis titles, it could be easily repurposed.  The intial 
configuration is to read in 4 files and output 4 subplots. 

*Note this program requires the Matplotlib library and all its
dependencies.  


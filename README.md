# Tele-steth
A project for tele-stethoscope
## The Project is divided into Four parts:
* Signal Processing 

  This part is done by the program <b>'preprocess.py'</b>. The preprocess program has a function 'custum_filter' which does the preprocessing. 
  The program can be run and tested independently. The signal is completely recorded first and then processed.  
  
* Signal Transmission

  This program is run by <b>'patient.py'</b>. The program imports the 'custum_filter' function from the 'preprocess.py' to do processing of the individual chunks before sending it to the server. 
  
* Server
  
  The program to be run at the server end (<b>server.py</b>).
  
 * Doctor
  
    This part is done by '<b>doctor.py</b>'. 

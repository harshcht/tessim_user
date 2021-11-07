This is a demo release for tessim embedded simulation software.
Tessim is an in development software for design and simulation of embedded and control systems. The idea behind tessim is for the user to be able to emulate exact hardware details that go into an embedded system. This includes parameters like ADC precision, delay introduced by SPI and other serial chennels (in terms of transmitting message from one part to another), pwm counters etc. Along with models of physical elements like motors, actuators and circuit elements (like the LC component of a buck converter).
#install instructions : 

1. first clone the git repository or download as a zp file from github : https://github.com/harshcht/tessim_user
2. go to inside folder tessim_user
3. check the path using pwd
4. Make an environment variable of this path with the name "TESSIM_PATH"
   eg : TESSIM_PATH="/home/user/abcd/tessim_user
5. export this path variable :  export TESSIM_PATH
6. start by running any pyton script inside test_scripts folder

for any queries and questions write a mail to : chittoraharsh98@gmail.com
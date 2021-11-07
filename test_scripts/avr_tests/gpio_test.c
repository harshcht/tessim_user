#define F_CPU 1000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>

int main(){
    DDRB = 0x00;
    return 0;
}
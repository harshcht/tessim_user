#define F_CPU 1000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>

void main(){
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    TCCR1B = 1 << WGM12 | 1 << CS10;
     TWAR = 0x81;
    TWCR = 1 << TWEN | 1 << TWEA;
    while(1){
        if(TWSR == 0x90){
            OCR1BL = TWDR;
        }
    }
}
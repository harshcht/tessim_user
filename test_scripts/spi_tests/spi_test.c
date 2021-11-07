#define F_CPU 1000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>


void main(){
    uint8_t x;
    DDRB = 1 << PB3 |1 << PB6;
    SPCR = 1 << SPE;
    //SPDR = 0x8F;
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    TCCR1B = 1 << WGM12 | 1 << CS10;
    while(1){
            while(!(SPSR & (1 << SPIF)));
            OCR1BL=SPDR;
    }
    //SPDR = 0xf8;

}
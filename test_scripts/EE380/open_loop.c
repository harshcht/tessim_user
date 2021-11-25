#define F_CPU 10000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>
#define PI 3.14

int main(){        
    TCCR3B = 1 << CS30 | 1 << CS31 | 1 << CS32;
    DDRB = 0xFE;
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    TCCR1B = 1 << WGM12 | 1 << CS10;
    int d;
    float u = 3.03;
    d = (u/20) * 0x3FF;
    OCR1B = d;

    return 0;
}
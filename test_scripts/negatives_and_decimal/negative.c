#define F_CPU 1000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>

int main(){
    //float a  = 0.5;
    //float b = 0.5;
    //DDRB = 0xFE;
    //TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    //TCCR1B = 1 << WGM12 | 1 << CS10;
    //OCR1BL = 0.3 * 0x8F;
    
    ADCSRA = 1 << ADEN | 1 << ADATE | 1<< ADSC;
    //ADMUX = 1 << ADLAR;
    DDRB = 0xFF;
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    TCCR1B = 1 << WGM12 | 1 << CS10;
    while(1){
        OCR1BL = ADCL / 3;
        OCR1BH = ADCH / 3;
    }

    return 0;
}
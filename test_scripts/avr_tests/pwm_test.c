#define F_CPU 1000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>

int main(){
    //TCCR1A = 1 << COM1B0;
    //TCCR1B = 1 << WGM12 | 1 << CS10;
    //TCCR3B |= 1 << WGM32 | 1 << CS30 |  1<< CS31 | 1 << CS32;
     //TCCR3B |= 1 << WGM32 | 1 << CS30 |  1<< CS31 | 1 << CS32;
    //OCR1AL = 0x0F;
    //OCR3BL = 0x0F;
    //OCR1BL = 0x04;
    //OCR1AH = 0x00;
    //ADCSRA = 1 << ADEN | 1 << ADATE | 1<< ADSC;
    //ADMUX = 1 << ADLAR;
    DDRB = 0xFE;
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    TCCR1B = 1 << WGM12 | 1 << CS10;
    uint16_t ref = 0x2CC;
    while(1){
        if(PINB & 1 << PB0){
            OCR1BL = 0x8F; //pwm with duty cycle 0x8f/0x3ffDDRB = 0xFE;
        }
        else{
            OCR1BL = 0x01; //motor should stop if button is not pressed
        }
    }
    return 0;
}
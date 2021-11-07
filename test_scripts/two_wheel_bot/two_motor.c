#define F_CPU 1000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>

int main(){
    
    DDRB = 0xF0;
    DDRE = 0xFF;
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11 | 1 << COM1A1;
    TCCR1B = 1 << WGM12 | 1 << CS10;
    TCCR3A = 1 << COM3B1 | 1<< WGM30 | 1 << WGM31 | 1 << COM3A1;
    TCCR3B = 1 << WGM32 | 1 << CS30;
    while(1){
        if(PINB & 1 << PB0){//move forward
            OCR1BL = 0x8F;
            OCR3BL = 0x8F;
            OCR3AL = 0x00;
            OCR1AL = 0x00;
        }
        else if(PINB & 1 << PB1){//move in reverse
            OCR3BL = 0x00;
            OCR3AL = 0x8F;
            OCR1BL = 0x00;
            OCR1AL = 0x8F;
        }
        else if(PINB & 1 << PB2){//move left
            OCR3BL = 0x8F;
            OCR3AL = 0x00;
            OCR1BL = 0x00; 
            OCR1AL = 0x8F;
        }
        else if(PINB & 1 << PB3){//move right
            OCR3BL = 0x00;
            OCR3AL = 0x8F;
            OCR1BL = 0x8F;
            OCR1AL = 0x00;
        }
        else{ //stop in any other scenario
            OCR3BL = 0x00;
            OCR3AL = 0x00;
            OCR1BL = 0x00;
            OCR1AL = 0x00;
        }
    }
    return 0;
}
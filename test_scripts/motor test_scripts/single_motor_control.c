#define F_CPU 1000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>


int main(){
    DDRD = 0xFF; //PWM out
    DDRB = 0x00; //input port

    TCCR0A = 0x83; //fast PWM mode for counter B
    TCCR0B = 0x02; // OC0B is disconnected
    while(1){
        if(PINB & 1 << PB0){
            OCR0A = 0x8F; //pwm with duty cycle 0x8f/0xff
        }
        else{
            OCR0A = 0x00; //motor should stop if button is not pressed
        }

    }
   
    return 0;
}
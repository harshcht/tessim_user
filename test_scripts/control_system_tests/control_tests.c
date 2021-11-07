#define F_CPU 50000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>

int main(){
    
    ADCSRA = 1 << ADEN | 1 << ADATE | 1 << ADSC;
    ADMUX =  1 << MUX4;
    DDRB = 0xFE;
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    TCCR1B = 1 << WGM12 | 1 << CS10;
    uint16_t d = 0, duty = 0, error = 0;
    uint16_t ref = 0x2CC;
    uint16_t div = 4;
    while(1){
        _delay_ms(2);
        d = ADCL | ADCH << 8;
        if(ref > d){
            error = (ref - d) / div;
            duty += error;
        }
        else{
            error = (d - ref) / div;
            duty -= error;
        }
        if(duty & 0x1000){
            duty = 0;
        }
        if(duty > 0x3FF){
            duty = 0x3FF;
        }
        
        OCR1B = duty;
    }
}
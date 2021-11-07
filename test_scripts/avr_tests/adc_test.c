#define F_CPU 50000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>

int main(){
    
    ADCSRA = 1 << ADEN | 1 << ADATE | 1<< ADSC;
    ADMUX =  1 << MUX4;
    static uint16_t d = 0, duty = 0, di;
    static uint16_t ref = 0x2CC;
    uint32_t power , power_pre = 0, count = 0;
    int ref_step = -0x01;
    
    DDRB = 0xFF;
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    TCCR1B = 1 << WGM12 | 1 << CS10;
    
    TCCR3B = 1 << CS30 | 1 <<  CS32;
    OCR1B = 0x00;
    while(1){
        //ref = 0x2CC;
        ADCSRA = 1 << ADEN | 1 << ADPS2 | 1 << ADSC;
        ADMUX = 0x00;

        while(ADCSRA & (1 << ADSC));
        d = ADCL | (ADCH << 8);
        if(ref < d){
            OCR1B = ref - ref / 8;
        }
        else
            OCR1B = ref + ref / 32;
        /*
        if(TCNT3 == 0xFFFF){
            count+=1;
            if(count > 0x3FF){
                
                /*
                count = 0;
                ADCSRA = 1 << ADEN | 1 << ADPS2 | 1 << ADSC;
                ADMUX = 0x01;
                di = ADCL | (ADCH << 8);
                while(ADCSRA & (1 << ADSC));
                power = d * di;
                if(power_pre > power){
                    ref_step = -ref_step;
                }
                ref = ref + ref_step;
                power_pre = power;
            }

        }

       /*
        if(duty + ref/64 > d/64)
            duty = (duty + ref/64) - d/64;
        else
            duty = 1;
        
        if(duty > 0x3FF) duty = 0x3FF;
        OCR1B =  (duty > 0x3FF) ? 0x3FF : duty;*/

    }
    return 0;
}
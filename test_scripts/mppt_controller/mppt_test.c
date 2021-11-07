#define F_CPU 50000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>

int main(){
    
    ADCSRA = 1 << ADEN | 1 << ADATE | 1<< ADSC;
    ADMUX =  1 << MUX4;
    static uint16_t d = 0, duty = 0x2CC, di;
    static uint16_t ref = 0x2CC;
    //uint32_t power , power_pre = 0, count = 0;
    //int ref_step = -0x01;
    //ADCSRA = 1 << ADEN | 1 << ADPS2 | 1 << ADSC;
    //ADMUX = 0x01;
    //while(ADCSRA & (1 << ADSC));
    //ref = ADCL | (ADCH << 8);
    DDRB = 0xFF;
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    TCCR1B = 1 << WGM12 | 1 << CS10;
    
    //TCCR3B = 1 << CS30 | 1 <<  CS32;
    OCR1B = 0x00;
    while(1){
        ADCSRA = 1 << ADEN | 1 << ADPS2 | 1 << ADSC;
        ADMUX = 0x00;
        while(ADCSRA & (1 << ADSC));
        d = ADCL | (ADCH << 8);
        if(ref < d){
            OCR1B = ref - ref / 8;
        }
        else
            OCR1B = ref + ref / 8;
        /*
        ADCSRA = 1 << ADEN | 1 << ADPS2 | 1 << ADSC;
        ADMUX = 0x00;

        while(ADCSRA & (1 << ADSC));
        d = ADCL | (ADCH << 8);
        if( ref < d)
            duty = 1;
        else
            duty = (duty + ref) - d;
        
        if(duty > 0x3FF) duty = 0x3FF;
        OCR1B =  (duty > 0x3FF) ? 0x3FF : duty;*/
        /*
        ADCSRA = 1 << ADEN | 1 << ADPS2 | 1 << ADSC;
        ADMUX = 0x01;
        while(ADCSRA & (1 << ADSC));
        ref = ADCL | (ADCH << 8);*/
        

        /*
        if(TCNT3 == 0xFFFF){
            count+=1;
            if(count > 0x3FF){
                
                
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

        }*/
        
        /*
        ADCSRA = 1 << ADEN | 1 << ADPS2 | 1 << ADSC;
        ADMUX = 0x00;

        while(ADCSRA & (1 << ADSC));
        d = ADCL | (ADCH << 8);
        if( ref < d)
            duty = 1;
        else
            duty = (duty + ref) - d;
        
        if(duty > 0x3FF) duty = 0x3FF;
        OCR1B =  (duty > 0x3FF) ? 0x3FF : duty;*/
       

    }
    return 0;
}
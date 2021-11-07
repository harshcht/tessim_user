#define F_CPU 1000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>


void main(){
    ADCSRA = 1 << ADEN | 1 << ADATE | 1<< ADSC;
    uint8_t x ;
    TWDR = 0x00;
    while(1){
        x = ((ADCH & 0x03) << 6) | (ADCL >> 2);
        TWCR = 1 << TWINT | 1 << TWEN | 1 << TWSTA;
        while(!(TWCR & (1 << TWINT)));
        TWDR = 0x00;//general call address
        TWCR = 1 << TWINT | 1 << TWEN;
        while(!(TWCR & (1 << TWINT)));//wait till gen call is given
        //TWDR = ((ADCH & 0x03) << 6) | (ADCL >> 2);//transfer some data
        TWDR =x;
        TWCR = 1 << TWINT | 1 << TWEN;
        while(!(TWCR & (1 << TWINT)));
        TWCR = 1 << TWINT | 1 << TWEN | 1 << TWSTO;
        while(!(TWCR & (1 << TWSTO)));
    }
}
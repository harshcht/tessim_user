#define F_CPU 1000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>


void main(){
    DDRE = 1 << PE2;
    UBRR0L = 0x01;
    UBRR0H = 0x00;
    UCSR0C = 1 << UCSZ00 | 1 << UCSZ01;
    UCSR0B = 1 << TXEN0 | 1 << RXEN0 | 1 << UCSZ02;
    UDR0 = 0x8F;
}
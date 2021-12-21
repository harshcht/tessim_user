#define F_CPU 10000000UL

#include <xc.h>
#include <avr/io.h>
#include <util/delay.h>
#define PI 3.14
//int getPulse();
//int updateDuty();
int main(){
    TCCR3B = 1 << CS30 | 1 << CS31 | 1 << CS32;
    DDRB = 0xFE;
    TCCR1A = 1 << COM1B1 | 1<< WGM10 | 1 << WGM11;
    TCCR1B = 1 << WGM12 | 1 << CS10;
    int ref = 0x14, d = 0, cnt = 0, int_gain = 1, Ts = 10, N = 500, Vs = 20, d_f;
    float ref_speed = 50, speed = 0, gain = 0.5, gain_1 = 1, ref_f, u = 0;
    ref_f = N * Ts * ref_speed / (2 * PI * 1000);
    ref = ((ref_f - floor(ref_f)) > 0.5) ? ceil(ref_f) : floor(ref_f);
    //ref += 1;
    gain_1 = gain * 0x3FF * 2 * PI / (N * Vs);
    //gain_1 = 0.32;
    //ref = 0x14;
    while(1){
        
        cnt = TCNT3;
        TCNT3 = 0;//the rotary encoder is connoected to the third counter
                //speed = cnt * (2pi) / (n * Ts)
       
        d += gain_1 * (ref-cnt);//integral controller
        //the duty cycle is given by : 
        //D = d / 0x3FF (10 bit timer goes to a max of 1023)

        if(d < 0){
            d=0;
        }
        if(d>0x3FF){
            d=0x3FF;
        }//max and min value of the counter compare register, going beyonf these might cause issues
        OCR1B = d;//OCR1B is the counter compare register
                //decides the pwm duty cycle for the pwm port 1
            //D = OCR1B / 0x3FF
        _delay_ms(Ts);
        
    }
    return 0;
}

/*

int
getPulse(){
    int cnt;
    cnt = TCNT3;
    TCNT3 = 0;
    return cnt;
}

int updateDuty(int duty, int ref, int cnt){
    return duty + 4*(ref - cnt);
}*/
/*
        speed = cnt * ref_speed / ref_f;  
        u += gain * (ref_speed - speed) * Ts / 1000;
        //u=u+0.2;
        
        if(u>20){
            u=20;
        }
        if(u < 0){
            u=0;
        }
        d = (u / 20) * 0x3FF;
        */
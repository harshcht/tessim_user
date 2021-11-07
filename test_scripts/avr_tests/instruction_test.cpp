#include <stdio.h>
#include "avr_general.hpp"

void assignSRAM(avr_mcu * mcu, uint16_t addr, uint8_t data){
    avr_cpu * cpu_avr = mcu->getCore();
    cpu_avr->SRAM[addr] = data;
}


int main(){
    Clock  * clk = new Clock(0.000001, 0.5, oscillator);
    avr_mcu * avr_test = new avr_mcu(atmega2560, NULL, clk);
    avr_cpu * avr_test_cpu = avr_test->getCore();
    uint16_t opcode;
    

    //TEST_ADC 
    printf("\ntesting ADC instruction");
    opcode =  0x1C00;
    for(int i = 0;i<32;i++){
        opcode =  0x1C00;//reinitialise the opcode to the core
        opcode |= i << 4;//d varying from 0 to 31
        action_ptr[getInstruct(&opcode)](&opcode, avr_test_cpu);
    }

    return 0;
}
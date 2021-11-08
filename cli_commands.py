import ctypes
from ctypes import c_char_p, c_double, c_void_p, cdll
import enum
import math
import os

tessim_path = os.environ['TESSIM_PATH']

tessim = cdll.LoadLibrary(tessim_path  + '/bin/libtessim.so')

parts = []
global_time_passed = 0
recorded_nodes = []
simulation_time = []
class architecture_family (enum.IntEnum) : 
    avr = 0
    arm = 1
    x86 = 2
    risc_v = 3
    pic = 4

    @classmethod
    def from_param(cls, obj):
        return int(obj)

class avr_mcu (enum.IntEnum) : 
    atmega328p = 0
    atmega2560 = 1

    @classmethod
    def from_param(cls, obj):
        return int(obj)

class counter_pwm_modes (enum.IntEnum) :
    up_only = 0
    up_down = 1
    down_only = 2

    @classmethod
    def from_param(cls, obj):
        return int(obj)

class counter_pwm_action (enum.IntEnum) :
    match_set_clear_top = 0
    match_set_clear_bottom = 1
    match_clear_set_top = 2
    match_clear_set_bottom = 3
    top_toggle = 4
    bottom_toggle = 5
    match_toggle = 6
    match_set = 7
    match_clear = 8
    top_set = 9
    top_clear = 10
    bottom_set = 11
    bottom_clear = 12

    @classmethod
    def from_param(cls, obj):
        return int(obj)

class debugger_type (enum.IntEnum) :
    master_spi = 0
    slave_spi = 1
    master_twi = 2
    slave_twi = 3
    master_usart = 4
    slave_usart = 5

    @classmethod
    def from_param(cls, obj):
        return int(obj)

class pin_state (enum.IntEnum) :
    pin_low = 0
    pin_high = 1

    @classmethod
    def from_param(cls, obj):
        return int(obj)

class clock_types (enum.IntEnum) :
    oscillator = 0
    external = 1
    dependant = 2

    @classmethod
    def from_param(cls, obj):
        return int(obj)

class twi_state(enum.IntEnum) :
    twi_recv_data = 0
    twi_send_data = 1
    twi_recv_ack = 2
    twi_send_ack = 3
    twi_send_nack = 4
    twi_send_start = 5
    twi_send_stop = 6
    twi_idle = 7

    @classmethod
    def from_param(cls, obj):
        return int(obj)

class data_direction(enum.IntEnum) :
    MSB_FIRST = 0
    LSB_FIRST = 1
    IDLE = 2


    @classmethod
    def from_param(cls, obj):
        return int(obj)

class clock_ticks(enum.IntEnum) :
    low_to_high = 0
    high_to_low = 1
    none  = 2

    @classmethod
    def from_param(cls, obj):
        return int(obj)    
    

class   usart_tx_state(enum.IntEnum) : 
    usart_tx_idle = 0
    usart_tx_start = 1
    usart_tx_data = 2
    usart_tx_stop = 3

    @classmethod
    def from_param(cls, obj):
        return int(obj)   

class t_parity(enum.IntEnum) :
    odd_parity = 0
    even_parity = 1
    none_parity = 2

    @classmethod
    def from_param(cls, obj):
        return int(obj)   
    


tessim.createMCU.argtypes = [architecture_family, ctypes.c_int, ctypes.c_char_p, ctypes.c_float]
tessim.createMCU.restype = ctypes.c_void_p
tessim.connectMCUNodes.argtypes = [ctypes.c_void_p, ctypes.c_void_p,architecture_family]
tessim.execMCU.argtypes = [architecture_family,ctypes.c_double,ctypes.c_void_p]
tessim.setCounterMode.argtypes = [ctypes.c_void_p, ctypes.c_int]
tessim.setCounterMatchAction.argtypes = [ctypes.c_void_p, counter_pwm_action, ctypes.c_int]
tessim.setCounterCompare.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_uint]
tessim.getCounterTop.argtypes = [ctypes.c_void_p]
tessim.createGenericMotorDriver.argtypes = [ctypes.c_double, ctypes.c_double]
tessim.createGenericMotorDriver.restype = ctypes.c_void_p
tessim.execMotorDriver.argtypes = [ctypes.c_void_p]
tessim.create_motor.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
tessim.motor_exec.argtypes = [ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double]
tessim.getMotorSpeed.restype = ctypes.c_double
tessim.setNodes.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
tessim.createNodes.argtypes = [ctypes.c_int]
tessim.createNodes.restype = ctypes.c_void_p
tessim.inToNode.argtypes = [ctypes.c_int, ctypes.c_double]
tessim.createCounter.argtypes = [ctypes.c_int, ctypes.c_int]
tessim.setCounterTopDefault.argtypes = [ctypes.c_void_p]
tessim.execCounter.argtypes = [ctypes.c_void_p, ctypes.c_double]
tessim.setCounterTop.argtypes = [ctypes.c_void_p, ctypes.c_uint]
tessim.getCounterTop.argtypes = [ctypes.c_void_p]
tessim.getCounterCount.argtypes = [ctypes.c_void_p]
tessim.getCounterCount.restype = ctypes.c_uint
tessim.getCounterTop.restype = ctypes.c_uint
tessim.setCounterClockFreq.argtypes = [ctypes.c_void_p, ctypes.c_double]
tessim.addTWIdebugger.argtypes = [ctypes.c_int, debugger_type, ctypes.c_void_p, ctypes.c_char_p]
tessim.addTWIdebugger.restype = ctypes.c_void_p
tessim.setTWIsda.argtypes = [ctypes.c_void_p, ctypes.c_uint]
tessim.TWIexec.argtypes = [ctypes.c_void_p, ctypes.c_double]
tessim.connectTWIline.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
tessim.putTWISlaveAddress.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
tessim.createClock.argtypes = [ctypes.c_double, ctypes.c_double, clock_types]
tessim.updateClock.argtypes = [ctypes.c_void_p, ctypes.c_double]
tessim.createClock.restype = ctypes.c_void_p
tessim.createTWILine.restype = ctypes.c_void_p
tessim.initTWILine.argtypes = [ctypes.c_void_p, ctypes.c_int]
tessim.execTWILine.argtypes = [ctypes.c_void_p]
tessim.getTWISDAPtr.argtypes = [ctypes.c_void_p]
tessim.getTWISDAPtr.restype = ctypes.c_void_p
tessim.setLineSDA.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int]
tessim.addSDAToLine.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
tessim.enableTWIAck.argtypes = [ctypes.c_void_p, ctypes.c_bool]
tessim.setStatusFlag.argtypes = [ctypes.c_void_p, ctypes.c_uint16]
tessim.getNodeVal.argtypes = [ctypes.c_int]
tessim.getNodeVal.restype = ctypes.c_double
tessim.getMCUTWILine.argtypes = [ctypes.c_void_p, architecture_family]
tessim.getMCUTWILine.restype = ctypes.c_void_p
tessim.getTWIMCUClock.argtypes = [ctypes.c_void_p,architecture_family]
tessim.getTWIMCUClock.restype = ctypes.c_void_p
tessim.setTwiLogFile.argtypes = [ctypes.c_void_p ,ctypes.c_char_p, architecture_family]
tessim.cpuLogFile.argtypes = [ctypes.c_void_p, architecture_family, ctypes.c_char_p]
tessim.enableGeneralTWICall.argtypes = [ctypes.c_void_p, ctypes.c_bool]
tessim.setMCUTWILine.argtypes = [ctypes.c_void_p, architecture_family, ctypes.c_void_p]
tessim.initMCUTWIDebuggerLogs.argtypes = [ctypes.c_void_p, architecture_family, ctypes.c_char_p]
tessim.setTWIMCUClock.argtypes = [ctypes.c_void_p, architecture_family, ctypes.c_void_p]
tessim.createSPIdebugger.argtypes = [ctypes.c_int, debugger_type, ctypes.c_void_p]
tessim.createSPIdebugger.restype = ctypes.c_void_p
tessim.executeSPIdbgr.argtypes = [ctypes.c_double, ctypes.c_double, pin_state, ctypes.c_void_p]
tessim.execSPINodes.argtypes = [ctypes.c_void_p, ctypes.c_double]
tessim.assignSPINodes.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]
tessim.setSPIOutputReg.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
tessim.setSPITicks.argtypes = [ctypes.c_void_p, clock_ticks, clock_ticks]
tessim.assignClockNode.argtypes = [ctypes.c_void_p,ctypes.c_int]
tessim.createIntegrator.argtypes = [ctypes.c_double, ctypes.c_int]
tessim.createIntegrator.restype = c_void_p
tessim.execIntegrator.argtypes = [ctypes.c_double, ctypes.c_void_p]
tessim.assignIntegratorOutput.argtypes = [ctypes.c_void_p, ctypes.c_int]
tessim.createAdder.argtypes = [ctypes.c_void_p, ctypes.c_void_p,ctypes.c_void_p]
tessim.setNegativeTerminals.argtypes = [ctypes.c_bool, ctypes.c_bool, ctypes.c_bool, ctypes.c_void_p]
tessim.createAdder.restype = ctypes.c_void_p
tessim.execAdder.argtypes = [ctypes.c_void_p, ctypes.c_double]
tessim.assignMotorSpeedNode.argtypes = [ctypes.c_void_p, ctypes.c_int]
tessim.createUSARTDbgr.argtypes = [ctypes.c_int, ctypes.c_void_p]
tessim.createUSARTDbgr.restype = ctypes.c_void_p
tessim.execUSARTdebugger.argtypes = [ctypes.c_double, ctypes.c_void_p]
tessim.setUSARTTicks.argtypes = [ctypes.c_void_p, clock_ticks, clock_ticks]
tessim.setUSARTsynch.argtypes = [ctypes.c_void_p, debugger_type]
tessim.assignUSARTNodes.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
tessim.enableUSARTTX_RX.argtypes = [ctypes.c_void_p, ctypes.c_bool, ctypes.c_bool]
tessim.setUSARTOutputBuff.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
tessim.setUSARTTxState.argtypes = [ctypes.c_void_p, usart_tx_state]
tessim.setUSARTParity.argtypes = [ctypes.c_void_p, t_parity]
tessim.setUSARTBits.argtypes = [ctypes.c_void_p, ctypes.c_int]
tessim.setUSARTSettings.argtypes = [ctypes.c_void_p, ctypes.c_int, t_parity, ctypes.c_int]
tessim.createRotaryEncoder.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double]
tessim.createRotaryEncoder.restype = ctypes.c_void_p
tessim.execEncoder.argtypes = [ctypes.c_double, ctypes.c_void_p]


def createNodes(num) :
    global recorded_nodes
    recorded_nodes.extend([] for i in range(num))
    return tessim.createNodes(num) 

def recordNodes() :
    global recorded_nodes
    records = []
    #with open(record,'w') as csvfile :
     #   csvwriter = csv.writer(csvfile) 
      #  for i in range(len(recorded_nodes)) :
       #     records.append(getNodeValue(i))
        
        #csvwriter.writerow(records)
    for i in range(len(recorded_nodes)):
        
        recorded_nodes[i].append(getNodeValue(i))
        #if recorded_nodes
    return


def execAll(time_div, time) :
    #print(len(parts))
    global global_time_passed
    global simulation_time
    t = global_time_passed
    num_record = 0
    while(t < time + global_time_passed) : 
        if(num_record % 50 == 0):
            recordNodes()
            simulation_time.append(t)
        for p in parts : 
            p.Exec(t)
            #print(mt.getSpeed())
        t  = t + time_div
        num_record += 1
    
    global_time_passed = time + global_time_passed

def putValue(node_num, value) : 
    tessim.inToNode(node_num, value)

def getNodeValue(node_num) :
    return tessim.getNodeVal(node_num)

def reset() :
    global parts

    for x in parts:
        del(x)

    parts  = []
    global global_time_passed
    global_time_passed = 0
    global simulation_time
    simulation_time = []



class mcu :
    mcu_obj = None
    mcu_family = 0
    mcu_part_num = 0
    def __init__(self, family, part_num, path, freq):
        self.mcu_obj = tessim.createMCU(family, part_num, path, freq)
        self.mcu_family = family
        self.mcu_part_num = part_num
        parts.append(self)

    def Exec(self, time) :
        tessim.execMCU(self.mcu_family, time, self.mcu_obj)

    def connectNodes(self, nodes):
        tessim.connectMCUNodes(self.mcu_obj,nodes, self.mcu_family)

    def getTWILine(self) :
        return tessim.getMCUTWILine(self.mcu_obj, self.mcu_family)

    def getTWIClock(self) :
        return tessim.getTWIMCUClock(self.mcu_obj, self.mcu_family)
    
    def setTwiLog(self, path) :
        tessim.setTwiLogFile(self.mcu_obj, path, self.mcu_family)

    def initCPULogFile(self, path) :
        tessim.cpuLogFile(self.mcu_obj, self.mcu_family, path)

    def setTWILine(self, line):
        tessim.setMCUTWILine(self.mcu_obj, self.mcu_family, line)

    def setTWIDebuggerLogs(self, path):
        tessim.initMCUTWIDebuggerLogs(self.mcu_obj, self.mcu_family, path)

    def setTWIClock(self, clk):
        tessim.setTWIMCUClock(self.mcu_obj, self.mcu_family, clk)

    def setSPILogs(self, path):
        tessim.setSPIDebuggerLogs(self.mcu_obj, self.mcu_family, path)
        

class dcMotor : 
    motor = 0
    speeds = []
    time = []
    torque = 0
    Vin = 0
    def __init__(self, kt, ke, r,  l,  jm, bm) :
        self.motor  = tessim.create_motor(kt, ke, r,  l,  jm, bm)
        self.speeds = []
        self.time = []
        parts.append(self)
    def execMotor(self, time_div, time) : 
        
        t  = 0
        while t < time : 
            tessim.motor_exec(self.motor, t, self.Vin, self.torque)
            t = t + time_div
            #print(t)
            self.speeds.append(self.getSpeed())
            self.time.append(t)
    def Exec(self, time) : 
        tessim.motor_exec(self.motor, time, self.Vin, self.torque)
        self.speeds.append(self.getSpeed())
        self.time.append(time)
    def getSpeed(self) :
        return tessim.getMotorSpeed(self.motor)

    def setNodes(self, nd1, nd2) :
        tessim.setNodes(self.motor, nd1, nd2) 

    def setSpeedNode(self, speed_node_num) :
        tessim.assignMotorSpeedNode(self.motor, speed_node_num)



class counter_pwm :
    counter = 0
    counter_obj = 0
    node_num = 0
    vcc = 5
    def __init__(self, n_bits, n_output, node_num):
        self.counter_obj = tessim.createCounter(n_bits, n_output)
        self.node_num = node_num
        parts.append(self)

    def setToptoDefault(self) :
        tessim.setCounterTopDefault(self.counter_obj)

    def Exec(self, time) :
        tessim.execCounter(self.counter_obj, time)
        putValue(self.node_num, self.vcc * self.getOutputBit(0))
        

    def getCounterCount(self) :
        return tessim.getCounterCount(self.counter_obj)

    def setMode(self, mode) : 
        tessim.setCounterMode(self.counter_obj, mode)
    
    def getOutputBit(self, num) :
        return tessim.getOutputBit(self.counter_obj, num)

    def setCounterAction(self, action, num) : 
        tessim.setCounterMatchAction(self.counter_obj, action, num)

    def setCounterCompare(self, num, val):
        tessim.setCounterCompare(self.counter_obj, num, val)

    def getCounterTop(self) :
        return tessim.getCounterTop(self.counter_obj)


    def setCounterClockFreq(self, freq):
        tessim.setCounterClockFreq(self.counter_obj, freq)

    def setPWMVcc(self, vcc) :
        self.vcc = vcc

class generic_motor_drivers :
    driver_obj = 0
    def __init__(self, on, off):
        self.driver_obj = tessim.createGenericMotorDriver(on, off)
        parts.append(self)

    def Exec(self,  t) : 
        tessim.execMotorDriver(self.driver_obj)

    def connectNodes(self, vcc, vin, vout, gnd) :
        tessim.connectDriverNodes(self.driver_obj, vcc, vin, vout, gnd)


class TWI_debugger :
    debugger_obj = None
    def __init__(self, n_bytes, type, clk, log_path):
        self.debugger_obj = tessim.addTWIdebugger(n_bytes, type, clk, log_path)
        parts.append(self)
    
    def setSDA(self, data) :
        tessim.setTWIsda(self.debugger_obj, data)

    def Exec(self, time):
        tessim.TWIexec(self.debugger_obj, time)

    def connectLine(self, line) :
        tessim.connectTWIline(self.debugger_obj, line)

    def putSlaveAddress(self, address, n):
        tessim.outTWISlaveAddress(self.debugger_obj, address, n)

    def setState(self, state):
        tessim.TWISetState(self.debugger_obj, state)

    def getSDAPtr(self) :
        return tessim.getTWISDAPtr(self.debugger_obj)

    def enableAck(self, enable) :
        tessim.enableTWIAck(self.debugger_obj, enable)

    def setStatusFlag(self, val) :
        tessim.setStatusFlag(self.debugger_obj, val)

    def enableGeneralCallAck(self, enable):
        tessim.enableGeneralTWICall(self.debugger_obj, enable)

class TWI_line :
    line_obj = None
    def __init__(self, n_devices) :
        self.line_obj = tessim.createTWILine()
        tessim.initTWILine(self.line_obj, n_devices)
        parts.append(self)

    def Exec(self, time) :
        tessim.execTWILine(self.line_obj)

    def setLineSDA(self, sda, index) :
        tessim.setLineSDA(self.line_obj, sda, index)

    def addSDAPtr(self, sda) :
        tessim.addSDAToLine(self.line_obj, sda)

   

class Clock :
    clock_obj = None

    def __init__(self, time_period, duty_cycle, type) :
        self.clock_obj = tessim.createClock(time_period, duty_cycle, type)
        parts.append(self)

    def updateClock(self, current_sim_time) :
        tessim.updateClock(self.clock_obj, current_sim_time)
    
    def Exec(self, time) :
        self.updateClock(time)

    def connectNode(self, node):
        tessim.assignClockNode(self.clock_obj, node)

    
class sine_source :
    freq = 0
    node_num = 0
    amplitude = 0
    offset  = 0
    def __init__(self, f,node, amp, off) :
        self.freq = f
        self.node_num = node
        self.amplitude = amp
        self.offset = off
        parts.append(self)

    def Exec(self, time) :
        putValue(self.node_num, self.offset + self.amplitude * math.sin(self.freq * time))


class SPI_debugger :
    debugger_obj = None
    mosi_node_num = 0
    miso_node_num = 0
    ss_node_num = 0
    dbgr_type = debugger_type.master_spi
    def __init__(self, n_bytes, type, clk):
        self.debugger_obj = tessim.createSPIdebugger(n_bytes, type, clk)
        self.dbgr_type = type
        parts.append(self)
    
    def Exec(self,time) :
        tessim.execSPINodes(self.debugger_obj, time)

    def connectNodes(self, miso, mosi, ss):
        tessim.assignSPINodes( miso, mosi, ss, self.debugger_obj)

    def getPinState(self) :
        if self.dbgr_type is debugger_type.master_spi :
            return getNodeValue(self.miso_node_num)

        elif self.dbgr_type is debugger_type.slave_spi :
            return getNodeValue(self.mosi_node_num)

    def setOutputReg(self, value) :
        tessim.setSPIOutputReg(self.debugger_obj, value)

    def setDirection(self, dir) :
        tessim.assignSPIDir(self.debugger_obj, dir)

    def setupTicks(self, sample, setup) :
        tessim.setSPITicks(self.debugger_obj, sample, setup)


class Integrator :
    gain = 1
    input_pte = None
    integrator_obj = None

    def __init__(self, gain, input) :
        self.integrator_obj = tessim.createIntegrator(gain, input)
        parts.append(self)
    
    def Exec(self, time) :
        tessim.execIntegrator(time, self.integrator_obj)

    def assignOutputNode(self, node) :
        tessim.assignIntegratorOutput(self.integrator_obj, node)

class Adder :
    adder_obj = None
    def __init__(self, in1, in2, out):
        self.adder_obj = tessim.createAdder(in1, in2, out)
        parts.append(self)

    def setNegative(self, in1, in2, out) :
        tessim.setNegativeTerminals(in1, in2, out, self.adder_obj)

    def Exec(self, time) :
        tessim.execAdder(self.adder_obj, time)

class uart_debugger :
    debugger_obj = None
    def __init__(self, n_bits, clk):
        self.debugger_obj = tessim.createUSARTDbgr(n_bits, clk)
        parts.append(self)

    def Exec(self, time) :
        tessim.execUSARTdebugger(time, self.debugger_obj)

    def setTicks(self, sample, setup):
        tessim.setUSARTTicks(self.debugger_obj, sample, setup)

    def setSynch(self, synch) :
        tessim.setUSARTsynch(self.debugger_obj, synch)

    def setType(self, type) :
        tessim.setUSARTType(self.debugger_obj, type)

    def connect(self, num_rx, num_tx) :
        tessim.assignUSARTNodes(self.debugger_obj, num_rx, num_tx)
    
    def enableTxRx(self, tx, rx) :
        tessim.enableUSARTTX_RX(self.debugger_obj, tx, rx)


    def setOutputBuff(self, data) :
        tessim.setUSARTOutputBuff(self.debugger_obj, data)

    def setState(self, state) :
        tessim.setUSARTTxState(self.debugger_obj, state)

    def setParity(self, parity) :
        tessim.setUSARTParity(self.debugger_obj, parity)

    def setBits(self, bits) :
        tessim.setUSARTBits(self.debugger_obj, bits)

    def txSettings(self, n_bits, parity, n_stop_bits) :
        tessim.setUSARTSettings(self.debugger_obj, n_bits, parity, n_stop_bits)


class encoder :
    encoder_obj = None
    def __init__(self, n, speed, a, b, frac, phase_dif):
        self.encoder_obj = tessim.createRotaryEncoder(n, speed, a, b, frac, phase_dif)
        parts.append(self)

    def Exec(self, time):
        tessim.execEncoder(time, self.encoder_obj)
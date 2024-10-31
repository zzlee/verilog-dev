from myhdl import *
from random import randrange

@block
def dffa(q, d, clk, rst):

    @always_seq(clk.posedge, reset=rst)
    def logic():
        if rst == 0:    # nRst ?  or use active high ?
            q.next = 0
        else:
            q.next = d

    return logic

@block
def test_dffa():

    q, d, clk = [Signal(bool(0)) for i in range(3)]
    rst = ResetSignal(val=1, active=0, isasync=True)

    dffa_inst = dffa(q, d, clk, rst)

    @always(delay(10))
    def clkgen():
        clk.next = not clk

    @always(clk.negedge)
    def stimulus():
        d.next = randrange(2)

    @instance
    def rstgen():
        yield delay(5)
        rst.next = 1
        while True:
            yield delay(randrange(500, 1000))
            rst.next = 0
            yield delay(randrange(80, 140))
            rst.next = 1

    return dffa_inst, clkgen, stimulus, rstgen


def simulate(timesteps):
    simInst = test_dffa() 
    simInst.config_sim(trace=True, tracebackup=False)
    simInst.run_sim(timesteps, quiet=0) 

simulate(2000)

def convert():
    q, d, clk = [Signal(bool(0)) for i in range(3)]
    rst = ResetSignal(val=1, active=0, isasync=True)
    convInst = dffa(q, d, clk, rst)
    convInst.convert(hdl='Verilog')
    convInst.convert(hdl='VHDL')

convert()

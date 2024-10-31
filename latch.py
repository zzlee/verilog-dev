from myhdl import *
from random import randrange

@block 
def latch(q, d, g):

	@always_comb
	def logic():
		if g == 1:
			q.next = d

	return logic

@block 
def test_latch():

	q, d, g = [Signal(bool(0)) for i in range(3)]

	latch_inst = latch(q, d, g) 

	@always(delay(7))
	def dgen():
		d.next = randrange(2)

	@always(delay(41))
	def ggen():
		g.next = randrange(2)

	return latch_inst, dgen, ggen

def simulate(timesteps):
	simInst = test_latch() 
	simInst.config_sim(trace=True)
	simInst.run_sim(timesteps, quiet=0) 

simulate(2000)

def convert():
	q, d, g = [Signal(bool(0)) for i in range(3)]
	convInst = latch(q, d, g)
	convInst.convert(hdl='Verilog')
	convInst.convert(hdl='VHDL')

convert()

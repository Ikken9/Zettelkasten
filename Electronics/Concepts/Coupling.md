# Coupling

Is the transfer of electrical energy from one circuit to another, or between parts of a circuit. Coupling can be deliberate as part of the function of the circuit, or it may be undesirable, for instance due to coupling to stray fields. For example, energy is transferred from a power source to an electrical load by means of conductive coupling, which may be either resistive or direct coupling. An AC potential may be transferred from one circuit segment to another having a DC potential by use of a [[Capacitor|capacitor]]. Electrical energy may be transferred from one circuit segment to another segment with different impedance by use of a transformer; this is known as impedance matching. These are examples of electrostatic and electrodynamic inductive coupling.

In the context of modular and not, say, trains, coupling is what happens when you patch two modules together. The electrical signal flows out one module, through the patch cable, and into another module’s input. That signal might be alternating current (AC) or direct current (DC). AC signals will come from things like audio oscillators: oscillators make signals that move up and down, generally pretty fast. DC signals will come from places like sequencers, offset generators, or LFOs: unlike audio oscillators, they’re static and they don’t move (or least not very fast). And if an input is DC coupled, you can put a slow or static signal into it; if an output is DC coupled, it’s good for that sort of signal.


#### What is meant by AC vs DC?
AC and DC are abbreviations for Alternating (Capacitive) Coupling and Direct Coupling. This setting is important as it will affect the frequency content of your data.

Most signals are composed of AC and DC components. The DC component is the 0 Hz component that acts as an offset in the time domain. The AC component consists of all other frequencies.

#### AC Coupling
Allows only AC signals to pass through a connection. AC coupling removes the DC offset by making use of a DC-blocking capacitor in series with the signal. AC coupling effectively rejects the DC component of the signal normalizing the signal to a mean of zero.

#### DC Coupling
Allows _both_ AC and DC signals to pass through a connection. The DC component is a 0 Hz signal which acts as an offset about which the AC component of the signal fluctuates.


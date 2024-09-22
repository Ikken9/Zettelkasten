# Crystal Oscillator

A **crystal oscillator** is an electronic oscillator circuit that uses a piezoelectric crystal as a frequency-selective element. The oscillator frequency is often used to keep track of time, as in quartz wristwatches, to provide a stable clock signal for digital integrated circuits, and to stabilize frequencies for radio transmitters and receivers. The most common type of piezoelectric resonator used is a quartz crystal, so oscillator circuits incorporating them became known as crystal oscillators.

A crystal oscillator relies on the slight change in shape of a quartz crystal under an electric field, a property known as inverse piezoelectricity. A voltage applied to the electrodes on the crystal causes it to change shape; when the voltage is removed, the crystal generates a small voltage as it elastically returns to its original shape. The quartz oscillates at a stable resonant frequency, behaving like an RLC circuit, but with a much higher Q factor (less energy loss on each cycle of oscillation). Once a quartz crystal is adjusted to a particular frequency (which is affected by the mass of electrodes attached to the crystal, the orientation of the crystal, temperature and other factors), it maintains that frequency with high stability.

### Crystal Cuts
Crystal blanks are cut from larger pieces of bulk quartz. Since quartz crystal has a predictable, lattice-shaped internal structure, the orientation or angle of the lattice structure can create different "cuts" of crystal blanks.

AT and SC cuts are two of the most common types used in oven controlled crystal oscillators (OCXOs). And just like with any other engineering or design decision, there are advantages and disadvantages that must be considered during the design phase of frequency control devices.

The AT is a temperature-compensated cut, meaning the cut is oriented such that the temperature coefficients of the lattice will have minimal impact on crystal performance.

The SC is a stress-compensated cut, but it is also temperature compensated. Is a double rotated cut (similar to a compound miter cut for the woodworkers out there).


### Output Signal Type

#### Sine Wave 
Is the standard or ‘natural’ signal output of a crystal or oscillator circuit. It consists of one fundamental sinusoidal frequency output. The linearity sine wave outputs offer the best phase noise performance of all the outputs. These are great for applications that require a high-quality output signal.

#### Clipped Sine Wave
The sine wave output is manipulated so it will not reach its max high or low. By doing this you are creating a square wave output without sacrificing any of the desired phase noise performance.


![comparison](sinusoidal-wave-vs-clipped-sine-wave.jpg)
*Sine Wave vs. Clipped Sine Wave*


#### Frequency Stability
Different cuts provide varying levels of frequency stability over temperature changes. More stable cuts like the AT-cut will maintain a more consistent waveform under varying environmental conditions, whereas less stable cuts might result in more waveform distortion.

#### Quality Factor (Q-Factor)
The Q-factor, which represents the damping of the crystal, is influenced by the cut. A high Q-factor crystal will produce a purer waveform with less clipping, while a lower Q-factor might lead to more signal distortion.

#### Jitter
Is a method of describing the stability of an oscillator in the Time Domain. It combines all the noise sources together and shows their effect with respect to time.

An ideal digital oscillator would provide a uniform square wave signal. The time span between two pulses would always be the same, and the pulses always the same length. Predicting when the next pulse arrives would be easy and precise.

In practice, however, the signal is never one hundred percent clean; the pulses sometimes come too early or too late. This phenomenon is called jitter and can negatively affect the function of the circuit. 

There are several types of jitter: period jitter, cycle-to-cycle jitter, peak-to-peak jitter and phase jitter. Each describes the same phenomenon from a different perspective. Consequently, it is not easy to compare the values of the individual types of jitter with each other.

#### Phase Noise
When the output signal of an oscillator deviates in its frequency from the ideal form, we call it phase noise. Phase noise occurs due to the jitter, so both values are related to each other.

Low phase noise is critical in RF applications to maintain the purity of the transmitted and received signals. This affects the signal-to-noise ratio (SNR) and overall performance of the system.



The following formula may be used to calculate a parallel resonant crystal's external load capacitors:  
CL = ((CX1 x CX2) / (CX1 + CX2)) + Cstray  
where:  
CL = the crystal load capacitance  
Cstray = the stray capacitance in the oscillator circuit, which will normally be in the 2pF to 5pF range.

Assuming that CX1=CX2 then the equation becomes:  
CL = ((CX1 x CX1) / (2 x CX1)) + Cstray  
CL = (CX1 / 2) + Cstray  
Rearranging the equation, we can find the external load capacitor value:  
CX1 = 2(CL - Cstray)

For example, if the crystal load capacitance is 15pF, and assuming Cstray=2pF, then:  
CX1 = CX2 = 2(15pF - 2pF) = 26pF
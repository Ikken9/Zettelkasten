# Oscillators

An **electronic oscillator** is an [electronic circuit](https://en.wikipedia.org/wiki/Electronic_circuit "Electronic circuit") that produces a periodic, [oscillating](https://en.wikipedia.org/wiki/Oscillation "Oscillation") or [alternating current](https://en.wikipedia.org/wiki/Alternating_current "Alternating current") (AC) signal, usually a [sine wave](https://en.wikipedia.org/wiki/Sine_wave "Sine wave"), [square wave](https://en.wikipedia.org/wiki/Square_wave "Square wave") or a [triangle wave](https://en.wikipedia.org/wiki/Triangle_wave "Triangle wave"), powered by a [direct current](https://en.wikipedia.org/wiki/Direct_current "Direct current") (DC) source.

Oscillators are often characterized by the [frequency](https://en.wikipedia.org/wiki/Frequency "Frequency") of their output signal:

- A [low-frequency oscillator](https://en.wikipedia.org/wiki/Low-frequency_oscillation "Low-frequency oscillation") (LFO) is an oscillator that generates a frequency below approximately 20 Hz. This term is typically used in the field of audio [synthesizers](https://en.wikipedia.org/wiki/Synthesizer "Synthesizer"), to distinguish it from an audio frequency oscillator.
- An audio oscillator produces frequencies in the [audio](https://en.wikipedia.org/wiki/Audio_frequency "Audio frequency") range, 20 Hz to 20 kHz.
- A [radio frequency](https://en.wikipedia.org/wiki/Radio_frequency "Radio frequency") (RF) oscillator produces signals above the audio range, more generally in the range of 100 kHz to 100 GHz.

There are two general types of electronic oscillators: the **linear** or **harmonic oscillator**, and the **nonlinear** or **[relaxation oscillator](https://en.wikipedia.org/wiki/Relaxation_oscillator "Relaxation oscillator")**. The two types are fundamentally different in how oscillation is produced, as well as in the characteristic type of output signal that is generated.

The most-common linear oscillator in use is the [crystal oscillator](https://en.wikipedia.org/wiki/Crystal_oscillator "Crystal oscillator"), in which the output frequency is controlled by a [piezo-electric](https://en.wikipedia.org/wiki/Piezo-electric "Piezo-electric") [resonator](https://en.wikipedia.org/wiki/Resonator "Resonator") consisting of a vibrating [quartz crystal](https://en.wikipedia.org/wiki/Quartz_crystal "Quartz crystal").


### Rise / Fall Time 
Rise Time is a measure of the transition time from a “Logic 0” to a “Logic 1” level. Fall Time is a measure of the transition time from a “Logic 1” to a “Logic 0” level. Both Rise and Fall Time are typically specified as a maximum transition time in nS (nanoseconds). The transition times are measured at specified voltage thresholds or at specified percentages of the output waveform. 

### Start Time 
Start Time is the time required for the waveform of an oscillator to reach steady state oscillation after power-up, and is usually specified as a maximum time in mS (milliseconds).

### Output Load
Output Load is the maximum load an oscillator can drive. It is specified in terms of number of gates or type of load circuit. For example: HCMOS, TTL and ECL are the most common load types oscillators must drive. An HCMOS load is usually specified as a capacitive load in pF (picofarads). TTL loads are specified as a number of TTL gates. ECL is specified as a resistive load into a specified voltage. Figures 3 through 5 show oscillator test circuits required for the loads mentioned here. When an oscillator can drive both HCMOS and TTL loads under all specified operating conditions, the nomenclature is HCMOS/TTL compatible. The type of load the oscillator must drive is a determining factor for the voltage thresholds used when measuring waveform parameters such as Logic Levels, Duty Cycle and Rise/Fall Time.
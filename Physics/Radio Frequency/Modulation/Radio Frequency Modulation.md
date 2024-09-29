# Radio Frequency Modulation

Modulation is the process of encoding information onto a carrier wave by altering its basic properties, such as [[Signal Amplitude|amplitude]], frequency, or phase.

[[Baseband]] signals are information signals at their original frequencies, typically low frequencies. Wireless communication systems typically will *upshift* the frequency spectrum of baseband signals to a higher range of frequencies to allow transmission through the atmosphere. This high frequency for wireless signal transmission is called the carrier frequency, and the process to shift the baseband signals to carrier frequency is called RF **modulation**.

Since the carrier frequency is at a higher range than baseband signal frequency, the RF modulation process is also referred to as the "*upconversion*".


## **Analog vs. Digital  Modulation**

While **all modulation types are physically analog** in the sense that they involve manipulating a continuous wave (the carrier signal) to encode information, **some modulation techniques are specifically designed for analog signals**, while others are used for **digital signals**. This distinction is based on the type of **information being transmitted** (analog or digital) and how the signal is **interpreted** rather than the modulation itself being inherently analog or digital.


### **Analog Modulation**
These modulation techniques are used to transmit **analog information**, such as sound or video, over an analog signal (continuous values). The modulating signal itself is continuous in time and amplitude. But also while modulating an analog signal, it can be done using a digital carrier, that is called Pulse Modulation. 

##### Examples of Continuous Wave Modulation:
- [[Amplitude Modulation (AM)]]
- [[Frequency Modulation (FM)]]
- [[Phase Modulation (PM)]]

In these techniques, the **carrier wave and the message signal** are both **continuous** and the modulation itself is continuous. Thus, these methods are considered **analog modulation**.

##### Examples of Pulse Modulation:
- [[Pulse Code Modulation (PCM)]]
- [[Pulse Width Modulation (PWM)]]
- [[Pulse Amplitude Modulation (PAM)]]

### **Digital Modulation**
Digital modulation techniques are used to transmit **digital information** (discrete bits: 0s and 1s) by manipulating an analog carrier signal. The carrier is continuous, but the information modulating it is **discrete**.

##### Examples:
- [[Frequency-Shift Keying (FSK)]]
- [[Phase-Shift Keying (PSK)]]
- [[Quadrature Phase-Shift Keying (QPSK)]]
- [[Quadrature Amplitude Modulation (QAM)]]
- [[Amplitude-Shift Keying (ASK)]]


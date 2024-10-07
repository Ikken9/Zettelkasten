# Bandwidth

Bandwidth, typically measured in hertz (Hz), represents the difference between the upper and lower frequencies in a continuous band of frequencies. It plays a crucial role in determining the capacity of communication channels and the performance of systems like amplifiers, [[Filter|filters]], and [[Radio Frequency Modulation|modulated]] signals.

The concept of bandwidth is essential in various technical fields:

- In **radio communications**, bandwidth refers to the frequency range occupied by a modulated carrier signal. Government agencies often regulate available bandwidth to prevent interference between different communication channels.

- In **filter design**, bandwidth is used to describe the range of frequencies over which the system maintains a specified performance level, such as within 3 dB of the maximum gain. The common -3 dB bandwidth defines the point where signal power drops to half its maximum value, providing a standard measure for assessing system performance.

- In **signal processing**, bandwidth often refers to the range of frequencies where the signal’s spectral density remains nonzero or above a small threshold value, frequently defined by the 3 dB point. This ensures the system can process signals within that range.


## Bandwidth and System Capacity
One of the key characteristics of bandwidth is its impact on information-carrying capacity. The same amount of information can be transmitted over any band of a given width, regardless of its location in the frequency spectrum. For example, a 3 kHz band can carry a telephone conversation, whether it is at baseband or modulated to a higher frequency.

However, at higher frequencies, wider bandwidths are easier to obtain and process because the fractional bandwidth (the ratio of bandwidth to the center frequency) is smaller.


## Performance Thresholds
In many applications, such as communication channels, bandwidth is tied to performance criteria. For instance, the essential bandwidth refers to the portion of the signal spectrum that contains most of the energy. Similarly, the system bandwidth denotes the range of frequencies the system can process effectively, often determined by how much performance degradation, such as a drop in gain or power, is acceptable.



## **What is the 3 dB bandwidth of a system?**
The 3 dB bandwidth is one measure of the range of electrical frequencies a system supports. Input signal frequency components in this range are minorly attenuated by the system, while components outside the 3 dB bandwidth are strongly attenuated. The system's frequency response magnitude data specifies the frequency-dependent scaling factors between input and output signals.

As an example, Figure 2 shows the frequency response magnitude data for a low-pass filter that accepts a voltage signal input. Voltage and current signals can be considered in terms of their amplitude or their power. Since the power in one of these signals is proportional to the square of the voltage or current, the power scaling factors are equal to the square of the amplitude scaling factors.

The 3 dB bandwidth specifies the range of frequencies for which the amplitude scaling factors are ≥0.707. This is equivalent to the range over which the power scaling factors ≥0.5. In terms of decibels, a power ratio of 0.5 corresponds to ≥-3 dB. The negative sign is implied in the phrase "3 dB Bandwidth."

The range of input signal components within a system's 3 dB bandwidth dominates the output signal. The output signal is a better representation of the input signal when the 3 dB bandwidth of a system completely overlaps the frequency range of the input signal.

**How can a system's 3 dB bandwidth be measured?**  
The system's bandwidth can be measured using a set of sine waves as input signals. All sine waves should have the same peak-to-peak amplitude, but each should have a different fixed oscillation frequency within the frequency range of interest. It is typical for the lowest oscillation frequency to be close to 0 Hz. For each input sinusoid, the peak-to-peak amplitude of the output signal should be measured. Normalized amplitude scaling factors are obtained by dividing these peak-to-peak measurements by a reference value, which is often the value corresponding to the input signal with the lowest oscillation frequency.
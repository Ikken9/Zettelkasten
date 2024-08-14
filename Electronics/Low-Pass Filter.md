# Low-Pass FIlter

A low-pass filter (LPF) is a circuit that only passes signals below its cutoff frequency while attenuating all signals above it. It is the complement of a high-pass filter, which only passes signals above its cutoff frequency and attenuates all signals below it.

### What is a low-pass filter used for?

Low-pass filters have applications such as anti-aliasing, reconstruction, and speech processing, and can be used in audio amplifiers, equalizers, and speakers.

Low-pass filters can also be used in conjunction with high-pass filters to form bandpass, band-stop, and notch filters. A bandpass filter passes a range of frequencies while attenuating all frequencies outside of the band. A band-stop filter (also called a band reject filter) does the opposite, attenuating signals within its stopband while passing all frequencies outside of it. Notch filters are a type of band-stop filter that attenuate a very narrow set of frequencies, which can be created from a combination of low-pass and high-pass filters with cutoff frequencies very close to each other.

### What is a low-pass filter circuit?

There are many different low-pass filter circuits, which are characterized by their order and amplitude characteristic or the type of polynomial that describes it (Butterworth, Chebyshev, Elliptic, or Bessel):

Butterworth - response that is flat in the passband and an adequate rate of rolloff.

Chebyshev - frequency cutoff is steeper than that of a Butterworth, at the cost of a variation in amplitude known as ripple in the passband.

Elliptic (or Cauer) - compared to the Chebyshev, the stopband cutoff is sharper (without incurring more passband ripple), but transient response is worse.

Bessel - represents a trade-off in the opposite direction from the Butterworth. Transient response is improved, but at the expense of a less steep cutoff in the stopband.

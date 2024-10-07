# Signal Phase

The Phase of a wave or other periodic function $F$ of some variable $t$ (such as time) is an angle-like quantity representing the fraction of the cycle covered up to $t$. It is expressed in such a scale that it varies by one full turn as the variable $t$ goes through each period (and $F(t)$ goes through each complete cycle). 

It also refers to the relationship between two RF signals operating on the same frequency detected by a receiving radio. If two signals are in phase, their peaks and troughs will occur simultaneously. If two signals are out of phase, the peaks and troughs occur at different times.

It may be measured in any angular unit such as degrees or radians, thus increasing by $360^{\circ}$ or $2\pi$ as the variable $t$ completes a full period.

0 degrees of phase separation means that two signals are completely in phase, and the receiving amplitude is combined to create a stronger signal. 180 degrees of phase separation means that the two signals are completely out of phase and will cancel each other out; there is no received signal. Different levels of phase separation will determine whether a receiving signal is increased or decreased at the receiver.

Let the signal $F$ be a periodic function of one real variable, and $T$ be its period (that is, the smallest positive real number such that $F(t+T)=F(t)$ for all $t$. Then the phase of $F$ at any argument $t$ is:

$$\varphi(t) = 2\pi \left[\!\!\left[t-t_0\over T\right]\!\!\right]$$
Here the double brackets denotes the fractional part of a real number, discarding its integer part; that is, $[\![ x ]\!] = x - \lfloor x \rfloor$; and $t_0$ is an arbitrary "origin" value of the argument, that one considers to be the beginning of a cycle.


## **Phase Shift**
The difference $\varphi(t)=\varphi G(t)-\varphi F(t)$ between the phases of two periodic signals $F$ and $G$ is called the _phase difference_ or _phase shift_ of $G$ relative to $F$.


#### Sinusoid Phase Shift
For sinusoidal signals, when the phase difference $\varphi(t)$ is 180° ($\pi$ radians), one says that the phases are *opposite*, and that the signals are *in antiphase*. Then the signals have opposite signs, and destructive interference occurs. Conversely, a _phase reversal_ or _phase inversion_ implies a 180-degree phase shift.

When the phase difference $\varphi(t)$ is a quarter of turn (a right angle, $+90^{\circ} = \frac{\pi}{2}$ or $-90^{\circ} = 270^{\circ} = \frac{-\pi}{2} = \frac{3\pi}{2}$, sinusoidal signals are sometimes said to be in _quadrature_, e.g., [in-phase and quadrature components](https://en.wikipedia.org/wiki/In-phase_and_quadrature_components "In-phase and quadrature components") of a composite signal or even different signals (e.g., voltage and current).

If the frequencies are different, the phase difference $\varphi(t)$ increases linearly with the argument $t$. The periodic changes from reinforcement and opposition cause a phenomenon called beating.

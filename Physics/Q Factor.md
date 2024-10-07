# Q Factor

The **Q factor** (or **Quality Factor**) is a dimensionless parameter that describes how efficiently a resonant circuit (such as an inductor-capacitor (LC) circuit or a filter) stores energy compared to how much energy it loses. It is commonly used in RF (radio frequency) circuits, oscillators, and filters to describe the sharpness or selectivity of resonance.


## **Definitions**:

#### **Bandwidth Q Factor:** 
In the context of resonators, there are two common definitions for $Q$, which are not exactly equivalent. They become approximately equivalent as $Q$ becomes larger, meaning the resonator becomes less damped. One of these definitions is the frequency-to-bandwidth ratio of the resonator:

$$Q = \frac{f_r}{\Delta f} = \frac{\omega_r}{\Delta\omega}$$
where:
- $f_r$ is the resonant frequency.
- $\Delta f$ is the **resonance width** or *full width at half maximum* (FWHM) i.e. the bandwidth over which the power of vibration is greater than half the power at the resonant frequency.
- $\omega_r$ = $2\pi f_r$ is the angular resonant frequency.
- $\Delta\omega$ is the angular half-power bandwidth.

Under this definition, $Q$ is the reciprocal of fractional bandwidth.


#### **Stored Energy Q Factor:**
The other common nearly equivalent definition for $Q$ is the ratio of the energy stored in the oscillating resonator to the energy dissipated per cycle by damping processes:

$$Q = 2\pi \times \frac{energy \; stored}{energy \; dissipated \; per \;cycle} = 2\pi f_r \times \frac{energy \; stored}{power \; loss}$$

The factor $2\pi$ makes $Q$ expressible in simpler terms, involving only the coefficients of the second-order differential equation describing most resonant systems, electrical or mechanical. In electrical systems, the stored energy is the sum of energies stored in lossless [[Inductor|inductors]] and [[Capacitor|capacitors]]; the lost energy is the sum of the energies dissipated in [[Resistor|resistors]] per cycle. In mechanical systems, the stored energy is the sum of the potential and kinetic energies at some point in time; the lost energy is the work done by an external force, per cycle, to maintain amplitude.

More generally and in the context of reactive component specification (especially inductors), the frequency-dependent definition of _Q_ is used:

$$Q(\omega) = \omega \times \frac{maximum \; energy \;stored}{power \; loss}$$
where $\omega$ is the angular frequency at which the stored energy and power loss are measured. This definition is consistent with its usage in describing circuits with a single reactive element (capacitor or inductor), where it can be shown to be equal to the ratio of reactive power to real power.



## Q Factor and Damping
One aspect of the Q factor that is of importance in many circuits is the damping. The Quality Factor, Q determines the qualitative behavior of simple damped oscillators and affects other circuits such as the response within filters, etc.

There are three main regimes which can be considered when referring to the damping and Q factor.

**_Under-damped (Q > 1/2):_** An under-damped system is one where the Q factor is greater than a half. Those systems where the Q factor is only just over a half may oscillate once or twice when a step impulse is applied before the oscillation falls away. As the quality factor increases, so the damping falls and oscillations will be sustained for longer.
In a theoretical system where the Q factor is infinite, the oscillation would be maintained indefinitely without the need for adding any further stimulus. In oscillators some signal is fed back to provide an additional stimulus, but a high Q factor normally produces a much cleaner result. Lower levels of phase noise are present on the signal.

**_Over-damped (Q < 1/2):_** An over-damped system has a Q factor that is less than 1/2. In this type of system, the losses are high and the system has no overshoot. Instead the system will exponential decay, approaching the steady state value asymptotically after a step impulse is applied.
As the Q factor or quality factor is reduced, so the systems responds more slowly to a step impulse.

**_Critically damped (Q = 1/2):_** The critically damped system has a Q factor of 0.5 and like an over-damped system, the output does not oscillate, and does not overshoot its steady-state output. The system will approach the steady-state asymptote in the fastest time without any overshoot.


# Capacitor
## Applications

In terms of pure functionality, no other discrete component can offer as much circuit performance as a capacitor. Although both capacitors and inductors provide field storage for electric and magnetic fields, respectively, the former fields are much easier to contend with. While inductors have their place, capacitors dominate as the charge storage device across the board, able to deliver instantaneous power during dips in the overall net performance.

#### Power Supply Smoothing
One of the most common and fundamental applications of a capacitor is in power supply smoothing. By placing a large electrolytic capacitor in parallel with the output of a rectifier, the capacitor compensates for the fluctuations in the rectified AC waveform, resulting in a relatively smooth DC output. The capacitor achieves this by charging during the voltage peaks and discharging during the intervals between these peaks. However, as the load increases, the capacitor discharges more rapidly, leading to a higher ripple in the output voltage.

#### Timing
Capacitors play a crucial role in timing circuits. When a capacitor is charged through a resistor, the charging process takes a finite amount of time. Similarly, when a resistive load is connected to a charged capacitor, the capacitor takes time to discharge. During the charging phase, the capacitor initially behaves like a short circuit, but once fully charged, it acts as an open circuit.

#### Filtering
Capacitors are also used in filtering applications. When DC voltage is applied to a capacitor, it charges and subsequently blocks any further current flow. However, when an AC signal is applied, the capacitor allows current to flow. The amount of current that flows depends on both the frequency of the AC signal and the capacitance value.

#### Snubber
Similar in concept to a fuse, snubber capacitors provide a safer path for excessive voltage spikes to travel through. A snubber capacitor is connected to a large-current switching node for the purpose of reducing the parasitic inductance of electric wiring. Parasitic inductance causes large surges at switch-off (when the current is blocked), and should such surges exceed component ratings, there are concerns of consequent failure in the worst case.
Unlike a fuse, a snubber is not necessarily sacrificial, allowing circuit operation to continue as it sits in parallel with the circuit that can generate the potential large source spike.


### What Size Capacitor Should You Use?

Selecting an appropriately-sized capacitor can be challenging. The selection of the capacitor should take into account the capacitance, voltage rating, ripple current rating, and temperature. The physical size of the capacitance is influenced by the variation in each of these parameters, and the variation in size is different for each capacitor type, including paper capacitors, mica capacitors, ceramic capacitors, and electrolytic capacitors.


## Types of PCB capacitors available

Typically, there are types of capacitors used in printed circuit boards (PCBs):

##### Aluminum electrolytic capacitors
These come in two types, etched foil, and plain foil. They have high capacitance values relative to their size due to the thickness of the aluminum oxide coating and the high breakdown voltage. They’re commonly used for coupling and DC blocking. But some assemblers prefer to use them as smoothing or flattening capacitors in power supplies.

##### Ceramic capacitors
These are some of the most common capacitors and come in two types, disc and multilayer ceramic capacitors (MLCC). They have high capacitance ratings and are great for filtering out high frequencies. They use dielectric materials with a much greater dielectric constant.

##### Tantalum capacitors 
These are electrolytic capacitors with an anode made of tantalum metal and a cathode made of either liquid or solid electrolyte, and an oxide layer that serves as the dielectric. They have a higher capacitance per unit of size and are smaller than ceramic capacitors.

**Maximum ESR for tantalum capacitors is specified at 100KHz**, as this is fairly close to the switching frequency of most power supplies, while ceramics are typically not specified or are given for resonant frequency only.

##### Film capacitors
These are non-polarized types of capacitors employed in various applications, made of insulating plastic film used as a dielectric. They are versatile and cost-effective.


## Factors to consider when choosing a capacitor

PCB developers must consider various factors when choosing the right capacitor for their design. The most important ones are:

#### 1. Dielectric Permittivity
Dielectric permittivity is a measure of a material’s ability to store electrical energy in an electric field. The higher the dielectric permittivity of a capacitor’s dielectric material, the higher its capacitance. Designers can calculate capacitance using the formula:

$$
C = \frac{\varepsilon A}{d}
$$

Where C is the capacitance, ε is the dielectric permittivity, A is the plate area in square meters, and d is the distance between the plates in meters. Different capacitor types have different dielectric materials, which affect their characteristics.

#### 2. Temperature
Each capacitor has a maximum operating temperature, and exceeding it can cause the insulation around the dielectric to degrade, leading to electrolyte loss and leakage current. Assemblers should select capacitors that can operate safely under the maximum operating temperature of their application.

#### 3. Effective Series Resistance
The equivalent circuit of a capacitor includes effective serial resistance (ESR) and effective serial inductance (ESL). The ESR value changes with frequency and temperature, and it is highest in electrolytic capacitors and lowest in film capacitors. PCB makers should choose capacitors with low ESR values, especially in high-frequency applications.

#### 4. Resonance
As a signal travels through a capacitor, it experiences insertion loss, which reduces its power. The loss increases with frequency until the capacitor reaches its self-resonance frequency, where the impedance becomes zero. In high-frequency applications, a high self-resonance frequency (or low ESL value) is recommended for better noise suppression.

#### 5. DC Biasing
The capacitance rating on a capacitor’s datasheet is under ideal conditions without any DC supply. However, in practical applications, a small DC supply can change the capacitance value of a ceramic capacitor with a high dielectric constant. Ideally, you should go for capacitance value capacitors, use larger package sizes, or switch to different types of capacitors to mitigate this issue.

#### 6. Tolerance
The tolerance value represents the minimum and maximum range of a capacitor from its nominal value. For sensitive applications, engineers should choose capacitors with a low tolerance value. For coupling capacitors, capacitors with wide tolerance values are preferable.

#### 7. Dissipation Factor
Capacitors have internal resistance, which causes power loss when an AC voltage is applied. The rate of loss is called the dissipation factor (DF). Different capacitors have different DF values at different stages of rated voltage, temperature, and frequency of operation. Engineers should select capacitors with the lowest DF possible for their application.

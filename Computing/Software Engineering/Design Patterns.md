# Design Patterns

Los **patrones de diseño** (design patterns) son soluciones habituales a problemas comunes en el diseño de software. Cada patrón es como un plano que se puede personalizar para resolver un problema de diseño particular de tu código.

## Clasificación

Los patrones de diseño varían en su complejidad, nivel de detalle y escala de aplicabilidad al sistema completo que se diseña. Me gusta la analogía de la construcción de carreteras: puedes hacer más segura una intersección instalando semáforos o construyendo un intercambiador completo de varios niveles con pasajes subterráneos para peatones.

Los patrones más básicos y de más bajo nivel suelen llamarse _idioms_. Normalmente se aplican a un único lenguaje de programación.

Los patrones más universales y de más alto nivel son los [[Computing/Software Engineering/images/Architectural Patterns|Architectural Patterns]]. Los desarrolladores pueden implementar estos patrones prácticamente en cualquier lenguaje. Al contrario que otros patrones, pueden utilizarse para diseñar la arquitectura de una aplicación completa.
Cabe mencionar que aunque un patrón arquitectónico comunica una imagen de un sistema, no es una arquitectura como tal. Un patrón arquitectónico es más un concepto que captura elementos esenciales de una arquitectura de software. Muchas arquitecturas diferentes pueden implementar el mismo patrón y por lo tanto compartir las mismas características.


Además, todos los patrones pueden clasificarse por su _propósito_. Este libro cubre tres grupos generales de patrones:

- Los **patrones creacionales** proporcionan mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización de código existente.
    
- Los **patrones estructurales** explican cómo ensamblar objetos y clases en estructuras más grandes a la vez que se mantiene la flexibilidad y eficiencia de la estructura.
    
- Los **patrones de comportamiento** se encargan de una comunicación efectiva y la asignación de responsabilidades entre objetos.


# Catalog

## Creacionales

### Factory

**Factory** define una interfaz para crear un objeto, pero permite que las subclases alteren el tipo de objeto que se crea.

Consiste en utilizar una clase constructora (al estilo del Abstract Factory) abstracta con unos cuantos métodos definidos y otro(s) abstracto(s): el dedicado a la construcción de objetos de un subtipo de un tipo determinado. Es una simplificación del [Abstract Factory](https://es.wikipedia.org/wiki/Abstract_Factory_(patr%C3%B3n_de_dise%C3%B1o) "Abstract Factory (patrón de diseño)"), en la que la [clase abstracta](https://es.wikipedia.org/wiki/Clase_abstracta "Clase abstracta") tiene métodos concretos que usan algunos de los abstractos; según usemos una u otra hija de esta clase abstracta, tendremos uno u otro comportamiento.

#### Estructura

![factory_sctructure](factory_structure.png)

#### Code Example (Java)

```
abstract class Creator {
    // Definimos método abstracto
    public abstract Product factoryMethod();
}
```

```
public class ConcreteCreatorA extends Creator {
    public Product factoryMethod() {
        return new ConcreteProduct();
    }
}
```

```
public interface Product {
    public void doStuff();
}
```

```
public class ConcreteProductA implements Product {
    public void doStuff(){
        System.out.println("Una operación de este producto");
    }
}
```


### Builder

**Builder** es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos y representaciones de un objeto empleando el mismo código de construcción.

Por ejemplo, pensemos en cómo crear un objeto `Casa`. Para construir una casa sencilla, debemos construir cuatro paredes y un piso, así como instalar una puerta, colocar un par de ventanas y ponerle un tejado. Pero ¿qué pasa si quieres una casa más grande y luminosa, con un jardín y otros extras (como sistema de calefacción, instalación de fontanería y cableado eléctrico)?

La solución más sencilla es extender la clase base `Casa` y crear un grupo de subclases que cubran todas las combinaciones posibles de los parámetros. Pero, en cualquier caso, acabarás con una cantidad considerable de subclases. Cualquier parámetro nuevo, como el estilo del porche, exigirá que incrementes esta jerarquía aún más.

El patrón Builder sugiere que saques el código de construcción del objeto de su propia clase y lo coloques dentro de objetos independientes llamados _constructores_.

![house_builder](house_builder.png)
*El patrón Builder te permite construir objetos complejos paso a paso. El patrón Builder no permite a otros objetos acceder al producto mientras se construye.*


El patrón organiza la construcción de objetos en una serie de pasos (`construirParedes`, `construirPuerta`, etc.). Para crear un objeto, se ejecuta una serie de estos pasos en un objeto constructor. Lo importante es que no necesitas invocar todos los pasos. Puedes invocar sólo aquellos que sean necesarios para producir una configuración particular de un objeto.

Puede ser que algunos pasos de la construcción necesiten una implementación diferente cuando tengamos que construir distintas representaciones del producto. Por ejemplo, las paredes de una cabaña pueden ser de madera, pero las paredes de un castillo tienen que ser de piedra.

En este caso, podemos crear varias clases constructoras distintas que implementen la misma serie de pasos de construcción, pero de forma diferente. Entonces podemos utilizar estos constructores en el proceso de construcción (por ejemplo, una serie ordenada de llamadas a los pasos de construcción) para producir distintos tipos de objetos.

#### Estructura

![builder_structure](builder_structure.png)

1) La interfaz **Constructora** declara pasos de construcción de producto que todos los tipos de objetos constructores tienen en común.
2) Los **Constructores Concretos** ofrecen distintas implementaciones de los pasos de construcción. Los constructores concretos pueden crear productos que no siguen la interfaz común.
3) Los **Productos** son los objetos resultantes. Los productos construidos por distintos objetos constructores no tienen que pertenecer a la misma jerarquía de clases o interfaz.
4) La clase **Directora** define el orden en el que se invocarán los pasos de construcción, por lo que puedes crear y reutilizar configuraciones específicas de los productos.
5) El **Cliente** debe asociar uno de los objetos constructores con la clase directora. Normalmente, se hace una sola vez mediante los parámetros del constructor de la clase directora, que utiliza el objeto constructor para el resto de la construcción. No obstante, existe una solución alternativa para cuando el cliente pasa el objeto constructor al método de producción de la clase directora. En este caso, puedes utilizar un constructor diferente cada vez que produzcas algo con la clase directora.

#### Code Example (Java)

```
public class Computer {
	
	//required parameters
	private String HDD;
	private String RAM;
	
	//optional parameters
	private boolean isBluetoothEnabled;
	

	public String getHDD() {
		return HDD;
	}

	public String getRAM() {
		return RAM;
	}

	public boolean isBluetoothEnabled() {
		return isBluetoothEnabled;
	}
	
	private Computer(ComputerBuilder builder) {
		this.HDD=builder.HDD;
		this.RAM=builder.RAM;
		this.isBluetoothEnabled=builder.isBluetoothEnabled;
	}
}
```

```
public static class ComputerBuilder {

	// required parameters
	private String HDD;
	private String RAM;

	// optional parameters
	private boolean isGraphicsCardEnabled;
	private boolean isBluetoothEnabled;
	
	public ComputerBuilder(String hdd, String ram) {
		this.HDD=hdd;
		this.RAM=ram;
	}

	public ComputerBuilder setBluetoothEnabled(boolean isBluetoothEnabled) {
		this.isBluetoothEnabled = isBluetoothEnabled;
		return this;
	}
	
	public Computer build() {
		return new Computer(this);
	}

}
```


### Prototype

**Prototype** es un patrón de diseño creacional que nos permite copiar objetos existentes sin que el código dependa de sus clases.

Digamos que tienes un objeto y quieres crear una copia exacta de él. ¿Cómo lo harías? En primer lugar, debes crear un nuevo objeto de la misma clase. Después debes recorrer todos los campos del objeto original y copiar sus valores en el nuevo objeto.

¡Bien! Pero hay una trampa. No todos los objetos se pueden copiar de este modo, porque algunos de los campos del objeto pueden ser privados e invisibles desde fuera del propio objeto.

Hay otro problema con el enfoque directo. Dado que debes conocer la clase del objeto para crear un duplicado, el código se vuelve dependiente de esa clase. Si esta dependencia adicional no te da miedo, todavía hay otra trampa. En ocasiones tan solo conocemos la interfaz que sigue el objeto, pero no su clase concreta, cuando, por ejemplo, un parámetro de un método acepta cualquier objeto que siga cierta interfaz.

El patrón Prototype delega el proceso de clonación a los propios objetos que están siendo clonados. El patrón declara una interfaz común para todos los objetos que soportan la clonación. Esta interfaz nos permite clonar un objeto sin acoplar el código a la clase de ese objeto. Normalmente, dicha interfaz contiene un único método `clonar`.

La implementación del método `clonar` es muy parecida en todas las clases. El método crea un objeto a partir de la clase actual y lleva todos los valores de campo del viejo objeto, al nuevo. Se puede incluso copiar campos privados, porque la mayoría de los lenguajes de programación permite a los objetos acceder a campos privados de otros objetos que pertenecen a la misma clase.

Un objeto que soporta la clonación se denomina _prototipo_. Cuando tus objetos tienen decenas de campos y miles de configuraciones posibles, la clonación puede servir como alternativa a la creación de subclases.

#### Estructura
![prototype_structure](prototype_structure.png)

#### Code Example (Java)

```
public interface Sheep {  
	Sheep clone();  
	String getName();  
	void setName(String name);  
}
```

```
public class BlackSheep implements Sheep {  
	private String name;  
  
	public BlackSheep(String name) {  
		this.name = name;  
	}  
	  
	public Sheep clone() {  
		return new BlackSheep(this.name);  
	}  
	  
	public String getName() {  
		return name;  
	}  
	  
	public void setName(String name) {  
		this.name = name;  
	}  
}
```

```
public class WhiteSheep implements Sheep {  
	private String name;  
	  
	public WhiteSheep(String name) {  
		this.name = name;  
	}  
	  
	public Sheep clone() {  
		return new WhiteSheep(this.name);  
	}  
	  
	public String getName() {  
		return name;  
	}  
	  
	public void setName(String name) {  
		this.name = name;  
	}  
}
```

```
public class SheepFarm {  
	public static void main(String[] args) {  
		// Create prototype sheep  
		Sheep blackPrototype = new BlackSheep("Baa Baa");  
		Sheep whitePrototype = new WhiteSheep("Fleecy");  
		  
		// Clone sheep as needed  
		Sheep clonedBlackSheep = blackPrototype.clone();  
		Sheep clonedWhiteSheep = whitePrototype.clone();  
		  
		// Customize cloned sheep  
		clonedBlackSheep.setName("Midnight");  
		clonedWhiteSheep.setName("Snowball");  
		  
		// Your sheep farm is thriving!  
		System.out.println("Black sheep: " + clonedBlackSheep.getName());  
		System.out.println("White sheep: " + clonedWhiteSheep.getName());  
	}  
}
```


### Singleton

**Singleton** es un patrón de diseño creacional que nos permite asegurarnos de que una clase tenga una única instancia, a la vez que proporciona un punto de acceso global a dicha instancia.

¿Por qué querría alguien controlar cuántas instancias tiene una clase? El motivo más habitual es controlar el acceso a algún recurso compartido, por ejemplo, una base de datos o un archivo.

Todas las implementaciones del patrón Singleton tienen estos dos pasos en común:

- Hacer privado el constructor por defecto para evitar que otros objetos utilicen el operador `new` con la clase Singleton.
- Crear un método de creación estático que actúe como constructor. Tras bambalinas, este método invoca al constructor privado para crear un objeto y lo guarda en un campo estático. Las siguientes llamadas a este método devuelven el objeto almacenado en caché.

#### Estructura

![singleton_structure](singleton_structure.png)

#### Code Example (Java)

```
class Singleton {

	private static Singleton instance;
	
	private Singleton() {
		System.out.println("Singleton is Instantiated.");
	}
	
	public static Singleton getInstance() {
		if (instance == null)
			instance = new Singleton();
		return instance;
	}
	
	public static void doSomething() {
		System.out.println("Somethong is Done.");
	}
}
```

```
class Example {
    public static void main(String[] args) {
        Singleton.getInstance().doSomething();
    }
}
```


## Estructurales

### Adapter

Se trata de un objeto especial que convierte la interfaz de un objeto, de forma que otro objeto pueda comprenderla.

Los adaptadores ayudan a objetos con distintas interfaces a colaborar. Funciona así:

1. El adaptador obtiene una interfaz compatible con uno de los objetos existentes.
2. Utilizando esta interfaz, el objeto existente puede invocar con seguridad los métodos del adaptador.
3. Al recibir una llamada, el adaptador pasa la solicitud al segundo objeto, pero en un formato y orden que ese segundo objeto espera.


#### Estructura

##### Adaptador de Objetos

Esta implementación utiliza el principio de composición de objetos: el adaptador implementa la interfaz de un objeto y envuelve el otro.

![adapter_structure](ObjectAdapter.png)

En el diagrama se muestra al **Cliente** quien necesita comunicarse con la clase adaptada **Adaptee** mediante un método llamado **methodA**, sin embargo la clase **Adaptee** la cual queremos utilizar tiene otro método diferente llamado **methodB**, por lo tanto las interfaces de comunicación son diferentes. Por tanto la clase Adapter tendrá una instancia de la clase que hay que adaptar y será la que se comunicará con el **Cliente** pero mediante el método que este espera.
Internamente el método de la clase **Adapter** invocará al método de la clase adaptada **Adaptee**.

![adapter_example](adapter_example.png)

#### Code Example (TypeScript)

![adapter_code_example](adapter_code_example.png)

![adapter_code_example_2](adapter_code_example_2.png)

![adapter_code_example_3](adapter_code_example_3.png)

### Bridge

**Bridge** es un patrón de diseño estructural que te permite dividir una clase grande, o un grupo de clases estrechamente relacionadas, en dos jerarquías separadas (abstracción e implementación) que pueden desarrollarse independientemente la una de la otra.

##### Ejemplo

- Abstracción: la capa GUI de la aplicación.
- Implementación: las API de los sistemas operativos.

![bridge_example](bridge_example.png)

El objeto de la abstracción controla la apariencia de la aplicación, delegando el trabajo real al objeto de la implementación vinculado. Las distintas implementaciones son intercambiables siempre y cuando sigan una interfaz común, permitiendo a la misma GUI funcionar con Windows y Linux.

En consecuencia, puedes cambiar las clases de la GUI sin tocar las clases relacionadas con la API. Además, añadir soporte para otro sistema operativo sólo requiere crear una subclase en la jerarquía de implementación.

#### Estructura

![bridge_structure](bridge_structure.png)

La clase base de control remoto declara un campo de referencia que la vincula con un objeto de dispositivo. Todos los controles remotos funcionan con los dispositivos a través de la interfaz general de dispositivos, que permite al mismo remoto soportar varios tipos de dispositivos.

Puedes desarrollar las clases de control remoto independientemente de las clases de dispositivo. Lo único necesario es crear una nueva subclase de control remoto. Por ejemplo, puede ser que un control remoto básico cuente tan solo con dos botones, pero puedes extenderlo añadiéndole funciones, como una batería adicional o pantalla táctil.

El código cliente vincula el tipo deseado de control remoto con un objeto específico de dispositivo a través del constructor del control remoto.


#### Pseudocode

```
// La "abstracción" define la interfaz para la parte de
// "control" de las dos jerarquías de clase. Mantiene una
// referencia a un objeto de la jerarquía de "implementación" y
// delega todo el trabajo real a este objeto.
class RemoteControl is
    protected field device: Device
    constructor RemoteControl(device: Device) is
        this.device = device
    method togglePower() is
        if (device.isEnabled()) then
            device.disable()
        else
            device.enable()
    method volumeDown() is
        device.setVolume(device.getVolume() - 10)
    method volumeUp() is
        device.setVolume(device.getVolume() + 10)
    method channelDown() is
        device.setChannel(device.getChannel() - 1)
    method channelUp() is
        device.setChannel(device.getChannel() + 1)

// Puedes extender clases de la jerarquía de abstracción
// independientemente de las clases de dispositivo.
class AdvancedRemoteControl extends RemoteControl is
    method mute() is
        device.setVolume(0)

// La interfaz de "implementación" declara métodos comunes a
// todas las clases concretas de implementación. No tiene por
// qué coincidir con la interfaz de la abstracción. De hecho,
// las dos interfaces pueden ser completamente diferentes.
// Normalmente, la interfaz de implementación únicamente
// proporciona operaciones primitivas, mientras que la
// abstracción define operaciones de más alto nivel con base en
// las primitivas.
interface Device is
    method isEnabled()
    method enable()
    method disable()
    method getVolume()
    method setVolume(percent)
    method getChannel()
    method setChannel(channel)

// Todos los dispositivos siguen la misma interfaz.
class Tv implements Device is
    // ...

class Radio implements Device is
    // ...

// En algún lugar del código cliente.
tv = new Tv()
remote = new RemoteControl(tv)
remote.togglePower()

radio = new Radio()
remote = new AdvancedRemoteControl(radio)
```

### Composite

**Composite** es un patrón de diseño estructural que te permite componer objetos en estructuras de árbol y trabajar con esas estructuras como si fueran objetos individuales.

El uso del patrón Composite sólo tiene sentido cuando el modelo central de tu aplicación puede representarse en forma de árbol.

Por ejemplo, imagina que tienes dos tipos de objetos: `Productos` y `Cajas`. Una `Caja` puede contener varios `Productos` así como cierto número de `Cajas` más pequeñas. Estas `Cajas` pequeñas también pueden contener algunos `Productos` o incluso `Cajas` más pequeñas, y así sucesivamente.

Digamos que decides crear un sistema de pedidos que utiliza estas clases. Los pedidos pueden contener productos sencillos sin envolver, así como cajas llenas de productos... y otras cajas. ¿Cómo determinarás el precio total de ese pedido?

El patrón Composite sugiere que trabajes con `Productos` y `Cajas` a través de una interfaz común que declara un método para calcular el precio total.

¿Cómo funcionaría este método? Para un producto, sencillamente devuelve el precio del producto. Para una caja, recorre cada artículo que contiene la caja, pregunta su precio y devuelve un total por la caja. Si uno de esos artículos fuera una caja más pequeña, esa caja también comenzaría a repasar su contenido y así sucesivamente, hasta que se calcule el precio de todos los componentes internos. Una caja podría incluso añadir costos adicionales al precio final, como costos de empaquetado.

#### Estructura

![composite_structure](composite_structure.png)

1) La interfaz **Componente** describe operaciones que son comunes a elementos simples y complejos del árbol.
2) La **Hoja** es un elemento básico de un árbol que no tiene subelementos. 
   Normalmente, los componentes de la hoja acaban realizando la mayoría del trabajo real, ya que no tienen a nadie a quien delegarle el trabajo.
3) El **Contenedor** (también llamado _compuesto_) es un elemento que tiene subelementos: hojas u otros contenedores. Un contenedor no conoce las clases concretas de sus hijos. Funciona con todos los subelementos únicamente a través de la interfaz componente. 
   Al recibir una solicitud, un contenedor delega el trabajo a sus subelementos, procesa los resultados intermedios y devuelve el resultado final al cliente. 
4) El **Cliente** funciona con todos los elementos a través de la interfaz componente. Como resultado, el cliente puede funcionar de la misma manera tanto con elementos simples como complejos del árbol. 

En este ejemplo, el patrón **Composite** te permite implementar el apilamiento (_stacking_) de formas geométricas en un editor gráfico.

##### Ejemplo

![composite_example](composite_example.png)

La clase `GráficoCompuesto` es un contenedor que puede incluir cualquier cantidad de subformas, incluyendo otras formas compuestas. Una forma compuesta tiene los mismos métodos que una forma simple. Sin embargo, en lugar de hacer algo por su cuenta, una forma compuesta pasa la solicitud de forma recursiva a todos sus hijos y “suma” el resultado.

El código cliente trabaja con todas las formas a través de la interfaz común a todas las clases de forma. De este modo, el cliente no sabe si está trabajando con una forma simple o una compuesta. El cliente puede trabajar con estructuras de objetos muy complejas sin acoplarse a las clases concretas que forman esa estructura.

#### Pseudocode

```
// La interfaz componente declara operaciones comunes para
// objetos simples y complejos de una composición.
interface Graphic is
    method move(x, y)
    method draw()

// La clase hoja representa objetos finales de una composición.
// Un objeto hoja no puede tener ningún subobjeto. Normalmente,
// son los objetos hoja los que hacen el trabajo real, mientras
// que los objetos compuestos se limitan a delegar a sus
// subcomponentes.
class Dot implements Graphic is
    field x, y

    constructor Dot(x, y) { ... }

    method move(x, y) is
        this.x += x, this.y += y

    method draw() is
        // Dibuja un punto en X e Y.

// Todas las clases de componente pueden extender otros
// componentes.
class Circle extends Dot is
    field radius

    constructor Circle(x, y, radius) { ... }

    method draw() is
        // Dibuja un círculo en X y Y con radio R.

// La clase compuesta representa componentes complejos que
// pueden tener hijos. Normalmente los objetos compuestos
// delegan el trabajo real a sus hijos y después "recapitulan"
// el resultado.
class CompoundGraphic implements Graphic is
    field children: array of Graphic

    // Un objeto compuesto puede añadir o eliminar otros
    // componentes (tanto simples como complejos) a o desde su
    // lista hija.
    method add(child: Graphic) is
        // Añade un hijo a la matriz de hijos.

    method remove(child: Graphic) is
        // Elimina un hijo de la matriz de hijos.

    method move(x, y) is
        foreach (child in children) do
            child.move(x, y)

    // Un compuesto ejecuta su lógica primaria de una forma
    // particular. Recorre recursivamente todos sus hijos,
    // recopilando y recapitulando sus resultados. Debido a que
    // los hijos del compuesto pasan esas llamadas a sus propios
    // hijos y así sucesivamente, se recorre todo el árbol de
    // objetos como resultado.
    method draw() is
        // 1. Para cada componente hijo:
        //     - Dibuja el componente.
        //     - Actualiza el rectángulo delimitador.
        // 2. Dibuja un rectángulo de línea punteada utilizando
        // las coordenadas de delimitación.

// El código cliente trabaja con todos los componentes a través
// de su interfaz base. De esta forma el código cliente puede
// soportar componentes de hoja simples así como compuestos
// complejos.
class ImageEditor is
    field all: CompoundGraphic

    method load() is
        all = new CompoundGraphic()
        all.add(new Dot(1, 2))
        all.add(new Circle(5, 3, 10))
        // ...

    // Combina componentes seleccionados para formar un
    // componente compuesto complejo.
    method groupSelected(components: array of Graphic) is
        group = new CompoundGraphic()
        foreach (component in components) do
            group.add(component)
            all.remove(component)
        all.add(group)
        // Se dibujarán todos los componentes.
        all.draw()
```


### Decorator

**Decorator** es un patrón de diseño estructural que te permite añadir funcionalidades a objetos colocando estos objetos dentro de objetos encapsuladores especiales que contienen estas funcionalidades.


#### Motivation

As an example, consider a window in a [windowing system](https://en.wikipedia.org/wiki/Windowing_system "Windowing system"). To allow [scrolling](https://en.wikipedia.org/wiki/Scrolling "Scrolling") of the window's contents, one may wish to add horizontal or vertical [scrollbars](https://en.wikipedia.org/wiki/Scrollbar "Scrollbar") to it, as appropriate. Assume windows are represented by instances of the _Window_ interface, and assume this class has no functionality for adding scrollbars. One could create a subclass _ScrollingWindow_ that provides them, or create a _ScrollingWindowDecorator_ that adds this functionality to existing _Window_ objects. At this point, either solution would be fine.

Now, assume one also desires the ability to add borders to windows. Again, the original _Window_ class has no support. The _ScrollingWindow_ subclass now poses a problem, because it has effectively created a new kind of window. If one wishes to add border support to many but not _all_ windows, one must create subclasses _WindowWithBorder_ and _ScrollingWindowWithBorder_, etc. This problem gets worse with every new feature or window subtype to be added. For the decorator solution, a new _BorderedWindowDecorator_ is created. Any combination of _ScrollingWindowDecorator_ or _BorderedWindowDecorator_ can decorate existing windows. If the functionality needs to be added to all Windows, the base class can be modified. On the other hand, sometimes (e.g., using external frameworks) it is not possible, legal, or convenient to modify the base class.

In the previous example, the _SimpleWindow_ and _WindowDecorator_ classes implement the _Window_ interface, which defines the _draw()_ method and the _getDescription()_ method that are required in this scenario, in order to decorate a window control.

![decorator_example](UML2_Decorator_Pattern.png)

Cuando tenemos que alterar la funcionalidad de un objeto, lo primero que se viene a la mente es extender una clase. No obstante, la herencia tiene varias limitaciones importantes de las que debes ser consciente.

- La herencia es estática. No se puede alterar la funcionalidad de un objeto existente durante el tiempo de ejecución. Sólo se puede sustituir el objeto completo por otro creado a partir de una subclase diferente.
- Las subclases sólo pueden tener una clase padre. En la mayoría de lenguajes, la herencia no permite a una clase heredar comportamientos de varias clases al mismo tiempo.

Una de las formas de superar estas limitaciones es empleando la _Agregación_ o la _Composición_  en lugar de la _Herencia_. Ambas alternativas funcionan prácticamente del mismo modo: un objeto _tiene una_ referencia a otro y le delega parte del trabajo, mientras que con la herencia, el propio objeto _puede_ realizar ese trabajo, heredando el comportamiento de su superclase.


#### Example

![decorator_ex](decorator_example.png)

#### Pseudocode

```
// La interfaz de componente define operaciones que los
// decoradores pueden alterar.
interface DataSource is
    method writeData(data)
    method readData():data

// Los componentes concretos proporcionan implementaciones por
// defecto para las operaciones. En un programa puede haber
// muchas variaciones de estas clases.
class FileDataSource implements DataSource is
    constructor FileDataSource(filename) { ... }

    method writeData(data) is
        // Escribe datos en el archivo.

    method readData():data is
        // Lee datos del archivo.

// La clase decoradora base sigue la misma interfaz que los
// demás componentes. El principal propósito de esta clase es
// definir la interfaz de encapsulación para todos los
// decoradores concretos. La implementación por defecto del
// código de encapsulación puede incluir un campo para almacenar
// un componente envuelto y los medios para inicializarlo.
class DataSourceDecorator implements DataSource is
    protected field wrappee: DataSource

    constructor DataSourceDecorator(source: DataSource) is
        wrappee = source

    // La decoradora base simplemente delega todo el trabajo al
    // componente envuelto. En los decoradores concretos se
    // pueden añadir comportamientos adicionales.
    method writeData(data) is
        wrappee.writeData(data)

    // Los decoradores concretos pueden invocar la
    // implementación padre de la operación en lugar de invocar
    // directamente al objeto envuelto. Esta solución simplifica
    // la extensión de las clases decoradoras.
    method readData():data is
        return wrappee.readData()

// Los decoradores concretos deben invocar métodos en el objeto
// envuelto, pero pueden añadir algo de su parte al resultado.
// Los decoradores pueden ejecutar el comportamiento añadido
// antes o después de la llamada a un objeto envuelto.
class EncryptionDecorator extends DataSourceDecorator is
    method writeData(data) is
        // 1. Encripta los datos pasados.
        // 2. Pasa los datos encriptados al método writeData
        // (escribirDatos) del objeto envuelto.

    method readData():data is
        // 1. Obtiene datos del método readData (leerDatos) del
        // objeto envuelto.
        // 2. Intenta descifrarlo si está encriptado.
        // 3. Devuelve el resultado.

// Puedes envolver objetos en varias capas de decoradores.
class CompressionDecorator extends DataSourceDecorator is
    method writeData(data) is
        // 1. Comprime los datos pasados.
        // 2. Pasa los datos comprimidos al método writeData del
        // objeto envuelto.

    method readData():data is
        // 1. Obtiene datos del método readData del objeto
        // envuelto.
        // 2. Intenta descomprimirlo si está comprimido.
        // 3. Devuelve el resultado.

// Un ejemplo sencillo del montaje de un decorador.
class Application is
    method dumbUsageExample() is
        source = new FileDataSource("somefile.dat")
        source.writeData(salaryRecords)
        // El archivo objetivo se ha escrito con datos sin
        // formato.

        source = new CompressionDecorator(source)
        source.writeData(salaryRecords)
        // El archivo objetivo se ha escrito con datos
        // comprimidos.

        source = new EncryptionDecorator(source)
        // La variable fuente ahora contiene esto:
        // Cifrado > Compresión > FileDataSource
        source.writeData(salaryRecords)
        // El archivo se ha escrito con datos comprimidos y
        // encriptados.
```


### Facade

**Facade** es un patrón de diseño estructural que proporciona una interfaz simplificada a una biblioteca, un framework o cualquier otro grupo complejo de clases.

Imagina que debes lograr que tu código trabaje con un amplio grupo de objetos que pertenecen a una sofisticada biblioteca o _framework_. Normalmente, debes inicializar todos esos objetos, llevar un registro de las dependencias, ejecutar los métodos en el orden correcto y así sucesivamente.

Como resultado, la lógica de negocio de tus clases se vería estrechamente acoplada a los detalles de implementación de las clases de terceros, haciéndola difícil de comprender y mantener.

Una fachada es una clase que proporciona una interfaz simple a un subsistema complejo que contiene muchas partes móviles. Una fachada puede proporcionar una funcionalidad limitada en comparación con trabajar directamente con el subsistema. Sin embargo, tan solo incluye las funciones realmente importantes para los clientes.

Tener una fachada resulta útil cuando tienes que integrar tu aplicación con una biblioteca sofisticada con decenas de funciones, de la cual sólo necesitas una pequeña parte.

Por ejemplo, una aplicación que sube breves vídeos divertidos de gatos a las redes sociales, podría potencialmente utilizar una biblioteca de conversión de vídeo profesional. Sin embargo, lo único que necesita en realidad es una clase con el método simple `codificar(nombreDelArchivo, formato)`. Una vez que crees dicha clase y la conectes con la biblioteca de conversión de vídeo, tendrás tu primera fachada.

#### Ejemplo

![facade_example](facade_example.png)

#### Pseudocode

```
// Estas son algunas de las clases de un framework de conversión
// de video de un tercero. No controlamos ese código, por lo que
// no podemos simplificarlo.

class VideoFile
// ...

class OggCompressionCodec
// ...

class MPEG4CompressionCodec
// ...

class CodecFactory
// ...

class BitrateReader
// ...

class AudioMixer
// ...

// Creamos una clase fachada para esconder la complejidad del
// framework tras una interfaz simple. Es una solución de
// equilibrio entre funcionalidad y simplicidad.
class VideoConverter is
    method convert(filename, format):File is
        file = new VideoFile(filename)
        sourceCodec = (new CodecFactory).extract(file)
        if (format == "mp4")
            destinationCodec = new MPEG4CompressionCodec()
        else
            destinationCodec = new OggCompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = (new AudioMixer()).fix(result)
        return new File(result)

// Las clases Application no dependen de un millón de clases
// proporcionadas por el complejo framework. Además, si decides
// cambiar los frameworks, sólo tendrás de volver a escribir la
// clase fachada.
class Application is
    method main() is
        convertor = new VideoConverter()
        mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
        mp4.save()
```


### Proxy

**Proxy** es un patrón de diseño estructural que te permite proporcionar un sustituto o marcador de posición para otro objeto. Un proxy controla el acceso al objeto original, permitiéndote hacer algo antes o después de que la solicitud llegue al objeto original.

¿Por qué querrías controlar el acceso a un objeto? Imagina que tienes un objeto enorme que consume una gran cantidad de recursos del sistema. Lo necesitas de vez en cuando, pero no siempre.

Puedes llevar a cabo una implementación diferida, es decir, crear este objeto sólo cuando sea realmente necesario. Todos los clientes del objeto tendrán que ejecutar algún código de inicialización diferida. Lamentablemente, esto seguramente generará una gran cantidad de código duplicado.

En un mundo ideal, querríamos meter este código directamente dentro de la clase de nuestro objeto, pero eso no siempre es posible. Por ejemplo, la clase puede ser parte de una biblioteca cerrada de un tercero.

#### Estructura

![proxy_structure](proxy_structure.png)


#### Code Example

```
// Define the Image interface  
public interface Image {  
	void display();  
}
```

```
public class RealImage implements Image {  
	private String filename;  
  
	public RealImage(String filename) {  
		this.filename = filename;  
		loadFromDisk();  
	}  
  
	private void loadFromDisk() {  
		System.out.println("Loading image: " + filename);  
	}  
	  
	public void display() {  
		System.out.println("Displaying image: " + filename);  
	}  
}
```

```
public class ProxyImage implements Image {  
	private RealImage realImage;  
	private String filename;  
	  
	public ProxyImage(String filename) {  
		this.filename = filename;  
	}  
	  
	public void display() {  
		if (realImage == null) {  
			realImage = new RealImage(filename);  
		}  
		realImage.display();  
	}  
}
```

```
public class ProxyPatternMain {  
	public static void main(String[] args) {  
		Image image1 = new ProxyImage("image1.jpg");  
		Image image2 = new ProxyImage("image2.jpg");  
		  
		image1.display(); // Image 1 will be loaded and displayed  
		image2.display(); // Image 2 will be loaded and displayed  
		  
		image1.display();  
	}  
}
```


## Comportamentales

### Chain of Responsibility

**Chain of Responsibility** es un patrón de diseño de comportamiento que te permite pasar solicitudes a lo largo de una cadena de manejadores. Al recibir una solicitud, cada manejador decide si la procesa o si la pasa al siguiente manejador de la cadena.

Al igual que muchos otros patrones de diseño de comportamiento, el **Chain of Responsibility** se basa en transformar comportamientos particulares en objetos autónomos llamados _manejadores_. En nuestro caso, cada comprobación debe ponerse dentro de su propia clase con un único método que realice la comprobación. La solicitud, junto con su información, se pasa a este método como argumento.

El patrón sugiere que vincules esos manejadores en una cadena. Cada manejador vinculado tiene un campo para almacenar una referencia al siguiente manejador de la cadena. Además de procesar una solicitud, los manejadores la pasan a lo largo de la cadena. La solicitud viaja por la cadena hasta que todos los manejadores han tenido la oportunidad de procesarla.

#### Estructura

![chain_of_responsibility](chain_of_responsibility.png)



### Mediator

**Mediator** es un patrón de diseño de comportamiento que te permite reducir las dependencias caóticas entre objetos. El patrón restringe las comunicaciones directas entre los objetos, forzándolos a colaborar únicamente a través de un objeto mediador.


El patrón Mediator sugiere que detengas toda comunicación directa entre los componentes que quieres hacer independientes entre sí. En lugar de ello, estos componentes deberán colaborar indirectamente, invocando un objeto mediador especial que redireccione las llamadas a los componentes adecuados. Como resultado, los componentes dependen únicamente de una sola clase mediadora, en lugar de estar acoplados a decenas de sus colegas.

En nuestro ejemplo del formulario de edición de perfiles, la propia clase de diálogo puede actuar como mediadora. Lo más probable es que la clase de diálogo conozca ya todos sus subelementos, por lo que ni siquiera será necesario que introduzcas nuevas dependencias en esta clase.


Antes de implementar **Mediator**:

![mediator_problem](problem1-mediator.png)

Después de implementar **Mediator**:

![solution_mediator](solution1-mediator.png)


#### Estructura

![mediator_structure](mediator_structure.png)

### Memento

**Memento** es un patrón de diseño de comportamiento que te permite guardar y restaurar el estado previo de un objeto sin revelar los detalles de su implementación.

El patrón Memento delega la creación de instantáneas de estado al propietario de ese estado, el objeto _originador_. Por lo tanto, en lugar de que haya otros objetos intentando copiar el estado del editor desde el “exterior”, la propia clase editora puede hacer la instantánea, ya que tiene pleno acceso a su propio estado.

El patrón sugiere almacenar la copia del estado del objeto en un objeto especial llamado _memento_. Los contenidos del memento no son accesibles para ningún otro objeto excepto el que lo produjo. Otros objetos deben comunicarse con mementos utilizando una interfaz limitada que pueda permitir extraer los metadatos de la instantánea (tiempo de creación, el nombre de la operación realizada, etc.), pero no el estado del objeto original contenido en la instantánea.

![memento](memento_solution.png)

#### Estructura

![memento_structure](memento_structure.png)

### Observer

**También llamado**: Observador, Publicación-Suscripción, Modelo-patrón, Event-Subscriber, Listener

Es un patrón de diseño de comportamiento que te permite definir un mecanismo de suscripción para notificar a varios objetos sobre cualquier evento que le suceda al objeto que están observando.

It is often used for implementing distributed [event-handling](https://en.wikipedia.org/wiki/Event_handling "Event handling") systems in [event-driven software](https://en.wikipedia.org/wiki/Event-driven_programming "Event-driven programming"). In such systems, the subject is usually named a "stream of events" or "stream source of events" while the observers are called "sinks of events." The stream nomenclature alludes to a physical setup in which the observers are physically separated and have no control over the emitted events from the subject/stream source. This pattern thus suits any process by which data arrives from some input that is not available to the [CPU](https://en.wikipedia.org/wiki/CPU "CPU") at [startup](https://en.wikipedia.org/wiki/Booting "Booting"), but instead arrives seemingly at random ([HTTP requests](https://en.wikipedia.org/wiki/HTTP_request "HTTP request"), [GPIO](https://en.wikipedia.org/wiki/GPIO "GPIO") data, [user input](https://en.wikipedia.org/wiki/User_input "User input") from [peripherals](https://en.wikipedia.org/wiki/Peripheral "Peripheral") and [distributed databases](https://en.wikipedia.org/wiki/Distributed_database "Distributed database"), etc.).

El patrón Observer sugiere que añadas un mecanismo de suscripción a la clase notificadora para que los objetos individuales puedan suscribirse o cancelar su suscripción a un flujo de eventos que proviene de esa notificadora. ¡No temas! No es tan complicado como parece. En realidad, este mecanismo consiste en: 1) un campo matriz para almacenar una lista de referencias a objetos suscriptores y 2) varios métodos públicos que permiten añadir suscriptores y eliminarlos de esa lista.

![observer](observer_solution1.png)

Ahora, cuando le sucede un evento importante al notificador, recorre sus suscriptores y llama al método de notificación específico de sus objetos.

![observer2](observer_solution2.png)



#### Estructura

![observer_structure](observer_structure.png)

#### Example

![observer_example](observer_example.png)

### State

**State** es un patrón de diseño de comportamiento que permite a un objeto alterar su comportamiento cuando su estado interno cambia. Parece como si el objeto cambiara su clase.

El patrón State está estrechamente relacionado con el concepto de la _Máquina de estados finitos_.

![finite_state_machine](finite_state_machine.png)
*Máquina de estados finitos*\


La idea principal es que, en cualquier momento dado, un programa puede encontrarse en un número _finito_ de _estados_. Dentro de cada estado único, el programa se comporta de forma diferente y puede cambiar de un estado a otro instantáneamente. Sin embargo, dependiendo de un estado actual, el programa puede cambiar o no a otros estados. Estas normas de cambio llamadas _transiciones_ también son finitas y predeterminadas.

También puedes aplicar esta solución a los objetos. Imagina que tienes una clase `Documento`. Un documento puede encontrarse en uno de estos tres estados: `Borrador`, `Moderación` y `Publicado`. El método `publicar` del documento funciona de forma ligeramente distinta en cada estado:

- En `Borrador`, mueve el documento a moderación.
- En `Moderación`, hace público el documento, pero sólo si el usuario actual es un administrador.
- En `Publicado`, no hace nada en absoluto.

![state_problem](state_problem2.png)

Las máquinas de estado se implementan normalmente con muchos operadores condicionales (`if` o `switch`) que seleccionan el comportamiento adecuado dependiendo del estado actual del objeto. Normalmente, este “estado” es tan solo un grupo de valores de los campos del objeto. Aunque nunca hayas oído hablar de máquinas de estados finitos, probablemente hayas implementado un estado al menos alguna vez. ¿Te suena esta estructura de código?

```
class Document is
    field state: string
    // ...
    method publish() is
        switch (state)
            "draft":
                state = "moderation"
                break
            "moderation":
                if (currentUser.role == "admin")
                    state = "published"
                break
            "published":
                // No hacer nada.
                break
    // ...
```

El patrón State sugiere que crees nuevas clases para todos los estados posibles de un objeto y extraigas todos los comportamientos específicos del estado para colocarlos dentro de esas clases.

En lugar de implementar todos los comportamientos por su cuenta, el objeto original, llamado _contexto_, almacena una referencia a uno de los objetos de estado que representa su estado actual y delega todo el trabajo relacionado con el estado a ese objeto.

![state_solution](state_solution.png)

#### Example

![state_example](state_example.png)

#### Pseudocode

```
// La clase ReproductordeAudio actúa como un contexto. También
// mantiene una referencia a una instancia de una de las clases
// estado que representa el estado actual del reproductor de
// audio.
class AudioPlayer is
    field state: State
    field UI, volume, playlist, currentSong

    constructor AudioPlayer() is
        this.state = new ReadyState(this)

        // El contexto delega la gestión de entradas del usuario
        // a un objeto de estado. Naturalmente, el resultado
        // depende del estado que esté activo ahora, ya que cada
        // estado puede gestionar las entradas de manera
        // diferente.
        UI = new UserInterface()
        UI.lockButton.onClick(this.clickLock)
        UI.playButton.onClick(this.clickPlay)
        UI.nextButton.onClick(this.clickNext)
        UI.prevButton.onClick(this.clickPrevious)

    // Otros objetos deben ser capaces de cambiar el estado
    // activo del reproductor.
    method changeState(state: State) is
        this.state = state

    // Los métodos UI delegan la ejecución al estado activo.
    method clickLock() is
        state.clickLock()
    method clickPlay() is
        state.clickPlay()
    method clickNext() is
        state.clickNext()
    method clickPrevious() is
        state.clickPrevious()

    // Un estado puede invocar algunos métodos del servicio en
    // el contexto.
    method startPlayback() is
        // ...
    method stopPlayback() is
        // ...
    method nextSong() is
        // ...
    method previousSong() is
        // ...
    method fastForward(time) is
        // ...
    method rewind(time) is
        // ...

// La clase estado base declara métodos que todos los estados
// concretos deben implementar, y también proporciona una
// referencia inversa al objeto de contexto asociado con el
// estado. Los estados pueden utilizar la referencia inversa
// para dirigir el contexto a otro estado.
abstract class State is
    protected field player: AudioPlayer

    // El contexto se pasa a sí mismo a través del constructor
    // del estado. Esto puede ayudar al estado a extraer
    // información de contexto útil si la necesita.
    constructor State(player) is
        this.player = player

    abstract method clickLock()
    abstract method clickPlay()
    abstract method clickNext()
    abstract method clickPrevious()

// Los estados concretos implementan varios comportamientos
// asociados a un estado del contexto.
class LockedState extends State is

    // Cuando desbloqueas a un jugador bloqueado, puede asumir
    // uno de dos estados.
    method clickLock() is
        if (player.playing)
            player.changeState(new PlayingState(player))
        else
            player.changeState(new ReadyState(player))

    method clickPlay() is
        // Bloqueado, no hace nada.

    method clickNext() is
        // Bloqueado, no hace nada.

    method clickPrevious() is
        // Bloqueado, no hace nada.

// También pueden disparar transiciones de estado en el
// contexto.
class ReadyState extends State is
    method clickLock() is
        player.changeState(new LockedState(player))

    method clickPlay() is
        player.startPlayback()
        player.changeState(new PlayingState(player))

    method clickNext() is
        player.nextSong()

    method clickPrevious() is
        player.previousSong()

class PlayingState extends State is
    method clickLock() is
        player.changeState(new LockedState(player))

    method clickPlay() is
        player.stopPlayback()
        player.changeState(new ReadyState(player))

    method clickNext() is
        if (event.doubleclick)
            player.nextSong()
        else
            player.fastForward(5)

    method clickPrevious() is
        if (event.doubleclick)
            player.previous()
        else
            player.rewind(5)
```


### Strategy

**Strategy** es un patrón de diseño de comportamiento que te permite definir una familia de algoritmos, colocar cada uno de ellos en una clase separada y hacer sus objetos intercambiables.

El patrón Strategy sugiere que tomes esa clase que hace algo específico de muchas formas diferentes y extraigas todos esos algoritmos para colocarlos en clases separadas llamadas _estrategias_.

La clase original, llamada _contexto_, debe tener un campo para almacenar una referencia a una de las estrategias. El contexto delega el trabajo a un objeto de estrategia vinculado en lugar de ejecutarlo por su cuenta.

La clase contexto no es responsable de seleccionar un algoritmo adecuado para la tarea. En lugar de eso, el cliente pasa la estrategia deseada a la clase contexto. De hecho, la clase contexto no sabe mucho acerca de las estrategias. Funciona con todas las estrategias a través de la misma interfaz genérica, que sólo expone un único método para disparar el algoritmo encapsulado dentro de la estrategia seleccionada.

De esta forma, el contexto se vuelve independiente de las estrategias concretas, así que puedes añadir nuevos algoritmos o modificar los existentes sin cambiar el código de la clase contexto o de otras estrategias.

#### Estructura

![strategy_structure](strategy_structure.png)



### Visitor

**Visitor** es un patrón de diseño de comportamiento que te permite separar algoritmos de los objetos sobre los que operan.

It is used when we have to perform an operation on a group of similar kind of Objects. With the help of visitor pattern, we can move the operational logic from the objects to another class. The visitor pattern consists of two parts:

- a method called **Visit()** which is implemented by the visitor and is called for every element in the data structure
- visitable classes providing **Accept()** methods that accept a visitor


El objeto que originalmente tenía que realizar el comportamiento se pasa ahora a uno de los métodos del visitante como argumento, de modo que el método accede a toda la información necesaria contenida dentro del objeto.

#### Estructura

![visitor_structure](visitor_structure.png)




*See also* [[Low Coupling, High Cohesion]], [[Anti-Patterns]]
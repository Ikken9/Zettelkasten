# exercising

**¿Cuáles son las diferencias entre disponibilidad y escalabilidad?**
La disponibilidad se refiere a la capacidad de mantener el sistema en funcionamiento sin interrupciones, mientras que la escalabilidad se refiere a la capacidad de manejar una mayor carga de trabajo. 

**Describa SLA de un servicio en la nube:**
Un SLA es un documento que establece las expectativas y garantías de rendimiento entre un proveedor de servicios y un cliente, incluyendo los niveles de servicio y las penalizaciones por incumplimiento. 

**¿Cuáles son las diferencias entre la escalabilidad vertical y horizontal?** 
La escalabilidad vertical se refiere a agregar más recursos a un solo servidor, como CPU y RAM, para aumentar su capacidad, mientras que la escalabilidad horizontal implica agregar más servidores y/o contenedores al sistema. 

**¿Qué ventajas proporciona una infraestructura en la nube vs. on-premise?** 
La infraestructura en la nube es inherentemente descentralizada, lo que permite la recuperación de fallos y la continuidad del servicio incluso en caso de eventos catastróficos en una región. 

**¿Qué característica principal distingue a IaaS de otros servicios en la nube?** 
En un modelo IaaS, se tiene el máximo control sobre tus recursos en la nube, incluyendo la configuración del sistema operativo, la red, bases de datos, almacenamiento, etc. 

**¿Cuáles son las diferencias entre PaaS y IaaS?** 
PaaS se enfoca en proporcionar una plataforma completa para el desarrollo y despliegue de aplicaciones, mientras que IaaS se centra en proporcionar recursos de infraestructura, como servidores y almacenamiento, que pueden ser configurados y gestionados por el usuario. 

**Describa el concepto de SaaS en el contexto de servicios en la nube** 
SaaS es un modelo que proporciona acceso a aplicaciones y software alojados en la nube disponibles a través de Internet. 

**¿Cuál es el propósito principal de las Availability Zones en la infraestructura de Azure?** 
Las Availability Zones están diseñadas para proporcionar resiliencia y continuidad operativa en caso de fallos en uno de los datacenters. 

**¿Qué función desempeñan las Azure Regions en la infraestructura de Azure?** 
Las Azure Regions son áreas geográficas que contienen al menos un datacenter y permiten una distribución de recursos equilibrada.

**¿Qué propósito tiene emparejar regiones en Microsoft Azure?** 
El emparejamiento de regiones ayuda a reducir la probabilidad de interrupciones debido a eventos como desastres naturales o fallas de red. 

**¿Cuáles son las ventajas clave de utilizar Azure Virtual Machines (VMs) en comparación con hardware físico?** 
Las VMs ofrecen flexibilidad de virtualización sin necesidad de comprar ni mantener el hardware físico. 

**¿Qué es una imagen en el contexto de Azure Virtual Machines (VMs)?** 
Una imagen es una plantilla utilizada para crear una VM y puede incluir un sistema operativo y otro software. 

**¿Cuales son las diferencias entre Virtual Machine Scale Sets y Virtual Machine Availability Sets?** 
Los Virtual Machine Scale Sets permiten configurar automáticamente un balanceador de carga, mientras que los Virtual Machine Availability Sets se enfocan en agrupar VMs para evitar la pérdida de todas las VMs en caso de falla. 

**¿Qué significa la expresión "lift and shift" en el contexto de la migración a la nube con VMs?** 
"Lift and shift" se refiere a la migración de una infraestructura física a la nube mediante la creación de una imagen de la infraestructura existente y su implementación en una máquina virtual en la nube. 

**Cuando se provisiona una VM en Azure, ¿cuáles son algunos de los recursos que se pueden seleccionar durante el proceso de creación?** 
Se pueden seleccionar el tamaño de la VM (CPU, RAM),, los discos de almacenamiento (HDD, SSD) y la configuración de red, incluyendo la dirección IP pública. 

**¿Qué diferencias tienen los containers y las máquinas virtuales (VMs)?** 
A diferencia de las VMs, en los containers no se administra el sistema operativo. Los containers son más ligeros y están diseñados para crear, escalar y detenerse de manera dinámica. 

**¿Qué motor de containers se menciona como uno de los más populares y que Azure admite?**
Docker 

**¿Cuáles son los beneficios de utilizar containers en una arquitectura de microservicios?** 
Con containers, puedes separar porciones de tu aplicación en secciones lógicas que pueden ser mantenidas, escaladas o actualizadas de manera independiente. 

**¿Qué ventajas proporciona utilizar conexiones VPN sitio a sitio en Azure?**
Las conexiones VPN sitio a sitio enlazan dispositivos VPN locales a Azure y permiten que los dispositivos en Azure parezcan estar en la red local. 

**¿Para qué sirve una red virtual privada (VPN)?**
Las VPNs se despliegan para conectar dos o más redes privadas de confianza a través de una red no confiable, como Internet. 

**¿Por qué es importante considerar la replicación de datos en una segunda región geográficamente distante al elegir una opción de redundancia en Azure Storage?**
Para proteger los datos contra fallas de hardware en la región primaria. 

**¿Qué servicios proporciona Azure Active Directory?** 
Autenticación y servicios de inicio de sesión único (SSO), etc. 

**¿Qué significa SSO y para qué sirve?**
SSO permite a los usuarios acceder a múltiples recursos y aplicaciones con una sola credencial. 

**Describa qué significa MFA y sus ventajas**
La MFA ofrece mecanismos alternativos y adicionales al inicio de sesión por usuario y contraseña. 

**¿Con qué tipo de mecanismo se reemplaza la contraseña en la autenticación sin contraseña (passwordless authentication)?** 
Se reemplaza la contraseña con algo que tienes en conjunto con algo que eres o algo que conoces. 

**¿Qué significa RBAC (Control de Acceso Basado en Roles)?** 
Controlar el acceso a los recursos de la nube mediante roles y permisos. 

**¿Cuál es una diferencia fundamental entre el modelo de seguridad Zero Trust y el modelo de seguridad tradicional?**
El modelo de seguridad Zero Trust requiere autenticación y autorización independientemente de la ubicación o red. 

**¿Cuál es una consideración importante relacionada con la geografía al aprovisionar recursos en Azure?**
Los costos de implementación de recursos en Azure pueden variar según la ubicación geográfica. 

**¿Cuál es la principal diferencia entre Azure PowerShell y Azure CLI?** 
Azure PowerShell es exclusivo para sistemas Windows, mientras que Azure CLI es compatible con Windows, Linux y Mac. 

**¿Qué beneficios presenta utilizar Infrastructure as Code (IaC) en la gestión de recursos en la nube?** 
Mayor automatización y reproducibilidad en la implementación de recursos.
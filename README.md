# Trabajo Final Machine Learning
### Integrantes
- Paulo Sergio Costa Mondragón 
- Enzo Fabricio Camargo Ramírez
- Henry Josué Diaz Huarcaya
## Milestone 4: TA3
## Introduction

En el vertiginoso panorama de la inteligencia artificial y la visión por computadora, el desarrollo de modelos capaces de transformar imágenes bidimensionales (2D) en representaciones tridimensionales (3D) ha emergido como un campo de investigación crucial. Este informe se centra en el diseño, la implementación y la evaluación de una red generativa adversarial (GAN) para abordar precisamente este desafío.

El propósito fundamental de este trabajo final ha sido la creación de un sistema que, a partir de un conjunto de datos compuesto por información no estructurada 2D, sea capaz de generar imágenes realistas en 3D que capturen la estructura y las características volumétricas de los objetos representados. Para ello, se empleó una arquitectura de GAN, una técnica de aprendizaje profundo conocida por su capacidad para generar datos nuevos e inéditos a partir de distribuciones existentes.

A lo largo de este informe, se detallarán los elementos esenciales de la GAN implementada, incluyendo su arquitectura, el proceso de entrenamiento, los desafíos encontrados y las estrategias adoptadas para superarlos. Además, se analizarán los resultados obtenidos, evaluando la calidad y la coherencia de las imágenes generadas en 3D, así como su utilidad en contextos específicos de aplicación.

## Objectives

El objetivo principal de este proyecto fue diseñar, implementar y evaluar una Generative Adversarial Network (GAN) capaz de transformar imágenes bidimensionales (2D) en representaciones tridimensionales (3D) de alta calidad y realismo.

### Objetivos específicos incluyeron:

1. Desarrollar una arquitectura de GAN adecuada: Investigar y diseñar una estructura de red neural que pudiera manejar de manera eficiente la transformación de datos 2D a 3D, manteniendo la coherencia estructural y las características distintivas de los objetos.

2. Recopilar y preprocesar datos de entrada: Recolectar y preparar un conjunto de datos diverso de imágenes 2D representativas de los objetos a transformar, asegurando su calidad y consistencia para el entrenamiento del modelo.

3. Implementar el proceso de entrenamiento: Desarrollar un entorno de entrenamiento para la GAN que optimice la generación de imágenes 3D realistas a partir de las imágenes 2D, ajustando parámetros y optimizando la red para mejorar la calidad de las salidas.

4. Evaluar la calidad de las imágenes generadas: Establecer métricas y procedimientos de evaluación para medir la calidad, la coherencia estructural y la precisión de las imágenes en 3D generadas por la red GAN en comparación con los datos reales.

5. Analizar la utilidad y aplicabilidad: Examinar la idoneidad de las imágenes generadas en contextos específicos de aplicación, evaluando su utilidad para tareas prácticas o su potencial en aplicaciones industriales, científicas o de diseño.

El cumplimiento de estos objetivos proporcionará una comprensión profunda del rendimiento y la capacidad de la GAN desarrollada para transformar imágenes 2D en representaciones realistas en 3D, así como su relevancia en diversos dominios de aplicación.

## Methodology

### Data processing and Transformation

A pesar de que la data conseguida provenga de un dataset de imágenes 3d de sillas en .off, la transformación de estos datos nos dá un data 2d en forma de .binvoxels. Gracias a la librería binvox es posible obtener imágenes de los objetos 3d en distintas posiciones.

![image](https://github.com/PSCostaM/TF_MachineLearning_u201912086_u20201c579_u202010122/assets/48858434/db28a1a1-9d5b-4188-9f96-9fbc194127ec)

El cuadro presentado es una representación "oversimplified" del procesamiento de datos para tener data de entrenamiento para el modelo GAN. La transformación de .binvoxels a imágenes nos sirve para visualizar la data escrita en los archivos generados y revisar cómo es que la librería binvox transforma los archivos .off.


![chair_108](https://github.com/PSCostaM/TF_MachineLearning_u201912086_u20201c579_u202010122/assets/48858434/f052564b-4b5c-4a76-bea0-c74ea4dcdfd7)

La imagen presentada fue obtenida del algoritmo encontrado en [TF_GAN/data/gen_images.py](https://github.com/PSCostaM/TF_MachineLearning_u201912086_u20201c579_u202010122/blob/master/TF_GAN/data/gen_images.py)

### Printing Plan

El software utilizado para la presentación de un archivo STL, generación del modelo con sus respectivos soportes y configuración de impresión 3D es prusa-slicer.

![image](https://github.com/PSCostaM/TF_MachineLearning_u201912086_u20201c579_u202010122/assets/48858434/ad2adde4-f9b0-4b82-892d-edcd72b3cd7f)

Tras la importación de un .STL la visualización del modelo fue inmediata y ya tenía los soportes generados. Después de esto tuvimos que configurar el material, especificar las cualidades de la impresora a usar para obtener los gramos totales y el tiempo aproximado de impresión. Después de este proceso de configuración, se generaba un archivo .gcode el cuál iba a ser transferido a un usb para ser conectado a la impresora y empezar con el proceso de impresión.

![image](https://github.com/PSCostaM/TF_MachineLearning_u201912086_u20201c579_u202010122/assets/48858434/3a476d6c-6279-4ab8-8173-77c7bc740add)


## Milestone 5: TA4
## Methodology

### Model Architecture

El modelo a utilizar está compuesto por un generador, el cual se encarga de generar muestras de imágenes con la intención de ser indistinguibles a las reales. Por otra parte, el discriminador tomará como entrada tanto las muestras de imágenes generadas como las del dataset con imágenes reales para tratar de distinguir las muestras reales de las generadas.



![Arquitectura-Diagrama](https://github.com/PSCostaM/TF_MachineLearning_u201912086_u20201c579_u202010122/assets/89089765/237fbd1b-bc75-4312-8dac-6becf678744e)

## Training Setup

Todo método de entrenamiento y generación de modelo fue hecha en una laptop personal. Las specs de esta fueron
- Procesador: Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz   2.59 GHz
- Ram Instalada: 32.0 GB (16gb 2933Mhz * 2) 
- GPU: NVIDIA GeForce GTX 1650 4Gb

Pseudocode algoritmo de entrenamiento 
```
# Import necessary libraries and modules

# Define a parser to handle command-line arguments
args = parse_command_line_arguments()

# Set device to GPU if available, else use CPU
device = determine_device()

# Load dataset
dataset = load_dataset(args.dataset)

# Create a dataloader
dataloader = create_dataloader(dataset, args.batch_size, shuffle=True, num_workers=args.workers)

# Function to initialize the neural renderer
def renderer_init(m):
    # Initialize weights of Conv layers using Xavier normal initialization

# Create a neural renderer model and move it to the specified device
renderer = create_neural_renderer_model(args).move_to(device)

# Load pre-trained weights if available, otherwise initialize weights
load_or_initialize_weights(renderer, 'weights/nr.pt')

# Define loss functions
criterion = BinaryCrossEntropyLoss()
l2 = MeanSquaredErrorLoss(reduction='sum')

# Define optimizer for the neural renderer
optimizerR = AdamOptimizer(renderer.parameters(), lr=args.nr_lr, betas=(args.beta1, 0.999))

# Initialize an empty list to store images
img_list = []

# Main training loop
for epoch in range(args.num_epochs):
    for i, data in enumerate(dataloader):
        # Update the neural renderer network
        renderer.zero_gradients()
        voxels = get_voxels_from_data(data).move_to(device)
        nr = renderer.render(voxels)
        ots = render_with_off_the_shelf_renderer(voxels, device)
        errR = calculate_l2_loss(nr, ots)
        calculate_gradients(errR)
        update_neural_renderer(optimizerR)
        
        # Output training statistics
        if i % 50 == 0:
            print_training_stats(epoch, args.num_epochs, i, len(dataloader), errR)
        if i % 200 == 0:
            add_image_to_list(nr.detach().cpu()[0, 0].numpy() * 255)

# Save trained neural renderer weights
save_trained_weights(renderer, 'weights/nr.pt')

# Display animated images using matplotlib
display_images_animation(img_list)
```

### 3D Printing

El proceso de impresión de nuestro modelo tomó alrededor de 17 minutos. Al ser un modelo de tamaño reducido y con grandes espacios en la zona inferior, requirió un soporte de similares proporciones a nuestro modelo.

![impresora3d](https://github.com/PSCostaM/TF_MachineLearning_u201912086_u20201c579_u202010122/assets/89089765/c5d84e1f-fb71-4f36-9681-fc9a2d911af9)

## Final Milestone: TF

### Results

Tras 8 horas de entrenamiento los pesos generados serán utilizados para la generación de archivos .binvoxels los cuales después son utilizados en una función para convertirlos en .STL y luego mostrarlos en cualquier software de visualización. 

![image](https://github.com/PSCostaM/TF_MachineLearning_u201912086_u20201c579_u202010122/assets/48858434/089673f7-7e38-4e7a-add0-dbcf1bcd973f)



### Conclusiones

- Generación Inicial con Potencial Mejorable: Durante el entrenamiento de 8 horas, se logró generar un modelo 3D a partir de imágenes 2D, representando un cubo con ruido o imperfecciones. A pesar de estas limitaciones iniciales, se evidencia el potencial de la Generative Adversarial Network (GAN) para crear representaciones tridimensionales, sugiriendo oportunidades de mejora y refinamiento con entrenamiento adicional o ajustes en la arquitectura del modelo.

- Desafíos en la Transformación de Datos: La transformación de datos desde archivos .binvoxels a imágenes 2D para su procesamiento presentó desafíos significativos. A pesar de ello, la visualización y manipulación de estos datos en diferentes posiciones permitió comprender cómo se representaban los objetos en 3D a través de imágenes 2D, siendo fundamental para el entrenamiento del modelo.

- Aplicaciones Prácticas en la Impresión 3D: La capacidad de generar modelos 3D a partir de imágenes 2D proporciona una herramienta valiosa para la impresión 3D. La representación fiel de objetos tridimensionales desde imágenes puede tener aplicaciones en diseño, prototipado rápido y fabricación, permitiendo la generación de modelos que son directamente utilizables en entornos de impresión 3D.

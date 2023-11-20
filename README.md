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

![image](https://github.com/PSCostaM/TF_MachineLearning_u201912086_u20201c579_u202010122/assets/48858434/ae2664c7-e455-4f3b-a1a0-1f32b0518113)


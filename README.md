<div align="center">

# Calculation and Simulation of Magnetic Braking Deceleration in a Drop Tower Ride

##### Python simulation of a free-fall mechanical game that is magnetically slowed down. Maxwell's laws, Biot-Savart law, and fourth-order Runge-Kutta were used. 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

</div>

## Overview

This project focuses on simulating the descent of a gondola as part of a free-fall amusement park ride, with a specific interest in understanding the deceleration achieved through magnetic braking.

The methodology incorporates the application of the Biot-Savart law and Maxwell's laws, enhanced by utilizing the Runge-Kutta numeric method. This computational approach allows for the calculation of the magnetic field surrounding the gondola and its interaction with the magnetic field present in the ground, providing insights into the deceleration process during the gondola's descent.

The simulation was implemented in Python, leveraging matplotlib and numpy to develop three distinct programs. 

## Repository Contents

### Main Scripts


1. **HeatMapAndNumericalApproximations.py**
   - *Description:* This program calculates and visually represents the magnetic field of a ring using streamplot, accompanied by a heatmap.

2. **ComparingMagneticFieldInEachComponent.py**
   - *Description:* This program program generates a comparative graph illustrating the magnetic field in each component (x, y, and z).

3. **AnimationOfTheGondolaFalling.py**
   - *Description:* This program animates the gondola's descent, showcasing the magnetic braking process until the point of complete stoppage.

## Usage 

Follow these steps to get the project up and running on your local machine.

### Prerequisites

Make sure you have the following installed on your machine:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/)
- [Numpy](https://numpy.org/)

### Installation

- Clone the repository:

    ```bash
    git clone https://github.com/HumbertoBM2/Calculation-and-Simulation-of-Magnetic-Braking-Deceleration-in-a-Drop-Tower-Ride
    ```

- Navigate to the project directory:

    ```bash
    cd Calculation-and-Simulation-of-Magnetic-Braking-Deceleration-in-a-Drop-Tower-Ride
    ```

- Open a terminal and run one of the following commands:

    ```bash
    python ./HeatMapAndNumericalApproximations.py
    ```

    ```bash
    python ./ComparingMagneticFieldInEachComponent.py
    ```

    ```bash
    python ./AnimationOfTheGondolaFalling.py
    ```
Each application will display an interactive menu guiding you through each step. Follow the instructions of each menu and enjoy.

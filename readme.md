# Student Performance Prediction System
This project is a Django-based web application that predicts students' final grades and categorizes their performance based on multiple features such as attendance, previous grades, study hours, assignment scores, and participation in extracurricular activities. The system uses a machine learning model trained with a genetic algorithm to provide accurate predictions.


### Genetic Algorithm
A Genetic Algorithm (GA) is a search heuristic inspired by the process of natural selection. It belongs to the larger class of evolutionary algorithms (EA), which generate solutions to optimization problems using techniques inspired by biological evolution, such as inheritance, mutation, selection, and crossover. Genetic algorithms are particularly useful for solving complex optimization problems where traditional methods might be inefficient or fail to provide optimal solutions.

#### Key Concepts

1. **Population**: A set of candidate solutions to the optimization problem. Each candidate solution is referred to as an individual or a chromosome.

2. **Genes**: Components of the candidate solutions that encode specific characteristics of the solution.

3. **Fitness Function**: A function that evaluates and assigns a fitness score to each individual based on how well it solves the problem. The higher the fitness score, the better the solution.

4. **Selection**: The process of choosing individuals from the population to create offspring for the next generation. Individuals with higher fitness scores are more likely to be selected.

5. **Crossover (Recombination)**: A genetic operator that combines two parent individuals to produce offspring. This mimics biological reproduction and helps to explore new areas of the solution space.

6. **Mutation**: A genetic operator that introduces random changes to an individual’s genes. This helps to maintain genetic diversity within the population and prevents premature convergence on suboptimal solutions.

7. **Generations**: Iterative cycles in which a population evolves. In each generation, selection, crossover, and mutation are applied to create a new population.

#### Process

1. **Initialization**: Generate an initial population of individuals randomly.

2. **Evaluation**: Calculate the fitness of each individual in the population using the fitness function.

3. **Selection**: Select individuals based on their fitness scores. Common selection methods include roulette wheel selection, tournament selection, and rank-based selection.

4. **Crossover**: Pair selected individuals to exchange genetic information and create offspring. Common crossover methods include single-point crossover, multi-point crossover, and uniform crossover.

5. **Mutation**: Apply random changes to the offspring's genes with a certain probability.

6. **Replacement**: Form a new population by replacing some or all individuals from the previous generation with the new offspring.

7. **Termination**: Repeat the evaluation, selection, crossover, mutation, and replacement steps for a specified number of generations or until a convergence criterion is met.

8. **Solution**: The best individual in the final population is considered the optimal solution to the problem.

#### Advantages

- **Exploration of Solution Space**: Genetic algorithms can efficiently explore large and complex solution spaces.
- **Adaptability**: They can adapt to changes in the problem environment.
- **Parallelism**: GA can evaluate multiple candidate solutions simultaneously, making them suitable for parallel processing.

#### Applications

Genetic algorithms are applied in various fields, including:

- **Optimization Problems**: Scheduling, routing, and resource allocation.
- **Machine Learning**: Hyperparameter tuning, feature selection, and neural network optimization.
- **Engineering**: Design optimization, control systems, and robotics.
- **Economics**: Portfolio optimization and market modeling.
- **Bioinformatics**: Protein folding and gene expression analysis.
- 
## Features

- Upload CSV files containing student data for predictions.
- Predict final grades based on input features.
- Categorize student performance into "Doing Well" and "Needs Improvement".
- Display results in interactive plots and tables.
- Mobile-responsive interface with modern styling using Tailwind CSS.

## Requirements

- Python 3.7+
- Django 3.2+
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Plotly

## Installation

1. Clone the repository:

```sh
git clone https://github.com/Levi-Chinecherem/genAlgorithm.git
cd genAlgorithm
```

2. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```sh
pip install -r requirements.txt
```

4. Apply migrations:

```sh
python manage.py migrate
```

5. Run the development server:

```sh
python manage.py runserver
```

## Usage

1. Navigate to the application URL (e.g., `http://127.0.0.1:8000/`).
2. Upload a CSV file containing student data with the following columns:
    - Attendance
    - Previous_Grade
    - Study_Hours
    - Assignment_Score
    - Extracurricular
3. View the predicted final grades and performance categorization.
4. Explore the results in the provided plots and tables.

## Project Structure

- `main_p/`: Main project directory containing settings and configuration files.
- `upload/`: Django app for handling file uploads and predictions.
- `templates/`: HTML templates for rendering the web pages.
- `static/`: Static files (CSS, JS) for styling and client-side functionality.
- `models/`: Machine learning models and related scripts.
- `media/`: Temporary storage for uploaded files (configured to save only one file at a time).

## Model Training

The machine learning model is trained using a genetic algorithm to optimize a linear regression model. The dataset includes a mix of good and bad performance data to avoid bias. The genetic algorithm helps in evolving the model over generations to find the best coefficients for prediction. The model is saved as `best_model.pkl` and loaded by the Django application for making predictions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact:

- **Levi Chinecherem Chidi**: [Email](mailto:levi.chinecherem@yahoo.com)
- **GitHub**: [Levi_Chinecherem](https://github.com/Levi-Chinecherem)

## Acknowledgments

- The project uses Tailwind CSS for modern styling and responsiveness.
- The machine learning model is built using Scikit-learn.
- Plots are generated using Matplotlib, Seaborn, and Plotly.



#### Conclusion

Genetic algorithms provide a robust and flexible approach to solving optimization problems by mimicking the process of natural selection. Their ability to explore a wide range of solutions and adapt to various problem domains makes them a powerful tool in both academic research and practical applications. By leveraging the principles of evolution, genetic algorithms can find near-optimal solutions where traditional methods might struggle.
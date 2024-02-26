# query_generator_app
A Streamlit and LangChain powered application for dynamically generating SQL queries. Designed to simplify database interactions through natural language inputs, this app leverages cutting-edge AI to translate user queries into executable SQL code. Perfect for analysts, developers, and anyone looking to interact with databases more intuitively.

## Getting Started

Welcome to `query_generator_app`, a Streamlit and LangChain powered tool designed to generate SQL queries from natural language inputs. Follow these steps to get the application up and running on your local machine.
### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Poetry for dependency management
### Installation 
1. **Clone the repository** 

First, clone the `query_generator_app` repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/query_generator_app.git
cd query_generator_app
``` 
2. **Install dependencies** 

Use Poetry to install the required dependencies. If you don't have Poetry installed, refer to the [Poetry documentation]()  for installation instructions.

```bash
poetry install
```
### Running the Application

After installing the dependencies, you can start the application using Streamlit. Run the following command in the terminal:

```bash
poetry run streamlit run app/main.py
```



This command launches the Streamlit server and opens the application in your default web browser. If the browser does not open automatically, you can access the app by navigating to the URL provided in the terminal output, typically `http://localhost:8501`.
### Using the Application

With the application running, you can start generating SQL queries by entering natural language descriptions of your desired query into the input field. The app uses LangChain to interpret your input and generate the corresponding SQL query, which you can then review and use as needed.---

Feel free to customize these instructions based on the specific requirements or additional features of your application.

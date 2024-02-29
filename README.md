# query_generator_app
A Streamlit and LangChain powered application for dynamically generating SQL queries. Designed to simplify database interactions through natural language inputs, this app leverages cutting-edge AI to translate user queries into executable SQL code. Perfect for analysts, developers, and anyone looking to interact with databases more intuitively.

## Getting Started

Follow these steps to get the application up and running on your local machine.
### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Poetry for dependency management
### Installation 
1. **Clone the repository** 

    Clone the `query_generator_app` repository to your local machine using Git:

    ```bash
    git clone git@github.com:knishioka/query_generator_app.git
    cd query_generator_app
    ``` 
1. **Install dependencies** 
    Use Poetry to install the required dependencies:

    ```bash
    poetry install
    ```

1. **Install pre-commit hooks**
    To ensure your codebase remains clean and follows the defined coding standards, install pre-commit hooks by running:

    ```bash
    pre-commit install
    ```
    This command sets up pre-commit hooks that will automatically run specified tasks (like linting and tests) before each commit.

### Environment Variables

To run the application smoothly and securely, you need to set up certain environment variables using a `.env` file.
#### Setting Up Your `.env` File 
1. In the root directory of the project, create a file named `.env`. 
1. Add the necessary environment variables to the `.env` file. For example, to set up the OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

Additionally, to enable LangSmith tracing for enhanced debugging and insights, include the following settings:

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="your_langchain_api_key"
LANGCHAIN_PROJECT="your_project"
```

Replace `your_langchain_api_key` with your actual LangChain API key and `your_project` with your project name.

**Note:**  The `.env` file is included in the `.gitignore` to prevent sensitive information from being committed to version control.
### Running the Application

After setting up the environment variables, start the application using Streamlit:

```bash
poetry run streamlit run app/main.py
```



This command launches the Streamlit server and opens the application in your default web browser. If the browser does not open automatically, navigate to the URL provided in the terminal output, typically `http://localhost:8501`.
## Using the Application

With the application running, enter natural language descriptions of your desired query into the input field. The app uses LangChain to interpret your input and generate the corresponding SQL query, which you can then review and use as needed.

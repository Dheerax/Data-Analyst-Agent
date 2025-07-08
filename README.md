# 🤖 Aether Agent - AI Data Analysis Assistant

A powerful AI-driven data analysis agent built with LangChain and Streamlit that converts natural language queries into intelligent data insights.

## ✨ Features

- **Natural Language Queries**: Ask questions about your data in plain English
- **Intelligent SQL Generation**: Automatically converts queries to SQL and executes them
- **Interactive Web Interface**: Clean Streamlit UI for easy data upload and analysis
- **Multiple File Formats**: Support for CSV files with plans for Excel integration
- **Real-time Analysis**: Get instant insights from your uploaded datasets
- **Verbose Mode**: See the AI's reasoning process step-by-step

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google API Key (for Gemini LLM)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "s:\Python\AI Agents\Rebuild"
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables: **
   Paste Your Google Gemini API key in the .env file
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run ui/app.py
   ```

## 📁 Project Structure

```
aether_agent/
├── core/                   # Core agent logic
│   ├── __init__.py
│   ├── llm.py              # LLM configuration
│   ├── db.py               # Database setup
│   ├── chains.py           # LLMChains & prompts
│   └── agent.py            # Main agent logic
├── ui/                     # Streamlit frontend
│   ├── __init__.py
│   └── app.py              # UI entry point
├── utils/                  # Helper utilities
│   ├── __init__.py
│   ├── preprocess.py       # Data preprocessing
│   └── file_handler.py     # File handling utilities
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables
└── README.md              # Project documentation
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key | Yes |

### LLM Configuration

The agent uses Google's Gemini-1.5-Flash model by default. You can modify the configuration in `core/llm.py`:

```python
def get_llm(model: str = "gemini-1.5-flash", temperature: float = 0.1):
    # Configuration options
```

## 💡 Usage Examples

### Basic Data Analysis
```
Upload a CSV file and ask questions like:
- "What's the average salary by department?"
- "Show me the top 5 customers by revenue"
- "How many employees are there in each location?"
```

### Advanced Queries
```
- "Find correlations between age and performance ratings"
- "What percentage of sales come from each region?"
- "Show me trends in quarterly revenue"
```

## 🛠️ Core Components

### DataAnalysisAgent
The main agent class that orchestrates data analysis:
- **Database Setup**: Converts DataFrames to SQLite
- **Agent Creation**: Initializes LangChain SQL agent
- **Query Processing**: Handles natural language queries

### LLM Configuration
Manages Large Language Model setup:
- Google Gemini integration
- Configurable temperature and model parameters
- Environment variable management

### Database Manager
Handles data storage and retrieval:
- Temporary SQLite database creation
- DataFrame to SQL conversion
- Query execution and results

## 🔧 Development

### Adding New Features

1. **Core Logic**: Add new functionality in the `core/` directory
2. **UI Components**: Extend the Streamlit interface in `ui/app.py`
3. **Utilities**: Add helper functions in the `utils/` directory

### Testing

```bash
# Run the agent with verbose mode to see reasoning
streamlit run ui/app.py
# Upload a test CSV and ask questions
```

## 📦 Dependencies

### Core Dependencies
- `langchain>=0.1.0` - LLM framework
- `langchain-google-genai>=1.0.0` - Google Gemini integration
- `streamlit>=1.28.0` - Web interface
- `pandas>=2.0.0` - Data manipulation
- `sqlalchemy>=2.0.0` - Database toolkit

### Optional Dependencies
- `openpyxl>=3.1.0` - Excel file support
- `matplotlib>=3.7.0` - Data visualization
- `plotly>=5.15.0` - Interactive charts
- `jupyter>=1.0.0` - Development notebooks

## 🚧 Roadmap

- [ ] Excel file support
- [ ] Data visualization capabilities
- [ ] Export analysis results
- [ ] Multiple LLM provider support
- [ ] Enhanced error handling
- [ ] Batch query processing
- [ ] Data preprocessing utilities

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

If you encounter any issues or have questions:

1. Check the troubleshooting section below
2. Open an issue on GitHub
3. Review the verbose output for debugging

### Troubleshooting

**"No module named core" error:**
- Ensure you're running from the project root directory
- Add `__init__.py` files to make directories proper Python packages

**API Key issues:**
- Verify your `.env` file is in the project root
- Check that `GOOGLE_API_KEY` is set correctly
- Ensure no extra spaces or quotes in the `.env` file

**Import errors:**
- Update LangChain imports if using newer versions
- Install all required dependencies from `requirements.txt`

---

Built with ❤️ using LangChain, Streamlit, and Google Gemini

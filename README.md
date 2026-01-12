# Contoso RAG Assistant Demo

A comprehensive Streamlit application showcasing **Retrieval-Augmented Generation (RAG)** capabilities using Azure OpenAI and Azure AI Search. This demo features two intelligent assistants that provide accurate, grounded responses from indexed enterprise data.

**Created by:** Aparna Rajawat

## 🚀 Features

- 🛍️ **Product Assistant** - Intelligent product search and recommendations
- 📚 **Manual Assistant** - Instant access to product documentation and guides
- 🔍 **Vector Search** - Powered by Azure AI Search with semantic capabilities
- 💬 **Context-Aware Conversations** - Maintains chat history for natural interactions
- 🎯 **Grounded Responses** - All answers are based on indexed enterprise data
- 🔒 **Secure Configuration** - Environment-based secrets management

## 📋 Prerequisites

- Python 3.8 or higher
- Azure OpenAI subscription with deployed models
- Azure AI Search service with indexed data
- Git (for cloning the repository)

## 🛠️ Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/Appy-success/Multi-Rag.git
cd Multi-Rag
```

### Step 2: Create Python Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

1. Copy the example environment file:
```bash
copy .env.example .env
```

2. Edit `.env` file with your Azure credentials:
```env
AZURE_OPENAI_ENDPOINT="your-azure-openai-endpoint"
AZURE_OPENAI_API_KEY="your-azure-openai-api-key"
CHAT_MODEL="your-chat-model-deployment-name"
EMBEDDING_MODEL="your-embedding-model-deployment-name"
SEARCH_ENDPOINT="your-azure-search-endpoint"
SEARCH_KEY="your-azure-search-admin-key"
INDEX_NAME="your-default-index-name"
product_index="your-product-index-name"
maunal_index="your-manual-index-name"
```

### Step 5: Create Search Indexes from Local Data

The application includes pre-built Jupyter notebooks to create Azure AI Search indexes from your local data files. This step is essential for setting up the RAG (Retrieval-Augmented Generation) functionality.

#### 📋 Prerequisites for Index Creation
- Azure AI Search service deployed
- Azure OpenAI service with embedding model deployed
- Valid credentials configured in `.env` file

#### 🔧 Creating Indexes Using Jupyter Notebooks

##### 1. **Product Search Index** (`create-azure-search.ipynb`)
This notebook creates a searchable index from your product catalog data:

**Location:** [`data/product_info/create-azure-search.ipynb`](data/product_info/create-azure-search.ipynb)

**Purpose:** 
- Processes the `products.csv` file containing product information
- Creates vector embeddings for product descriptions
- Sets up Azure AI Search index with semantic search capabilities

**Steps:**
1. Open the notebook in Jupyter or VS Code
2. Ensure your `.env` file contains valid Azure credentials
3. Run all cells sequentially
4. The notebook will automatically:
   - Load product data from `products.csv`
   - Generate embeddings using Azure OpenAI
   - Create and populate the search index
   - Verify index creation and document count

##### 2. **Manual Documentation Index** (`contoso-manuals-index.ipynb`)
This notebook creates a searchable index from product manuals and documentation:

**Location:** [`data/manual_info/contoso-manuals-index.ipynb`](data/manual_info/contoso-manuals-index.ipynb)

**Purpose:**
- Processes all Markdown files in the `manuals/` folder
- Creates chunked embeddings for better retrieval
- Enables semantic search across product documentation

**Steps:**
1. Place your manual files (`.md` format) in `data/manual_info/manuals/`
2. Open the notebook in your preferred environment
3. Execute all cells in order
4. The notebook will:
   - Scan all manual files in the directory
   - Process and chunk the content for optimal search
   - Generate embeddings and create the search index
   - Validate the index with sample queries

#### 📂 Data Structure Requirements

**For Product Index:**
```
data/product_info/
├── create-azure-search.ipynb
└── products.csv (your product catalog)
```

**For Manual Index:**
```
data/manual_info/
├── contoso-manuals-index.ipynb
└── manuals/
    ├── product_info_1.md
    ├── product_info_2.md
    └── ... (your manual files)
```

#### ✅ Verification Steps

After running the notebooks, verify your indexes:

1. **Check Azure Portal:** Navigate to your Azure AI Search service to confirm indexes are created
2. **Test Search Queries:** Use the Azure Search Explorer to test sample queries
3. **Run the Application:** Start the Streamlit app and test both assistants

#### 🔍 Index Configuration Details

Both notebooks create indexes with:
- **Vector search capabilities** for semantic similarity
- **Keyword search** for exact matches
- **Hybrid search** combining both approaches
- **Chunking strategies** optimized for RAG retrieval

#### 📝 Additional Setup Notes

1. **Customer Data Index** (Optional): Use `data/customer_info/create-cosmos-db.ipynb` if you need customer information storage in Cosmos DB
2. **Environment Variables:** Ensure all required variables are set in your `.env` file before running notebooks
3. **Model Dependencies:** Both notebooks require access to your deployed embedding model in Azure OpenAI

## 🚀 Running the Application

### Option 1: Streamlit Web App (Recommended)
```bash
streamlit run app.py
```
The application will open in your browser at `http://localhost:8501`

### Option 2: Command Line Interface
```bash
python main.py
```

## 📖 Usage Guide

### Using the Streamlit App

1. **Navigate**: Use the sidebar to switch between "Product Assistant" and "Manual Assistant"
2. **Ask Questions**: Type your questions in the chat input box
3. **Get Responses**: The AI will search indexed data and provide grounded answers
4. **Continue Conversations**: The app maintains chat history for context-aware follow-ups
5. **Clear Chat**: Use the "Clear Chat" button to reset conversation history

### Example Queries

**Product Assistant:**
- "Show me tents available in your catalog"
- "What backpacks do you have under $100?"
- "Compare the TrailMaster tent with other camping gear"

**Manual Assistant:**
- "How do I set up the TrailMaster X4 Tent?"
- "What is the waterproof rating of the tent?"
- "Does the backpack have hydration system compatibility?"

## 📁 Project Structure

```
Multi-Rag/
├── app.py                    # Main Streamlit application
├── main.py                   # Command-line interface
├── rag-app.py               # Original RAG implementation
├── product.prompty          # Product assistant prompt template
├── manual.prompty           # Manual assistant prompt template
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
├── DEMO_EXAMPLES.md        # Demo examples and usage guide
├── SOCIAL_MEDIA_POST.md    # Social media promotion templates
└── data/                   # Data files and notebooks
    ├── customer_info/      # Customer data and Cosmos DB setup
    ├── product_info/       # Product data and search index setup
    └── manual_info/        # Manual documentation and index setup
```

## 🔧 Configuration Details

### Required Azure Resources

1. **Azure OpenAI Service**
   - GPT model deployment (e.g., gpt-4, gpt-35-turbo)
   - Text embedding model (e.g., text-embedding-ada-002)

2. **Azure AI Search Service**
   - Search indexes for your data
   - Vector search capabilities enabled

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI service endpoint | `https://your-service.openai.azure.com/` |
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key | `your-api-key` |
| `CHAT_MODEL` | Deployed chat model name | `gpt-4` |
| `EMBEDDING_MODEL` | Deployed embedding model name | `text-embedding-ada-002` |
| `SEARCH_ENDPOINT` | Azure AI Search endpoint | `https://your-search.search.windows.net/` |
| `SEARCH_KEY` | Azure AI Search admin key | `your-search-key` |
| `product_index` | Product data index name | `contoso-products` |
| `maunal_index` | Manual data index name | `contoso-manuals-index` |

## 🎯 Demo & Training

This application is perfect for:
- **Training Sessions**: Demonstrating RAG patterns and best practices
- **Client Demos**: Showcasing enterprise AI search capabilities
- **Workshops**: Hands-on learning with real data and queries
- **Technical Presentations**: Illustrating Azure AI integration

Use the examples in `DEMO_EXAMPLES.md` for structured demonstrations.

## 🔒 Security Best Practices

- ✅ Never commit `.env` files to version control
- ✅ Use environment variables for all sensitive data
- ✅ Regularly rotate API keys and access tokens
- ✅ Use Azure Key Vault for production deployments
- ✅ Implement proper access controls on Azure resources

## 🛠️ Troubleshooting

### Common Issues

1. **Import Errors**: Ensure virtual environment is activated and dependencies are installed
2. **Authentication Errors**: Verify Azure credentials in `.env` file
3. **Search Errors**: Confirm Azure AI Search indexes exist and contain data
4. **Model Errors**: Check that specified models are deployed in Azure OpenAI

### Debug Mode

Run with debug logging:
```bash
streamlit run app.py --logger.level debug
```

## 📚 Additional Resources

- [Azure OpenAI Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/)
- [Azure AI Search Documentation](https://docs.microsoft.com/azure/search/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [RAG Pattern Best Practices](https://learn.microsoft.com/azure/ai-services/openai/concepts/use-your-data)

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements. For major changes, please open an issue first to discuss proposed modifications.

## 📝 License

This project is provided as-is for educational and demonstration purposes.

---

**Created with ❤️ by Aparna Rajawat**

*Showcasing the power of Retrieval-Augmented Generation with Azure AI*
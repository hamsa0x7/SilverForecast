# Kaggle MCP Setup Guide

## Why Use Kaggle MCP?

The Kaggle MCP (Model Context Protocol) server allows AI agents to directly access Kaggle datasets without manual downloads or API key management.

**Benefits:**
- ✅ No manual API key setup
- ✅ Direct dataset access from AI
- ✅ Simplified data collection in Phase 1
- ✅ Better for automation

---

## Setup Instructions

### Option 1: Gemini CLI (Recommended)

```bash
gemini mcp add --transport http kaggle https://www.kaggle.com/mcp
```

### Option 2: Manual Configuration

Add to your `.gemini/settings.json`:

```json
{
  "mcpServers": {
    "kaggle": {
      "httpUrl": "https://www.kaggle.com/mcp"
    }
  }
}
```

---

## Using Kaggle MCP in DS Projects

Once configured, the AI can access datasets directly:

```python
# Instead of manual download script:
# kaggle datasets download -d {dataset_name}

# AI automatically uses MCP to:
# 1. List available datasets
# 2. Read dataset metadata
# 3. Download files to data/raw/
```

---

## For Silver Forecasting Project

**Dataset:** `muhammadaammartufail/silver-prices-10-year-data-and-2026-forecast`

**After setup, the AI will:**
1. Use MCP to locate the dataset
2. Read the CSV files directly
3. Save to `data/raw/` automatically

---

## Verification

To verify Kaggle MCP is working:

```bash
gemini mcp list
# Should show "kaggle" in the list
```

---

**Next:** Once Kaggle MCP is configured, restart Phase 1 (Data Collection) and the AI will use it automatically!

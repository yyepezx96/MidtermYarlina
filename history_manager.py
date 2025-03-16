import pandas as pd

# Initialize the history DataFrame (load from CSV if exists)
history_file = 'history.csv'

def load_history():
    try:
        return pd.read_csv(history_file)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Operation", "Result"])

# Load or initialize history data
history_df = load_history()

def add_to_history(operation, result):
    global history_df
    new_entry = pd.DataFrame([[operation, result]], columns=["Operation", "Result"])

# Filter out any empty or NA rows before concatenating
    new_entry = new_entry.dropna(axis=1, how='all')   
    history_df = pd.concat([history_df, new_entry], ignore_index=True)
    history_df.to_csv(history_file, index=False)
    print(f"History updated with operation: {operation}, result: {result}")

def show_history():
    """Displays the entire calculation history"""
    print(history_df)

def clear_history():
    global history_df
    history_df = pd.DataFrame(columns=["Operation", "Result"])
    print("History cleared.")

def save_history(filename):
    history_df.to_csv(filename, index=False)
    print(f"History saved to {filename}")

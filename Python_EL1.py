import time
import random
import os

# --- 1. THE INVENTORY (Our Database) ---
# We use emojis to make it visual and fun
inventory = {
    "Apples": 20,
    "Bananas": 15,
    "Milk": 8,
    "Bread": 10
}

THRESHOLD = 5  # The danger zone limit

# --- 2. COLOR CODES (Creative Design) ---
# These weird codes tell the terminal to change color.
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m" # Resets color back to white
BOLD = "\033[1m"

def clear_screen():
    # Clears the console so it looks like a fixed dashboard
    os.system('cls' if os.name == 'nt' else 'clear')

def display_dashboard():
    while True: # This Loop makes it "Real Time"
        clear_screen()
        
        print(f"{BOLD}--- LIVE WAREHOUSE MONITOR ---{RESET}")
        print("Watching stock levels in real-time...\n")
        
        all_stock_healthy = True

        # Check every item in our list
        for item, count in inventory.items():
            if count <= THRESHOLD:
                # DANGER MODE: Print in RED with Warning Signs
                print(f"{RED} LOW STOCK ALERT: {item} - Only {count} left!{RESET}")
                all_stock_healthy = False
            else:
                # SAFE MODE: Print in GREEN
                print(f"{GREEN} {item} : {count} units{RESET}")

        print("\n---------------------------------------")
        
        if all_stock_healthy:
            print("Status: All Systems Normal")
        else:
            print(f"{RED}Status: ACTION REQUIRED! Restock needed.{RESET}")

        # --- 3. SIMULATE A SALE (The "Real Time" Effect) ---
        # Randomly pick an item and sell it
        item_sold = random.choice(list(inventory.keys()))
        
        # Only decrease if we have stock
        if inventory[item_sold] > 0:
            inventory[item_sold] -= 1
            print(f"\n🛒 A customer just bought: {item_sold}")
        
        # Wait 2 seconds before the next update
        time.sleep(2)

# Run the dashboard
if __name__ == "__main__":
    display_dashboard()
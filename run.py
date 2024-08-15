import time
def main():
    print("Starting simulation...")
    
    for step in range(3):
        print(f"Running step {step + 1}")
        start_time = time.time()
        model.step()
        end_time = time.time()
        print(f"Step {step + 1} completed in {end_time - start_time:.2f} seconds")
        
    print("Simulation complete.")

if __name__ == "__main__":
    main()

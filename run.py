from model.data_replication_model import DataReplicationModel

def main():
    # Initialize the model with a specified number of agents
    num_agents = 6
    model = DataReplicationModel(num_agents=num_agents)

    # Run the simulation for a certain number of steps
    for step in range(10):
        print(f"Running step {step + 1}")
        model.step()

    print("Simulation complete.")

if __name__ == "__main__":
    main()

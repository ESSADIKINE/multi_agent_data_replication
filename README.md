# Multi-Agent Data Replication System

This project simulates a multi-agent system (MAS) that optimizes the distribution and replication of data in a distributed MongoDB environment. The system is built using Python, the `mesa` framework for agent-based modeling, and MongoDB as the underlying database.

## Table of Contents
- [Project Overview](#project-overview)
- [Key Components](#key-components)
- [Getting Started](#getting-started)
- [Running the Project](#running-the-project)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [License](#license)

## Project Overview

The goal of this project is to demonstrate how multiple intelligent agents can collaborate to manage data distribution and replication in a distributed database system. The system is designed to:
- Optimize data distribution across multiple database nodes.
- Ensure data redundancy and reliability through replication.
- Monitor the performance and state of the system.

## Key Components

- **Agents:**
  - **DataManagerAgent:** Manages where data should be stored across the database nodes.
  - **ReplicationAgent:** Handles replicating data across nodes to ensure consistency.
  - **MonitoringAgent:** Monitors the system's performance and tracks data distribution.

- **MongoDB Nodes:** 
  - The system simulates three MongoDB nodes (`node1_db`, `node2_db`, `node3_db`) where data is stored, replicated, and managed.

- **Web Interface (Flask):**
  - Provides a user-friendly interface to run the simulation and view the distribution of data across nodes.

## Getting Started

### Prerequisites

- Python 3.x
- MongoDB running locally on `localhost:27017`
- Flask and other dependencies (listed in `requirements.txt`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ESSADIKINE/multi_agent_data_replication.git
   cd multi_agent_data_replication

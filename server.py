from agent import BuildingAgent, TrafficLightAgent, CarAgent, MotorcycleAgent, TruckAgent
from model import IntersectionModel
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer

def intersectionPortrayal(agent):
    if agent is None:
        return

    portrayal = {"Filled": "true"}

    if isinstance(agent, BuildingAgent):
        portrayal["Shape"] = "rect"
        portrayal["w"] = 0.8
        portrayal["h"] = 0.8
        portrayal["Color"] = "#8B4513"  # Brown for buildings
        portrayal["Layer"] = 1

    elif isinstance(agent, TrafficLightAgent):
        portrayal["Shape"] = "rect"
        portrayal["w"] = 0.6
        portrayal["h"] = 0.6
        portrayal["Color"] = "green" if agent.state == "green" else "red" if agent.state == "red" else "yellow"
        portrayal["Layer"] = 2

    elif isinstance(agent, CarAgent):
        portrayal["Shape"] = "circle"
        portrayal["r"] = 0.5
        portrayal["Color"] = "#0000FF" if agent.state == "happy" else "#FF0000"
        portrayal["Layer"] = 3

    elif isinstance(agent, MotorcycleAgent):
        portrayal["Shape"] = "circle"
        portrayal["r"] = 0.3  # Smaller radius for motorcycle
        portrayal["Color"] = "orange"  if agent.state == "happy" else "#FF0000"
        portrayal["Layer"] = 3

    elif isinstance(agent, TruckAgent):
        portrayal["Shape"] = "rect"
        portrayal["w"] = 0.7
        portrayal["h"] = 0.7
        portrayal["Color"] = "#800080" if agent.state == "happy" else "#FF0000"
        portrayal["Layer"] = 3

    return portrayal

# Create the CanvasGrid
grid = CanvasGrid(intersectionPortrayal, 23, 23, 500, 500)

# Create the ChartModule for displaying agent counts by approach
advance_chart = ChartModule(
    [
        {"Label": "Cooperative Advances", "Color": "Purple"},
        {"Label": "Competitive Advances", "Color": "Orange"},
        {"Label": "Neutral Advances", "Color": "Gray"}
    ],
    data_collector_name='datacollector'  # Must match the data collector in IntersectionModel
)

# Set up model parameters for the user interface
model_parameters = {
    "size": 23,
    "num_lights": 4,  # Number of traffic lights
    "num_cars": 10,  # Number of cars
    "num_motorcycles": 5,  # Number of motorcycles
    "num_trucks": 3  # Number of trucks
}

# Set up the ModularServer to run the simulation with the grid and advance chart
server = ModularServer(
    IntersectionModel,
    [grid, advance_chart],  # Include the grid and the single chart
    "Intersection Simulation with Advances Chart",
    model_parameters
)

server.port = 8521  # Default port
server.launch()

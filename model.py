from mesa import Model
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
import random
from agent import BuildingAgent, TrafficLightAgent, CarAgent, MotorcycleAgent, TruckAgent
from map import optionMap, startList, endList, Semaphores
from aStar import create_maximal_graph, astarComplete, manhattan_distance

class IntersectionModel(Model):
    def __init__(self, size, num_lights, num_cars, num_motorcycles=2, num_trucks=1):
        self.schedule = SimultaneousActivation(self)
        self.grid = MultiGrid(size, size, torus=False)
        self.num_lights = num_lights
        self.num_cars = num_cars
        self.num_motorcycles = num_motorcycles
        self.num_trucks = num_trucks
        self.current_time = 0
        self.current_id = 0
        self.G = create_maximal_graph(optionMap)
        self.running = True
        self.completedCars = 0
        self.traffic_lights = []
        self.light_index = 0  # Start cycling from the first traffic light

        # Advance counters by agent type
        self.cooperative_advances = 0
        self.competitive_advances = 0
        self.neutral_advances = 0

        # DataCollector to record advances by agent type
        self.datacollector = DataCollector(
            model_reporters={
                "Cooperative Advances": lambda m: sum(1 for a in m.schedule.agents if isinstance(a, (CarAgent, MotorcycleAgent, TruckAgent)) and a.agent_type == "cooperative"),
                "Competitive Advances": lambda m: sum(1 for a in m.schedule.agents if isinstance(a, (CarAgent, MotorcycleAgent, TruckAgent)) and a.agent_type == "competitive"),
                "Neutral Advances": lambda m: sum(1 for a in m.schedule.agents if isinstance(a, (CarAgent, MotorcycleAgent, TruckAgent)) and a.agent_type == "neutral"),
            }
        )



        middle_lane = size // 2
        self.create_buildings(size, middle_lane)
        self.create_traffic_lights()
        self.create_car_agents()
        self.create_motorcycle_agents()  # Add motorcycles to the simulation
        self.create_truck_agents()

    def create_buildings(self, size, middle_lane):
        for x in range(size):
            for y in range(size):
                if not (middle_lane - 3 <= x <= middle_lane + 3 or middle_lane - 3 <= y <= middle_lane + 3):
                    building = BuildingAgent(f"B-{x}-{y}", self)
                    self.schedule.add(building)
                    self.grid.place_agent(building, (x, y))
                elif x == middle_lane or y == middle_lane:
                    if not (middle_lane - 3 <= x <= middle_lane + 3 and middle_lane - 3 <= y <= middle_lane + 3):
                        building = BuildingAgent(f"B-{x}-{y}", self)
                        self.schedule.add(building)
                        self.grid.place_agent(building, (x, y))
                    if x == middle_lane and y == middle_lane:
                        building = BuildingAgent(f"B-{x}-{y}", self)
                        self.schedule.add(building)
                        self.grid.place_agent(building, (x, y))

    def create_traffic_lights(self):
        for position, initial_state in Semaphores:
            unique_id = self.next_id()
            traffic_light = TrafficLightAgent(unique_id, self, position, "red")  # Initialize all as red
            self.schedule.add(traffic_light)
            self.grid.place_agent(traffic_light, position)
            self.traffic_lights.append(traffic_light)

        # Ensure cycling starts with the first traffic light set to green
        if self.traffic_lights:
            self.light_index = 0  # Reset light index for cycling
            self.traffic_lights[self.light_index].state = "green"
            self.traffic_lights[self.light_index].timer = 5
            print(f"Traffic light at {self.traffic_lights[self.light_index].pos} initialized to green.")

    def create_car_agents(self):
        for _ in range(self.num_cars):
            starting_pos = random.choice(startList)
            target_pos = random.choice(endList)
            path = astarComplete(self.G, starting_pos, target_pos, manhattan_distance)
            unique_id = self.next_id()
            
            # Randomly assign an agent type
            agent_type = random.choice(["cooperative", "competitive", "neutral"])
            car = CarAgent(unique_id, self, starting_pos, target_pos, path, agent_type)
            
            self.schedule.add(car)
            self.grid.place_agent(car, starting_pos)

    def create_motorcycle_agents(self):
        for _ in range(self.num_motorcycles):
            starting_pos = random.choice(startList)
            target_pos = random.choice(endList)
            path = astarComplete(self.G, starting_pos, target_pos, manhattan_distance)
            unique_id = self.next_id()
            
            # Randomly assign an agent type
            agent_type = random.choice(["cooperative", "competitive", "neutral"])
            motorcycle = MotorcycleAgent(unique_id, self, starting_pos, target_pos, path, agent_type)
            
            self.schedule.add(motorcycle)
            self.grid.place_agent(motorcycle, starting_pos)

    def create_truck_agents(self):
        for _ in range(self.num_trucks):
            starting_pos = random.choice(startList)
            target_pos = random.choice(endList)
            path = astarComplete(self.G, starting_pos, target_pos, manhattan_distance)
            unique_id = self.next_id()
            
            # Randomly assign an agent type
            agent_type = random.choice(["cooperative", "competitive", "neutral"])
            truck = TruckAgent(unique_id, self, starting_pos, target_pos, path, agent_type)
            
            self.schedule.add(truck)
            self.grid.place_agent(truck, starting_pos)

    def step(self):
        current_light = self.traffic_lights[self.light_index]
        
        # Check if all cars associated with this light have reached their target
        associated_cars = [agent for agent in self.schedule.agents 
                        if isinstance(agent, (CarAgent, TruckAgent, MotorcycleAgent)) 
                        and agent.starting_pos in self.get_traffic_light_positions(current_light.pos)]
        
        if all(agent.reached_goal for agent in associated_cars):
            # Change traffic light states
            if current_light.state == "green" and current_light.timer == 0:
                current_light.state = "yellow"
                current_light.timer = 2
            elif current_light.state == "yellow" and current_light.timer == 0:
                current_light.state = "red"
                current_light.timer = 7
                # Cycle to the next traffic light and set it to green
                self.light_index = (self.light_index + 1) % len(self.traffic_lights)
                next_light = self.traffic_lights[self.light_index]
                next_light.state = "green"
                next_light.timer = 5
                print(f"Traffic light at {next_light.pos} turning green.")
        
        # Check if all vehicles have reached their destination
        all_vehicles_reached = all(agent.reached_goal for agent in self.schedule.agents 
                                if isinstance(agent, (CarAgent, TruckAgent, MotorcycleAgent)))
        
        # If all vehicles have reached their destination, set all traffic lights to yellow and stop the simulation
        if all_vehicles_reached:
            for light in self.traffic_lights:
                light.state = "yellow"
                light.timer = 2  # Optional: Set a timer for yellow light
            print("All vehicles have reached their destinations. All traffic lights set to yellow.")
            self.running = False  # Stop the simulation
            return  # Exit the step function to prevent further processing

        # Decrement the timer for the current light if it's still running
        if current_light.timer > 0:
            current_light.timer -= 1

        # Track advances by agent type based on negotiation results
        for agent in list(self.schedule.agents):
            if isinstance(agent, (CarAgent, TruckAgent, MotorcycleAgent)):
                if agent.pos == agent.target_pos:
                    print(f"{agent.__class__.__name__} {agent.unique_id} has reached its destination at {agent.pos} and will be removed.")
                    self.grid.remove_agent(agent)
                    self.schedule.remove(agent)
                elif agent.last_negotiation == "Advance":
                    if agent.agent_type == "cooperative":
                        self.cooperative_advances += 1
                    elif agent.agent_type == "competitive":
                        self.competitive_advances += 1
                    elif agent.agent_type == "neutral":
                        self.neutral_advances += 1
                    agent.last_negotiation = None  # Reset for the next round

        # Collect data for each step
        self.datacollector.collect(self)

        # Proceed with normal simulation step
        self.schedule.step()

    def get_traffic_light_positions(self, position):
        # Return starting positions associated with each traffic light
        if position == (9, 15):
            return [(8, 22), (9, 22), (10, 22)]
        elif position == (15, 13):
            return [(22, 12), (22, 13), (22, 14)]
        elif position == (13, 7):
            return [(12, 0), (13, 0), (14, 0)]
        elif position == (7, 9):
            return [(0, 8), (0, 9), (0, 10)]
        return []

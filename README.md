# SIMP
## Simulation and Instrumentation of Monopod Planarizer
### Prerequirements
Please follow the seup instruction repo to get ignition-gym, ignition etc setup before installing SIMP

### Installation
Install the latest pack of models using pip,

`pip3 install git+https://github.com/Baesian-Balancer/SIMP.git `

### Examples
 
`>>> import SIMP`

`>>> print(SIMP.get_model_file("monopod_v1"))`

`/home/dawson/Repos/SIMP/SIMP/monopod_v1/monopod_v1.urdf`

`>>> print(SIMP.get_model_file("ground_plane"))`

`/home/dawson/Repos/SIMP/SIMP/ground_plane/ground_plane.sdf`

can be paired with ignition-gym by Robotology like this,

```import time
import SIMP
from scenario import gazebo as scenario_gazebo

# Create the simulator
gazebo = scenario_gazebo.GazeboSimulator(step_size=0.001,
                                         rtf=1.0,
                                         steps_per_run=1)

# Initialize the simulator
gazebo.initialize()

# Get the default world and insert the ground plane
world = gazebo.get_world()
world.insert_model(SIMP.get_model_file("ground_plane"))

# Select the physics engine
world.set_physics_engine(scenario_gazebo.PhysicsEngine_dart)

# Insert monopod
world.insert_model(SIMP.get_model_file("monopod_v1"))

# Get the monopod model
monopod = world.get_model("monopod_v1")
# Open the GUI
gazebo.gui()

# Reset the pole position
monopod.get_joint("planarizer_02_joint").to_gazebo().reset_position(0.2)

time.sleep(3.5)
gazebo.run(paused=True)

# Simulate 30 seconds
for _ in range(int(30.0 / gazebo.step_size())):
    upper_leg = monopod.get_joint("upper_leg_joint").to_gazebo()
    lower_leg = monopod.get_joint("lower_leg_joint").to_gazebo()
    upper_leg.set_joint_generalized_force_target([0.3])
    lower_leg.set_joint_generalized_force_target([0.3])
    gazebo.run()
    print('lower leg: ', lower_leg.joint_position(),'upper leg: ', upper_leg.joint_position())
    

# Close the simulator
time.sleep(10)
gazebo.close()```

# NOTE:

We need to import SIMP in a gym gazebo model file for gym-ignition... if the import is held in a function the environment variables will be hidden and unable to be accessed...


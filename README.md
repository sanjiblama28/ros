```
Week-4
```

# Turtlesim
The terminal that I am using is in ROS_DISTRO=foxy and can also be checked by the given command below.

```
printenv | grep -i ROS
```
(![image](https://github.com/sanjiblama28/Github/blob/main/11.PNG)

## 1. Turtlesim: Installation
First of all,  making sure your system is up-to-date and then installing the turtlesim library along with checking that the package is installed by the following command.

```
sudo apt update
sudo apt install ros-foxy-turtlesim
ros2 pkg executables turtlesim
```
![image](https://github.com/sanjiblama28/Github/blob/main/12.PNG)

## 2. Turtlesim: Start

Enter the following command to start turtlesim in your terminal:
```
ros2 run turtlesim turtlesim_node
```
Now, the simulator window appears along with a turtle in the center and messages from the node can be seen in the terminal.    

![image](https://github.com/sanjiblama28/Github/blob/main/13.PNG)

## 3. Turtlesim: Using
Now, the new terminal needs to be opened and the following command needs to be executed to control the turtle type.
```
ros2 run turtlesim turtle_teleop_key
```
![image](https://github.com/sanjiblama28/Github/blob/main/l.PNG)

You should have three windows open at this point:
```
a terminal running turtlesim_node 
a terminal running turtle_teleop_key 
the turtlesim window
```

# RQT
## 4. Installation of RQT
Now, You need to open a new terminal to make sure your system is up-to-date and then install the rqt library and its plugins and to use rqt by the given command below.

```
sudo apt update
sudo apt install ~nros-foxy-rqt*
rqt
```
![image](https://github.com/sanjiblama28/Github/blob/main/141.PNG)

![image](https://github.com/sanjiblama28/Github/blob/main/14.PNG)


## 5. RQT: Running 
The window will be blank for the first time use of rqt. Then you need to select Plugins > Services > Service from the menu bar at the top.
![image](https://github.com/sanjiblama28/Github/blob/main/15.PNG)

## 5.1. Trying some of the services provided by service caller

Select the /spawn service where the /clear is seen and can also be used to select other services also and /spawn will help in creating another turtle in the turtlesim window by replacing the digit 0 with another digit and string name also needs to be written and the result can be seen in the response and the turtlesim window.

![image](https://github.com/sanjiblama28/Github/blob/main/161.PNG)

![image](https://github.com/sanjiblama28/Github/blob/main/162.PNG)

Now, using teleport_abosulte service as shown in the figure below.

![image](https://github.com/sanjiblama28/Github/blob/main/s1.PNG)

![image](https://github.com/sanjiblama28/Github/blob/main/s2.PNG)


## 6. RQT: rqt_console

A GUI tool called rqt_console is used in ROS 2 to inspect log messages.
With the following command, you can start rqt_console in a new terminal:
```
ros2 run rqt_console rqt_console
```
![image](https://github.com/sanjiblama28/Github/blob/main/17.PNG)

The console's first part is where the system log messages from your system will appear.
In the center, you can exclude severity levels to filter out messages.
The mails with your custom string are highlighted in the bottom portion.

## 7. ROS2 Nodes

## 7.1. ROS2 Graph

 A network of ROS 2 components processing data simultaneously makes up the ROS graph. If you were to map and visualize every executable, it would include all of their connections.
 
 ![image](https://github.com/sanjiblama28/Github/blob/main/d1.PNG)
 
 ![image](https://github.com/sanjiblama28/Github/blob/main/d2.PNG)

``` 
Week-5
```

# Using colcon to build packages

## Background

The ROS build tools colcon is an iteration of include catkin make, catkin make isolated, catkin tools, and ament tools.

## Prerequisites

## Install colcon

```
sudo apt install python3-colcon-common-extensions
```
![image](https://github.com/sanjiblama28/Github/blob/main/a1.PNG)

## Install ROS 2

You will require ROS 2 to build the examples.

# Create a workspace

Make a directory called ros2 ws to house our workspace first:

```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
```
![image](https://github.com/sanjiblama28/Github/blob/main/a2.PNG)

I modified ros2_ws to ros2_ws1 because I had built a workspace and package with a directory named ros2_ws.

Currently, the workspace only has the empty directory src:

```
.
└── src

1 directory, 0 files
```

## Add some sources

Let's clone the examples repository and place it in the workspace's src directory:

```
git clone https://github.com/ros2/examples src/examples -b foxy
```

![image](https://github.com/sanjiblama28/Github/blob/main/a3.PNG)

The source code for the ROS 2 examples should now be in the workspace:

```
.
└── src
    └── examples
        ├── CONTRIBUTING.md
        ├── LICENSE
        ├── rclcpp
        ├── rclpy
        └── README.md

4 directories, 3 files
```
## Build the workspace

```
colcon build --symlink-install
```

![image](https://github.com/sanjiblama28/Github/blob/main/a4.PNG)

After the build is finished, we should see the build, install, and log directories:

```
.
├── build
├── install
├── log
└── src

4 directories, 0 files
```
## Run tests

Run the following tests to run the packages we just built:

```
colcon test
```

![image](https://github.com/sanjiblama28/Github/blob/main/a5.PNG)

## Source the environment

```
. install/setup.bash
```

## Try a demo

Executables created by Colcon can be run using the environment supplied. Run a subscriber node using the following examples:

```
ros2 run examples_rclcpp_minimal_subscriber subscriber_member_function
```

![image](https://github.com/sanjiblama28/Github/blob/main/a6.PNG)

Let's launch a publisher node in a different terminal (remember to source the setup script):

```
ros2 run examples_rclcpp_minimal_publisher publisher_member_function
```

![image](https://github.com/sanjiblama28/Github/blob/main/a7.PNG)

Messages from the publisher and subscriber should appear, their numbers rising.

# Create your own package

## Setup colcon_cd

```
echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
echo "export _colcon_cd_root=/opt/ros/foxy/" >> ~/.bashrc
```

## Setup colcon tab completion

```
echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
```

# A Simple Publisher and Subscriber

## 1 Create a package

Navigate into ros2_ws/src and run the package creation command:

```
ros2 pkg create --build-type ament_python py_pubsub
```
A notification from your terminal confirming the creation of your package py pubsub and all of its required files and folders will be shown.

## 2 Write the publisher node

Navigate into ros2_ws/src/py_pubsub/py_pubsub and by executing the following command, the example talker code can be downloaded:

```
wget https://raw.githubusercontent.com/ros2/examples/foxy/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py
```
![image](https://github.com/sanjiblama28/Github/blob/main/sp1.PNG)

A new file called publisher member function.py will now be present next to __init .py.
Use the text editor of your choice to open the file.

```
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```
## 2.1 Add dependencies

Navigate one level back to the ros2_ws/src/py_pubsub directory, where the setup.py, setup.cfg, and package.xml files have been created for you.

Use your text editor to open package.xml, and be sure to complete the description>, maintainer>, and license> tags:

```
<description>Examples of minimal publisher/subscriber using rclpy</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache License 2.0</license>
```

Add the following dependencies following the lines above that match to the import declarations for your node:

```
<exec_depend>rclpy</exec_depend>
<exec_depend>std_msgs</exec_depend>
```

![image](https://github.com/sanjiblama28/Github/blob/main/sp5.PNG)

This declares that when the package's code is executed, rclpy and std msgs are required.

Ensure that the file is saved.

## 2.2 Add an entry point

Check out the setup.py file. Make sure to match the maintainer, maintainer email, description, and license columns to your package.xml once more:

```
maintainer='YourName',
maintainer_email='you@email.com',
description='Examples of minimal publisher/subscriber using rclpy',
license='Apache License 2.0',
```
Within the console scripts brackets of the entry points field, add the following line:

```
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
        ],
},
```

![image](https://github.com/sanjiblama28/Github/blob/main/sp6.PNG)

Remember to save.

## 2.3 Check setup.cfg

The setup.cfg file should automatically contain the following information:

```
[develop]
script-dir=$base/lib/py_pubsub
[install]
install-scripts=$base/lib/py_pubsub
```
Simply instruct setuptools to place your executables in the lib directory, where ros2 run will look for them.

If you wanted to see the entire system in action, you could build your package right now, source the local setup files, and launch it. However, let's first create the subscriber node.

## 3 Write the subscriber node

The next node can be created by going back to ros2 ws/src/py pubsub/py pubsub. Fill out your terminal with the following code:

```
wget https://raw.githubusercontent.com/ros2/examples/foxy/rclpy/topics/minimal_subscriber/examples_rclpy_minimal_subscriber/subscriber_member_function.py
```
Now, the directory must include the following files:

```
__init__.py  publisher_member_function.py  subscriber_member_function.py
```

Now, Open the subscriber_member_function.py with your text editor.

```
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

## 3.1 Add an entry point

Reopen setup.py and place the subscriber node's entry point beneath the publisher's entry point. Now, the entry points field should be as follows:

```
entry_points={
        'console_scripts': [
                'talker = py_pubsub.publisher_member_function:main',
                'listener = py_pubsub.subscriber_member_function:main',
        ],
},
```

![image](https://github.com/sanjiblama28/Github/blob/main/sp7.PNG)

Once the file has been saved, your pub/sub system should be operational.

## 4 Build and Run

The rclpy and std msgs packages are probably already installed on your ROS 2 system. Before building, it's best practice to run rosdep in the workspace's root directory (ros2 ws) to check for any missing dependencies:

```
rosdep install -i --from-path src --rosdistro foxy -y
```

Still in the root of your workspace, ros2_ws, build your new package:

```
colcon build --packages-select py_pubsub
```
![image](https://github.com/sanjiblama28/Github/blob/main/sp2%20(2).PNG)

Open a new terminal, navigate to ros2_ws, and source the setup files:

```
. install/setup.bash
```

Now run the talker node:

```
ros2 run py_pubsub talker
```
Starting in 0.5 seconds, the terminal should begin sending out info messages as follows:

```
[INFO] [minimal_publisher]: Publishing: "Hello World: 0"
[INFO] [minimal_publisher]: Publishing: "Hello World: 1"
[INFO] [minimal_publisher]: Publishing: "Hello World: 2"
[INFO] [minimal_publisher]: Publishing: "Hello World: 3"
[INFO] [minimal_publisher]: Publishing: "Hello World: 4"
```

![image](https://github.com/sanjiblama28/Github/blob/main/sp3.PNG)

Launch a new terminal, once more source the setup files from ros2 ws, and then launch the listener node:

```
ros2 run py_pubsub listener
```

Starting at the publisher's current message count, the listener will begin writing messages to the console as follows:

```
[INFO] [minimal_subscriber]: I heard: "Hello World: 10"
[INFO] [minimal_subscriber]: I heard: "Hello World: 11"
[INFO] [minimal_subscriber]: I heard: "Hello World: 12"
[INFO] [minimal_subscriber]: I heard: "Hello World: 13"
[INFO] [minimal_subscriber]: I heard: "Hello World: 14"
```

![image](https://github.com/sanjiblama28/Github/blob/main/sp4.PNG)

Enter Ctrl+C in each terminal to stop the nodes from spinning

# A Simple Service and Client 

## 1 Create a package

Navigate into ros2_ws/src and run the package creation command:

```
ros2 pkg create --build-type ament_python py_srvcli --dependencies rclpy example_interfaces
```

A notification from your terminal confirming the creation of your package py_srvcli and all of its required files and folders will be shown.

![image](https://github.com/sanjiblama28/Github/blob/main/ss1.PNG)

## 1.1 Update (package.xml)

You don't need to manually add dependencies to package.xml because you used the --dependencies option when creating the package.

But as always, remember to fill up package.xml with the description, maintainer's name and email, and license details.

```
<description>Python client server tutorial</description>
<maintainer email="you@email.com">Your Name</maintainer>
<license>Apache License 2.0</license>
```
![image](https://github.com/sanjiblama28/Github/blob/main/ssp4.PNG)

## 1.2 Update (setup.py)

The maintainer, maintainer email, description, and license fields should all have the following information added to the setup.py file:

```
maintainer='Your Name',
maintainer_email='you@email.com',
description='Python client server tutorial',
license='Apache License 2.0',
```
![image](https://github.com/sanjiblama28/Github/blob/main/ssp5.PNG)

## 2 Write the service node

Create a new file called service_member_function.py in the ros2 ws/src/py_srvcli/py_srvcli directory, and then paste the following code inside:

```
from example_interfaces.srv import AddTwoInts

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

## 2.1 Add an entry point

The entry point must be added to setup.py (found in the ros2 ws/src/py srvcli directory) in order for the ros2 run command to be able to execute your node.

The following line to be added in between the "console scripts" brackets:

```
'service = py_srvcli.service_member_function:main',
```

![image](https://github.com/sanjiblama28/Github/blob/main/ssp6.PNG)

## 3 Write the client node

Create a new file called client_member_function.py in the ros2 ws/src/py_srvcli/py_srvcli directory, and then paste the following code inside:

```
import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    response = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    minimal_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.sum))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```
![image](https://github.com/sanjiblama28/Github/blob/main/ssp3.jpg)

## 3.1 Add an entry point

The client node requires an entry point to be added, much like the service node does.

Your setup.py file's entry points column needs to be formatted as follows:

```
entry_points={
    'console_scripts': [
        'service = py_srvcli.service_member_function:main',
        'client = py_srvcli.client_member_function:main',
    ],
},
```

![image](https://github.com/sanjiblama28/Github/blob/main/ssp7.PNG)

## 4 Build and Run

To check for missing dependencies before building, it's a good idea to run rosdep in the workspace's root directory (ros2 ws):

```
rosdep install -i --from-path src --rosdistro foxy -y
```

Navigate back to the root of your workspace, ros2_ws, and build your new package:

```
colcon build --packages-select py_srvcli
```

![image](https://github.com/sanjiblama28/Github/blob/main/ssp2.jpg)

Open a new terminal, navigate to ros2_ws, and source the setup files:

```
. install/setup.bash
```

Now run the service node:

```
ros2 run py_srvcli service
```
The node will await the request from the client.

Open a new terminal and once more source the setup files from ros2_ws. the client node, any two integers, and a space between them.

```
ros2 run py_srvcli client 2 3
```

The client would get a response like this if you selected options 2 and 3 as an example:

```
[INFO] [minimal_client_async]: Result of add_two_ints: for 2 + 3 = 5
```

![image](https://github.com/sanjiblama28/Github/blob/main/ss3.PNG)

The terminal where your service node is executing should be visited again. When it received the request, as you can see, it published the following log messages:

```
[INFO] [minimal_service]: Incoming request
a: 2 b: 3
```

![image](https://github.com/sanjiblama28/Github/blob/main/ssp1.jpg)

Enter Ctrl+C in each terminal to stop the nodes from spinning

# Creating custom msg and srv files

## 1 Create a new package

Navigate into ros2_ws/src and run the package creation command:

```
ros2 pkg create --build-type ament_cmake tutorial_interfaces
```

A notification from your terminal confirming the creation of your package tutorial_interfaces and all of its required files and folders will be shown. It should be noted that it is a CMake package because pure Python packages cannot yet generate.msg or.srv files. A Python node, which will be discussed in the last part, can use a custom interface that you design in a CMake package.

Maintaining.msg and.srv files in separate locations within a package is excellent practice. In ros2 ws/src/tutorial interfaces, create the directories.

```
mkdir msg

mkdir srv
```

![image](https://github.com/sanjiblama28/Github/blob/main/sss1.PNG)

## 2 Create custom definitions

## 2.1 msg definition 

Create a new file called Num.msg in the tutorial interfaces/msg directory that you just made, then add a single line of code stating the data structure in Num.msg:

```
int64 num
```
This custom message transmits the 64-bit integer num, which is one single value.

Create a new file called Sphere.msg in the tutorial interfaces/msg directory that you just established and fill it with the following information:

```
geometry_msgs/Point center
float64 radius
```
This custom message makes use of a message from a different message package (in this case, geometry msgs/Point).

## 2.2 srv definition

Create a new file called AddThreeInts.srv with the following request and response structure back in the tutorial interfaces/srv directory you just made:

```
int64 a
int64 b
int64 c
---
int64 sum
```
This is a custom service that accepts three integers with names a, b, and c and returns an answer with the integer sum.

![image](https://github.com/sanjiblama28/Github/blob/main/sss2.PNG)

## 3 CMakeLists.txt

Add the following lines to CMakeLists.txt to translate the interfaces you defined into language-specific code (such C++ and Python) so they may be utilized in those languages:

```
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Num.msg"
  "msg/Sphere.msg"
  "srv/AddThreeInts.srv"
  DEPENDENCIES geometry_msgs # Add packages that above messages depend on, in this case geometry_msgs for Sphere.msg
)
```

## 4 package.xml

These lines should be added to package.xml.

```
<depend>geometry_msgs</depend>

<build_depend>rosidl_default_generators</build_depend>

<exec_depend>rosidl_default_runtime</exec_depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```

## 5 Build the tutorial_interfaces package

You may construct your custom interfaces package now that all of its components are in place. Run the command below in the workspace's root (~/ros2_ws):

```
colcon build --packages-select tutorial_interfaces
```
![image](https://github.com/sanjiblama28/Github/blob/main/sss3.PNG)

Other ROS 2 programs will now be able to find the interfaces.

## 6 Confirm msg and srv creation

Run the following command from within your workspace (ros2 ws) to source it in a new terminal:

```
. install/setup.bash
```

The ros2 interface show command can now be used to verify that your interface creation was successful:

```
ros2 interface show tutorial_interfaces/msg/Num
```
should return:
```
int64 num
```
And
```
ros2 interface show tutorial_interfaces/msg/Sphere
```
should return:
```
geometry_msgs/Point center
        float64 x
        float64 y
        float64 z
float64 radius
```
And
```
ros2 interface show tutorial_interfaces/srv/AddThreeInts
```
should return:

```
int64 a
int64 b
int64 c
---
int64 sum
```
![image](https://github.com/sanjiblama28/Github/blob/main/sss4.PNG)

## 7 Test the new interfaces

You can utilize the packages you made in earlier instructions for this step. You may use your new interfaces by making a few straightforward changes to the nodes, CMakeLists, and package files.

## 7.1 Testing Num.msg with pub/sub

You may see Num.msg in action by making a few minor adjustments to the publisher/subscriber package developed in a prior tutorial (C++ or Python). The output will be slightly different because you'll be switching from the default string message to a numerical one.

Publisher:

```
import rclpy
from rclpy.node import Node

from tutorial_interfaces.msg import Num    # CHANGE


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Num, 'topic', 10)     # CHANGE
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Num()                                           # CHANGE
        msg.num = self.i                                      # CHANGE
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%d"' % msg.num)  # CHANGE
        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

Subscriber:

```
import rclpy
from rclpy.node import Node

from tutorial_interfaces.msg import Num        # CHANGE


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Num,                                              # CHANGE
            'topic',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
            self.get_logger().info('I heard: "%d"' % msg.num) # CHANGE


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

CMakeLists.txt:

Add the following lines (C++ only):

```
#...

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tutorial_interfaces REQUIRED)                         # CHANGE

add_executable(talker src/publisher_member_function.cpp)
ament_target_dependencies(talker rclcpp tutorial_interfaces)         # CHANGE

add_executable(listener src/subscriber_member_function.cpp)
ament_target_dependencies(listener rclcpp tutorial_interfaces)     # CHANGE

install(TARGETS
  talker
  listener
  DESTINATION lib/${PROJECT_NAME})

ament_package()
```

package.xml:

Add the following line:

```
<exec_depend>tutorial_interfaces</exec_depend>
```

After making the above edits and saving all the changes, build the package:

```
colcon build --packages-select py_pubsub
```
On Windows:

```
colcon build --merge-install --packages-select py_pubsub
```

Then open two new terminals, source ros2_ws in each, and run:

```
ros2 run py_pubsub talker

```

![image](https://github.com/sanjiblama28/Github/blob/main/sss5.PNG)

```
ros2 run py_pubsub listener

```

![image](https://github.com/sanjiblama28/Github/blob/main/sss7.PNG)

The talker should only be publishing integer values as opposed to the string it previously published as Num.msg only relays an integer:

```
[INFO] [minimal_publisher]: Publishing: '0'
[INFO] [minimal_publisher]: Publishing: '1'
[INFO] [minimal_publisher]: Publishing: '2'
```

## 7.2 Testing AddThreeInts.srv with service/client

You may use AddThreeInts.srv by making a few minor adjustments to the service/client package developed in a prior tutorial (in C++ or Python). The output will alter significantly because you'll be switching from the initial two integer request srv to a three integer request srv.

Service:

```
from tutorial_interfaces.srv import AddThreeInts     # CHANGE

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(AddThreeInts, 'add_three_ints', self.add_three_ints_callback)        # CHANGE

    def add_three_ints_callback(self, request, response):
        response.sum = request.a + request.b + request.c                                                  # CHANGE
        self.get_logger().info('Incoming request\na: %d b: %d c: %d' % (request.a, request.b, request.c)) # CHANGE

        return response

def main(args=None):
    rclpy.init(args=args)

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

Client:

```
from tutorial_interfaces.srv import AddThreeInts       # CHANGE
import sys
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(AddThreeInts, 'add_three_ints')       # CHANGE
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = AddThreeInts.Request()                                   # CHANGE

    def send_request(self):
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[2])
        self.req.c = int(sys.argv[3])                  # CHANGE
        self.future = self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                    'Result of add_three_ints: for %d + %d + %d = %d' %                               # CHANGE
                    (minimal_client.req.a, minimal_client.req.b, minimal_client.req.c, response.sum)) # CHANGE
            break

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

CMakeLists.txt:

Add the following lines (C++ only):

```
#...

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tutorial_interfaces REQUIRED)        # CHANGE

add_executable(server src/add_two_ints_server.cpp)
ament_target_dependencies(server
  rclcpp tutorial_interfaces)                      #CHANGE

add_executable(client src/add_two_ints_client.cpp)
ament_target_dependencies(client
  rclcpp tutorial_interfaces)                      #CHANGE

install(TARGETS
  server
  client
  DESTINATION lib/${PROJECT_NAME})

ament_package()
```

package.xml:

Add the following line:

```
<exec_depend>tutorial_interfaces</exec_depend>
```

After making the above edits and saving all the changes, build the package:

```
colcon build --packages-select py_srvcli
```

On Windows:

```
colcon build --merge-install --packages-select py_srvcli
```

Then open two new terminals, source ros2_ws in each, and run:

```
ros2 run py_srvcli service
```

![image](https://github.com/sanjiblama28/Github/blob/main/sss8.PNG)

```
ros2 run py_srvcli client 2 3 1
```

![image](https://github.com/sanjiblama28/Github/blob/main/sss9.PNG)

```
Week-6
```

# Managing Dependencies with rosdep

## How do I use the rosdep tool?

We are prepared to use the utility now that we have a basic understanding of rosdep, package.xml, and rosdistro. First, if using rosdep for the first time, it must be initialized using:

```
sudo rosdep init
rosdep update
```

![image](https://user-images.githubusercontent.com/92040822/194984951-6c15ca19-ef70-459a-bc1d-c3dcbed8acb9.png)


We can finally use rosdep install to install dependencies. This is often called once across a workspace that contains numerous packages in order to install all dependencies. If the workspace's root contained the source-code-containing directory src, a call for that might look like the following.

```
rosdep install --from-paths src -y --ignore-src
```
![image](https://user-images.githubusercontent.com/92040822/194985049-f97687a2-a070-432b-8d50-15b0e4f318d9.png)

# Creating an action

## Prerequisites

Colcon and ROS 2 must be installed.

Establish a workspace and a package called "action tutorials interfaces":

(Remember to source first from your ROS 2 installation.)

```
mkdir -p ros2_ws/src #you can reuse existing workspace with this naming convention
cd ros2_ws/src
ros2 pkg create action_tutorials_interfaces
```

![image](https://user-images.githubusercontent.com/92040822/194985781-d285bf6d-dc69-4898-b207-e77806cc20ab.png)

## Tasks
## 1. Defining an action

Actions are described in .action files with the following format:

```
# Request
---
# Result
---
# Feedback
```
Create a directory called "action" in our ROS 2 package called "action tutorials interfaces":

```
cd action_tutorials_interfaces
mkdir action
```

![image](https://user-images.githubusercontent.com/92040822/194997859-cf7b8875-7ee6-4fb1-ad5d-61ea9c9b3ec8.png)


Make a file called Fibonacci in the action directory. action that includes the following information:

```
int32 order
---
int32[] sequence
---
int32[] partial_sequence
```

## 2. Building an action

The definition of the new Fibonacci action type must be sent to the pipeline that generates Rosidl code before we can use it in our code.

The following lines need be added to our CMakeLists.txt before the ament package() line in the action tutorials interfaces to achieve this:

```
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/Fibonacci.action"
)
```

We must also include the necessary dependencies in our package.xml file:

```
<buildtool_depend>rosidl_default_generators</buildtool_depend>

<depend>action_msgs</depend>

<member_of_group>rosidl_interface_packages</member_of_group>
```

The fact that action definitions contain additional metadata means that we must rely on action msgs (e.g. goal IDs).

The package containing the definition of the Fibonacci action should now be able to be built:

```
# Change to the root of the workspace
cd ~/ros2_ws
# Build
colcon build
```

![image](https://user-images.githubusercontent.com/92040822/194997429-6b430f6e-8bbd-4bb3-9f57-33c69ba07dec.png)

We are done!

Action types will often start with the term "action" and the package name. As a result, our new action will be referred to by its complete name, action tutorials interfaces/action/Fibonacci.

Using the command line tool, we can verify that our action was built successfully:

```
# Source our workspace
# On Windows: call install/setup.bat
. install/setup.bash
# Check that our action definition exists
ros2 interface show action_tutorials_interfaces/action/Fibonacci
```

![image](https://user-images.githubusercontent.com/92040822/194998140-8b4ab337-de02-4b82-8eed-09df6c031cbf.png)


The definition of the Fibonacci action should appear on the screen.

# Writing an action server and client

## Prerequisites

You will require both the Fibonacci.action interface from the previous tutorial, "Creating an action," and the action tutorials interfaces package.

## Tasks

## 1. Writing an action server

You should create a new file in your home directory called fibonacci action server.py and add the following code to it:

```
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        result = Fibonacci.Result()
        return result


def main(args=None):
    rclpy.init(args=args)

    fibonacci_action_server = FibonacciActionServer()

    rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
    main()
```

Let's attempt to run our action server:

```
python3 fibonacci_action_server.py
```

![image](https://user-images.githubusercontent.com/92040822/195005805-079536ff-680e-41f3-8b1f-52c91067fd85.png)

We can communicate a goal via the command line interface to another terminal:

```
ros2 action send_goal fibonacci action_tutorials_interfaces/action/Fibonacci "{order: 5}"
```

![image](https://user-images.githubusercontent.com/92040822/195005945-5bed8f77-710a-4cc2-b45e-e13fcd590e2c.png)

You should see the logged message "Executing goal..." followed by a notice that the goal state was not established in the terminal that is running the action server. The aborted state is assumed by default if the goal handle state is not set in the execute callback.

The succeed() method on the goal handle can be used to show that the goal was successful:

```
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')

        goal_handle.succeed()

        result = Fibonacci.Result()
        return result
```

You should see the goal completed with the status SUCCEED if you restart the action server and send another goal at this point. 

![image](https://user-images.githubusercontent.com/92040822/195006346-83e3bae1-0ce7-4693-97e1-ea8ce72be268.png)

![image](https://user-images.githubusercontent.com/92040822/195006367-2b341169-9964-4b03-b992-d3ee7165785a.png)

Let's now make sure that our target execution computes and returns the specified Fibonacci sequence:

```
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')


        sequence = [0, 1]



        for i in range(1, goal_handle.request.order):

            sequence.append(sequence[i] + sequence[i-1])


        goal_handle.succeed()

        result = Fibonacci.Result()

        result.sequence = sequence

        return result
```

We compute the sequence, assign it to the result message field, and then proceed to the return.

Send another goal and restart the action server. The aim should be completed with the expected results in order.

![image](https://user-images.githubusercontent.com/92040822/195006747-a1500020-d012-434b-9ad3-87ba9987323e.png)

![image](https://user-images.githubusercontent.com/92040822/195006803-99357e2b-2932-4885-8205-e26e372d6f1a.png)

## 1.2 Publishing feedback

The sequence variable will be swapped out, and the sequence will now be stored in a feedback message. We publish the feedback message and then fall asleep after each update of the feedback message in the for-loop for impact:

```
import time


import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')


        feedback_msg = Fibonacci.Feedback()

        feedback_msg.partial_sequence = [0, 1]


        for i in range(1, goal_handle.request.order):

            feedback_msg.partial_sequence.append(

                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1])

            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))

            goal_handle.publish_feedback(feedback_msg)

            time.sleep(1)


        goal_handle.succeed()

        result = Fibonacci.Result()

        result.sequence = feedback_msg.partial_sequence

        return result


def main(args=None):
    rclpy.init(args=args)

    fibonacci_action_server = FibonacciActionServer()

    rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
    main()
```

Utilizing the command line tool with the --feedback option after restarting the action server, we can verify that feedback has now been published:

```
ros2 action send_goal --feedback fibonacci action_tutorials_interfaces/action/Fibonacci "{order: 5}"
```

![image](https://user-images.githubusercontent.com/92040822/195008024-7aed6b72-3e4a-4baa-ae36-de3bee6fdd54.png)


![image](https://user-images.githubusercontent.com/92040822/195007345-05b776e6-bec4-47ab-bd78-f714953600e0.png)

## 2. Writing an action client

We'll limit the action client to just one file as well. Then, open a new file and name it fibonacci action client.py. Add the following boilerplate code to the new file:

```
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'fibonacci')

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()

        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client = FibonacciActionClient()

    future = action_client.send_goal(10)

    rclpy.spin_until_future_complete(action_client, future)


if __name__ == '__main__':
    main()
```

Let's test our action client by first launching the earlier-built action server:

```
python3 fibonacci_action_server.py
```

Run the action client in an other terminal.

```
python3 fibonacci_action_client.py
```

As the action server completes the goal, the following messages should be printed:

```
[INFO] [fibonacci_action_server]: Executing goal...
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3])
[INFO] [fibonacci_action_server]: Feedback: array('i', [0, 1, 1, 2, 3, 5])
# etc.
```

![image](https://user-images.githubusercontent.com/92040822/195008493-54dd71ba-08eb-4e15-a8fd-607641d65326.png)

The action client should begin and complete as soon as possible. We currently have a working action client, but we receive no feedback or results.

## 2.1 Getting a result

We must first obtain a goal handle for the goal that we sent. The result can then be requested using the goal handle.

The full code for this example is provided here:

```
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'fibonacci')

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        rclpy.shutdown()


def main(args=None):
    rclpy.init(args=args)

    action_client = FibonacciActionClient()

    action_client.send_goal(10)

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
```

Go ahead and attempt to run our Fibonacci action client while an action server is running in a separate terminal!

```
python3 fibonacci_action_client.py
```

![image](https://user-images.githubusercontent.com/92040822/195009217-a65fdda3-72f8-46c5-b863-a95166ea9dce.png)

You should be able to see the goal being accepted and the outcome in the logs.

## 2.2 Getting feedback

We can send goals to our action client. Nice! However, it would be wonderful to hear some input regarding the goals we transmit from the action server.

Here is the whole code for this illustration:

```
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'fibonacci')

    def send_goal(self, order):
        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.sequence))
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))


def main(args=None):
    rclpy.init(args=args)

    action_client = FibonacciActionClient()

    action_client.send_goal(10)

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
```

Everything is ready for us. Your screen should display feedback if we run our action client.

```
python3 fibonacci_action_client.py
```

![image](https://user-images.githubusercontent.com/92040822/195010081-8356976d-ace7-4f85-acc7-2d20318cd105.png)

# Composing multiple nodes in a single process


## Discover available components

Run the following commands in a shell to see what components are registered and accessible in the workspace:

```
ros2 component types
```

The terminal will provide a list of every component that is available:

```
(... components of other packages here)
composition
  composition::Talker
  composition::Listener
  composition::Server
  composition::Client
```

![image](https://user-images.githubusercontent.com/92040822/196695754-20bd1682-0e54-408c-8a42-db48a92739d6.png)
  
## Run-time composition using ROS services with a publisher and subscriber

Start the component container in the first shell.

```
ros2 run rclcpp_components component_container
```

Open the second shell, then use the ros2 command line tools to confirm if the container is active:

```
ros2 component list
```

You ought to see the component's name:

```
/ComponentManager
```

![image](https://user-images.githubusercontent.com/92040822/196696246-e7e9202a-1a14-4ab3-8ecb-a5b4a5f0bb64.png)

Load the talker component into the second shell (see the talker source code):

```
ros2 component load /ComponentManager composition composition::Talker
```

The command will return the unique ID of the loaded component as well as the node name:

```
Loaded component 1 into '/ComponentManager' container node as '/talker'
```
![image](https://user-images.githubusercontent.com/92040822/196696591-c9d24ce0-ca5a-464a-9468-ad576f604616.png)

Messages indicating that the component was loaded and that a message was published should now appear in the first shell.

![image](https://user-images.githubusercontent.com/92040822/196696795-ce644651-75ba-4b4d-a068-0a8528473160.png)

Run a different command in the second shell to load the listener component (see the listener source code):

```
ros2 component load /ComponentManager composition composition::Listener
```

Terminal will return:

```
Loaded component 2 into '/ComponentManager' container node as '/listener'
```

![image](https://user-images.githubusercontent.com/92040822/196697102-034a3256-6639-4c72-93bb-c3228e761c14.png)

Now, the container's state may be examined using the ros2 command-line tool:

```
ros2 component list
```

The outcome will be as follows:

```
/ComponentManager
   1  /talker
   2  /listener
```

![image](https://user-images.githubusercontent.com/92040822/196697455-c2d18f17-164f-4540-a740-c94286c1bbc7.png)

The first shell should now provide repeated output for each message that was received.

## Run-time composition using ROS services with a server and client

The first shell contains:

```
ros2 run rclcpp_components component_container
```

In the second shell (see the source code for the server and client):

```
ros2 component load /ComponentManager composition composition::Server
ros2 component load /ComponentManager composition composition::Client
```
![image](https://user-images.githubusercontent.com/92040822/196700307-a1e303ca-a221-4ff3-b434-395f8b3355c9.png)

In this scenario, the client requests something from the server, which then processes the request and sends back an answer, which the client then outputs.

## Compile-time composition using ROS services

This demonstration demonstrates how the same shared libraries can be used to create an executable that runs numerous components from a single file. The talker and listener, as well as the server and client, are all included in the executable.

In the shell call (see source code):

```
ros2 run composition manual_composition
```

![image](https://user-images.githubusercontent.com/92040822/196701189-3235f758-0cf1-4056-ba68-b336e2bc5987.png)

This should demonstrate repeated messages from both pairs, including the talker and listener, server, and client.

## Run-time composition using dlopen

This demonstration offers a different approach to run-time composition by building a generic container process and explicitly passing the libraries to load without utilizing ROS APIs. One instance of each "rclcpp::Node" class will be created in each open library's source code by the procedure.

```
ros2 run composition dlopen_composition `ros2 pkg prefix composition`/lib/libtalker_component.so `ros2 pkg prefix composition`/lib/liblistener_component.so
```

![image](https://user-images.githubusercontent.com/92040822/196701548-94c73072-f111-49ef-b73c-9d042a0d1f9f.png)

## Composition using launch actions

While the command line tools can be helpful for troubleshooting and debugging component setups, it is frequently more practical to launch a group of components at once. We can make use of the ros2 launch feature to automate this process.

```
ros2 launch composition composition_demo.launch.py
```

![image](https://user-images.githubusercontent.com/92040822/196701949-072ec24a-d9f9-41a1-bac9-0006ecac1081.png)

# Advanced Topics

We may look at more sophisticated issues now that the fundamental operation of the components has been completed.

## Unloading components

Start the component container in the first shell.

```
ros2 run rclcpp_components component_container
```

Using the ros2 command line tools, confirm the container is active:

```
ros2 component list
```

You ought to see the component's name:

```
/ComponentManager
```

![image](https://user-images.githubusercontent.com/92040822/196702620-268dfad0-cc21-4731-acfb-6039b53bfec0.png)

Within the second shell (see talker source code). Both the node name and the component's distinctive ID will be returned by the command.

```
ros2 component load /ComponentManager composition composition::Talker
ros2 component load /ComponentManager composition composition::Listener
```

![image](https://user-images.githubusercontent.com/92040822/196702977-1352f25b-9f67-402b-bf8d-235e6c2b06e4.png)

The node can be removed from the component container by using its special ID.

```
ros2 component unload /ComponentManager 1 2
```

The terminal should return:

```
Unloaded component 1 from '/ComponentManager' container
Unloaded component 2 from '/ComponentManager' container
```

![image](https://user-images.githubusercontent.com/92040822/196703265-ea574fef-5475-4d20-95cd-04c278b5c5b2.png)

Verify that the talker and listener's repeated messages have stopped in the first shell.

## Remapping container name and namespace

Standard command line parameters can be used to remap the name and namespace of the component manager:

```
ros2 run rclcpp_components component_container --ros-args -r __node:=MyContainer -r __ns:=/ns
```

Components can be loaded in a second shell by using the modified container name:

```
ros2 component load /ns/MyContainer composition composition::Listener
```

![image](https://user-images.githubusercontent.com/92040822/196704015-2ee12101-fcbb-4afb-babd-0bde5dbbe0b5.png)

![image](https://user-images.githubusercontent.com/92040822/196704105-431a27db-dd25-431f-9213-4de11f920802.png)

## Remap component names and namespaces

Arguments to the load command can be used to change component names and namespaces.

Start the component container in the first shell.

```
ros2 run rclcpp_components component_container
```

Several illustrations of name and namespace remapping.

Node name to remap:

```
ros2 component load /ComponentManager composition composition::Talker --node-name talker2
```

Remap namespace:

```
ros2 component load /ComponentManager composition composition::Talker --node-namespace /ns
```

Remap both:

```
ros2 component load /ComponentManager composition composition::Talker --node-name talker3 --node-namespace /ns2
```

Now use ros2 command line utility:

```
ros2 component list
```

In the console you should see corresponding entries:

```
/ComponentManager
   1  /talker2
   2  /ns/talker
   3  /ns2/talker
```

![image](https://user-images.githubusercontent.com/92040822/196704739-27d7c9b9-861c-4ff6-b9fc-757c95829fb6.png)

![image](https://user-images.githubusercontent.com/92040822/196704864-f163488d-c1b7-4f38-9f01-44b24568552a.png)

## Passing parameter values into components

Passing arbitrary parameters to the node as it is being built is supported by the ros2 component load command-line. Here are some examples of how to use this functionality:

```
ros2 component load /ComponentManager image_tools image_tools::Cam2Image -p burger_mode:=true
```

![image](https://user-images.githubusercontent.com/92040822/196705455-d317ca6e-5118-4d81-9a22-f47106ee2e27.png)

## Passing additional arguments into components

Specific settings can be passed to the component manager using the ros2 component load command-line to be used while building the node. Using intra-process communication to instantiate a node is currently the sole supported command-line option. The following are some uses for this functionality:

```
ros2 component load /ComponentManager composition composition::Talker -e use_intra_process_comms:=true
```

![image](https://user-images.githubusercontent.com/92040822/196705580-627ccdb4-0a6d-4c6e-87b8-0889d515724b.png)

# Creating launch files

## 1. Setup

Organize your launch files in a new directory by creating it:

```
mkdir launch
```

## 2. Write the launch file

Utilize the turtlesim package and associated executables to create a ROS 2 launch file.
The following code should be copied and pasted into the launch/turtlesim mimic launch.py file:

```
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        )
    ])
```

![image](https://user-images.githubusercontent.com/92040822/196708973-1cb57155-fc2b-4deb-ab23-16c7a2fe6a0d.png)

## 3. ROS2 launch

Enter the directory you previously created, then issue the following command to start the launch file you produced above:

```
cd launch
ros2 launch turtlesim_mimic_launch.py
```
The following [INFO] messages letting you know which nodes your launch file has begun appear in two turtlesim windows:

```
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [turtlesim_node-1]: process started with pid [11714]
[INFO] [turtlesim_node-2]: process started with pid [11715]
[INFO] [mimic-3]: process started with pid [11716]
```

![image](https://user-images.githubusercontent.com/92040822/196709379-78ff3b4e-049d-492d-950f-84a8965785a8.png)

Open a fresh terminal and issue the ros2 topic pub command on the /turtlesim1/turtle1/cmd_vel topic to move the first turtle in order to witness the system in action:

```
ros2 topic pub -r 1 /turtlesim1/turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -1.8}}"
```

The two turtles will appear to be traveling in unison.

![image](https://user-images.githubusercontent.com/92040822/196709891-62c85dd4-199e-4880-936f-3c83e7c86203.png)


## 4. Introspect the system with rqt_graph

Open a new terminal and run rqt graph while the system is still operating to better understand the connections between the nodes in your launch file.

Execute this command:

```
rqt_graph
```

![image](https://user-images.githubusercontent.com/92040822/196710417-a83aaf8a-9823-485f-82c3-bdf321c85916.png)

![image](https://user-images.githubusercontent.com/92040822/196711277-7ab17e0d-f549-4fb2-965d-54b5eac66c1d.png)

![image](https://user-images.githubusercontent.com/92040822/196711387-a46765f7-20f0-4e45-86a0-d87982a470df.png)

The /turtlesim1/sim node is subscribed to the /turtlesim1/turtle1/cmd_vel topic on the left, to which a hidden node (the ros2 topic pub command you executed) is publishing data. The remainder of the graph demonstrates what was previously stated: mimic publishes to the velocity command topic of /turtlesim2/sim and subscribes to the posture topic of /turtlesim1/sim.

## 5. Summary

Launch files make it easier to execute complicated systems with numerous nodes and intricate configurations. Using the ros2 launch command, launch files created in Python, XML, or YAML can be executed.

# Integrating launch files into ROS2 packages

## 1. Create a package
Make a living environment for the package at your workspace:

```
mkdir -p launch_ws/src
cd launch_ws/src
```

```
ros2 pkg create py_launch_example --build-type ament_python
```

![image](https://user-images.githubusercontent.com/92040822/196713918-e6bfbe1a-e7d3-4ece-b569-776a643519c9.png)

## 2. Creating the structure to hold launch files

The directory that houses your package should have the following structure for Python packages:

```
src/
  py_launch_example/
    package.xml
    py_launch_example/
    resource/
    setup.py
    setup.cfg
    test/
```

We must tell Python's setup tools about our launch files using the data files setup option in order for colcon to discover the launch files.

Inside our setup.py file:

```
import os
from glob import glob
from setuptools import setup

package_name = 'py_launch_example'

setup(
    # Other parameters ...
    data_files=[
        # ... Other data files
        # Include all launch files.
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
    ]
)
```

## 3. Writing the Launch 

Create a new launch file with the name my_script_launch.py inside of your launch directory.

The generate launch description() function, which produces a launch.LaunchDescription() that the ros2 launch verb can utilize, should be defined in your launch file.

```
import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='demo_nodes_cpp',
            executable='talker',
            name='talker'),
  ])
```

## 4. Building and running the launch file

Go to the workspace's top level and construct it:

```
colcon build
```

![image](https://user-images.githubusercontent.com/92040822/196971132-d9b4a896-8ee7-4522-b433-f1833038fcde.png)

You should be able to run the launch file as follows once the colcon build has been successful and you've sourced the workspace:

```
ros2 launch py_launch_example my_script_launch.py
```

# Using substitutions

## 1. Create and setup the package

Make a launch tutorial package of build_type ament_python.

```
ros2 pkg create launch_tutorial --build-type ament_python
```

Make a directory called launch inside of the package.

```
mkdir launch_tutorial/launch
```

![image](https://user-images.githubusercontent.com/92040822/196972159-af6efe98-1868-4f99-985b-7a9686baea84.png)

Changes should be made to the package's setup.py file to ensure the installation of the launch files:

```
import os
from glob import glob
from setuptools import setup

package_name = 'launch_tutorial'

setup(
    # Other parameters ...
    data_files=[
        # ... Other data files
        # Include all launch files.
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
    ]
)
```

## 2. Parent launch file

Make a file called example_main.launch.py and place it in the launch folder of the launch tutorial package.

```
from launch_ros.substitutions import FindPackageShare

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution


def generate_launch_description():
    colors = {
        'background_r': '200'
    }

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('launch_tutorial'),
                    'example_substitutions.launch.py'
                ])
            ]),
            launch_arguments={
                'turtlesim_ns': 'turtlesim2',
                'use_provided_red': 'True',
                'new_background_r': TextSubstitution(text=str(colors['background_r']))
            }.items()
        )
    ])
```

## 3. Substitutions example launch file

Create a file called example substitutions.launch.py in the same folder now.

```
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression


def generate_launch_description():
    turtlesim_ns = LaunchConfiguration('turtlesim_ns')
    use_provided_red = LaunchConfiguration('use_provided_red')
    new_background_r = LaunchConfiguration('new_background_r')

    turtlesim_ns_launch_arg = DeclareLaunchArgument(
        'turtlesim_ns',
        default_value='turtlesim1'
    )
    use_provided_red_launch_arg = DeclareLaunchArgument(
        'use_provided_red',
        default_value='False'
    )
    new_background_r_launch_arg = DeclareLaunchArgument(
        'new_background_r',
        default_value='200'
    )

    turtlesim_node = Node(
        package='turtlesim',
        namespace=turtlesim_ns,
        executable='turtlesim_node',
        name='sim'
    )
    spawn_turtle = ExecuteProcess(
        cmd=[[
            'ros2 service call ',
            turtlesim_ns,
            '/spawn ',
            'turtlesim/srv/Spawn ',
            '"{x: 2, y: 2, theta: 0.2}"'
        ]],
        shell=True
    )
    change_background_r = ExecuteProcess(
        cmd=[[
            'ros2 param set ',
            turtlesim_ns,
            '/sim background_r ',
            '120'
        ]],
        shell=True
    )
    change_background_r_conditioned = ExecuteProcess(
        condition=IfCondition(
            PythonExpression([
                new_background_r,
                ' == 200',
                ' and ',
                use_provided_red
            ])
        ),
        cmd=[[
            'ros2 param set ',
            turtlesim_ns,
            '/sim background_r ',
            new_background_r
        ]],
        shell=True
    )

    return LaunchDescription([
        turtlesim_ns_launch_arg,
        use_provided_red_launch_arg,
        new_background_r_launch_arg,
        turtlesim_node,
        spawn_turtle,
        change_background_r,
        TimerAction(
            period=2.0,
            actions=[change_background_r_conditioned],
        )
    ])
```

## 4. Build the package

Go to the workspace's root and create the package:

```
colcon build
```

![image](https://user-images.githubusercontent.com/92040822/196974298-1b77d237-310d-464a-998f-ac0f9d7e805d.png)


## 5. Launching example

Now you can use the ros2 launch command to launch the example_main.launch.py file.

```
ros2 launch launch_tutorial example_main.launch.py
```

It will accomplish the following:

- Start a blue-background turtlesim node.

- Produce a second turtle

- Purple should be used instead.

- If the provided background r parameter is 200 and the use provided red argument is True, change the color to pink after two seconds.

![image](https://user-images.githubusercontent.com/92040822/196980509-753a8f41-000d-492e-9e31-9b226fb52590.png)

![image](https://user-images.githubusercontent.com/92040822/196980609-bde01bbb-8997-4fd2-8924-f2ed8a62cb84.png)

## 6. Modifying launch arguments

If you want to modify the default launch arguments, you may either do so in the example main.launch.py launch arguments dictionary.

```
ros2 launch launch_tutorial example_substitutions.launch.py --show-args
```

This displays the launch file's possible arguments along with their default values.

```
Arguments (pass arguments as '<name>:=<value>'):

    'turtlesim_ns':
        no description given
        (default: 'turtlesim1')

    'use_provided_red':
        no description given
        (default: 'False')

    'new_background_r':
        no description given
        (default: '200')
```

![image](https://user-images.githubusercontent.com/92040822/196980903-c9221afe-6523-4cdf-8d50-65369b05b175.png)

The launch file can now receive the following arguments:

```
ros2 launch launch_tutorial example_substitutions.launch.py turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200
```

![image](https://user-images.githubusercontent.com/92040822/196981113-5ec82b0b-87b4-4b0f-bb39-7ff82615a7c2.png)

![image](https://user-images.githubusercontent.com/92040822/196981266-ad252736-7c62-414d-8742-63596f8cfea6.png)

## 7. Summary

This tutorial taught me how to use replacements in launch files and how to make reusable launch files using them.

# Using Event Handlers

## Event handler example launch file

We added a new file called "example_event_handlers.launch.py" to the same directory, i.e. inside the "launch" folder of the "launch tutorial" package.

```
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, EmitEvent, ExecuteProcess,
                            LogInfo, RegisterEventHandler, TimerAction)
from launch.conditions import IfCondition
from launch.event_handlers import (OnExecutionComplete, OnProcessExit,
                                OnProcessIO, OnProcessStart, OnShutdown)
from launch.events import Shutdown
from launch.substitutions import (EnvironmentVariable, FindExecutable,
                                LaunchConfiguration, LocalSubstitution,
                                PythonExpression)


def generate_launch_description():
    turtlesim_ns = LaunchConfiguration('turtlesim_ns')
    use_provided_red = LaunchConfiguration('use_provided_red')
    new_background_r = LaunchConfiguration('new_background_r')

    turtlesim_ns_launch_arg = DeclareLaunchArgument(
        'turtlesim_ns',
        default_value='turtlesim1'
    )
    use_provided_red_launch_arg = DeclareLaunchArgument(
        'use_provided_red',
        default_value='False'
    )
    new_background_r_launch_arg = DeclareLaunchArgument(
        'new_background_r',
        default_value='200'
    )

    turtlesim_node = Node(
        package='turtlesim',
        namespace=turtlesim_ns,
        executable='turtlesim_node',
        name='sim'
    )
    spawn_turtle = ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            ' service call ',
            turtlesim_ns,
            '/spawn ',
            'turtlesim/srv/Spawn ',
            '"{x: 2, y: 2, theta: 0.2}"'
        ]],
        shell=True
    )
    change_background_r = ExecuteProcess(
        cmd=[[
            FindExecutable(name='ros2'),
            ' param set ',
            turtlesim_ns,
            '/sim background_r ',
            '120'
        ]],
        shell=True
    )
    change_background_r_conditioned = ExecuteProcess(
        condition=IfCondition(
            PythonExpression([
                new_background_r,
                ' == 200',
                ' and ',
                use_provided_red
            ])
        ),
        cmd=[[
            FindExecutable(name='ros2'),
            ' param set ',
            turtlesim_ns,
            '/sim background_r ',
            new_background_r
        ]],
        shell=True
    )

    return LaunchDescription([
        turtlesim_ns_launch_arg,
        use_provided_red_launch_arg,
        new_background_r_launch_arg,
        turtlesim_node,
        RegisterEventHandler(
            OnProcessStart(
                target_action=turtlesim_node,
                on_start=[
                    LogInfo(msg='Turtlesim started, spawning turtle'),
                    spawn_turtle
                ]
            )
        ),
        RegisterEventHandler(
            OnProcessIO(
                target_action=spawn_turtle,
                on_stdout=lambda event: LogInfo(
                    msg='Spawn request says "{}"'.format(
                        event.text.decode().strip())
                )
            )
        ),
        RegisterEventHandler(
            OnExecutionComplete(
                target_action=spawn_turtle,
                on_completion=[
                    LogInfo(msg='Spawn finished'),
                    change_background_r,
                    TimerAction(
                        period=2.0,
                        actions=[change_background_r_conditioned],
                    )
                ]
            )
        ),
        RegisterEventHandler(
            OnProcessExit(
                target_action=turtlesim_node,
                on_exit=[
                    LogInfo(msg=(EnvironmentVariable(name='USER'),
                            ' closed the turtlesim window')),
                    EmitEvent(event=Shutdown(
                        reason='Window closed'))
                ]
            )
        ),
        RegisterEventHandler(
            OnShutdown(
                on_shutdown=[LogInfo(
                    msg=['Launch was asked to shutdown: ',
                        LocalSubstitution('event.reason')]
                )]
            )
        ),
    ])
```

## Build the package

Go to the root of the workspace, and build the package:

```
colcon build
```

## Launching example

The example_event_handlers.launch.py file can now be launched using the ros2 launch command after you have finished creating and sourcing the workspace.

```
ros2 launch launch_tutorial example_event_handlers.launch.py turtlesim_ns:='turtlesim3' use_provided_red:='True' new_background_r:=200
```
The results of this will be:

Start a turtlesim node with a blue background while spawning a second turtle and changing the color to purple. If the provided background_r argument is 200 and the use_provided_red argument is True, change the color to pink after two seconds. Shut down the launch file when the turtlesim window is closed.

Additionally, when the turtlesim node starts, the spawn action, the change_background_r action and the change_background_r_conditioned action is executed respectively and the turtlesim node leaves and the launch process is prompted to shut down  which results in notifications to belogged to the console.

![image](https://user-images.githubusercontent.com/92040822/196988780-b6446fd4-3df1-4dfa-b24d-eefb3d0be555.png)

![image](https://user-images.githubusercontent.com/92040822/196988908-43053242-9f9e-4b1f-b020-e22b769220e1.png)

```
Week-7
```

# Managing large projets

## 1. Top-level organization

We will first construct a launch file that will call other launch files. Create a launch_turtlesim.launch.py file in the launch_tutorial package's /launch folder to accomplish this.

```
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
   turtlesim_world_1 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('launch_tutorial'), 'launch'),
         '/turtlesim_world_1.launch.py'])
      )
   turtlesim_world_2 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('launch_tutorial'), 'launch'),
         '/turtlesim_world_2.launch.py'])
      )
   broadcaster_listener_nodes = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('launch_tutorial'), 'launch'),
         '/broadcaster_listener.launch.py']),
      launch_arguments={'target_frame': 'carrot1'}.items(),
      )
   mimic_node = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('launch_tutorial'), 'launch'),
         '/mimic.launch.py'])
      )
   fixed_frame_node = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('launch_tutorial'), 'launch'),
         '/fixed_broadcaster.launch.py'])
      )
   rviz_node = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('launch_tutorial'), 'launch'),
         '/turtlesim_rviz.launch.py'])
      )

   return LaunchDescription([
      turtlesim_world_1,
      turtlesim_world_2,
      broadcaster_listener_nodes,
      mimic_node,
      fixed_frame_node,
      rviz_node
   ])
```

## 2. Parameters
## 2.1 Setting parameters in the launch file

The first thing we'll do is create the launch file that will launch our first turtlesim simulation. In the beginning, make a new file called turtlesim_world_1.launch.py.

```
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, TextSubstitution

from launch_ros.actions import Node


def generate_launch_description():
   background_r_launch_arg = DeclareLaunchArgument(
      'background_r', default_value=TextSubstitution(text='0')
   )
   background_g_launch_arg = DeclareLaunchArgument(
      'background_g', default_value=TextSubstitution(text='84')
   )
   background_b_launch_arg = DeclareLaunchArgument(
      'background_b', default_value=TextSubstitution(text='122')
   )

   return LaunchDescription([
      background_r_launch_arg,
      background_g_launch_arg,
      background_b_launch_arg,
      Node(
         package='turtlesim',
         executable='turtlesim_node',
         name='sim',
         parameters=[{
            'background_r': LaunchConfiguration('background_r'),
            'background_g': LaunchConfiguration('background_g'),
            'background_b': LaunchConfiguration('background_b'),
         }]
      ),
   ])
```

## 2.2 Loading parameters from YAML file

We'll start a new simulation of the turtlesim with a different setup during the second launch. Making a turtlesim_world_2.launch.py file is the next step.

```
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
   config = os.path.join(
      get_package_share_directory('launch_tutorial'),
      'config',
      'turtlesim.yaml'
      )

   return LaunchDescription([
      Node(
         package='turtlesim',
         executable='turtlesim_node',
         namespace='turtlesim2',
         name='sim',
         parameters=[config]
      )
   ])
```

Let's now make turtlesim.yaml, a configuration file that will be loaded by our launch file, in the /config subdirectory of our package.

```
/turtlesim2/sim:
   ros__parameters:
      background_b: 255
      background_g: 86
      background_r: 150
```

## 2.3 Using wildcards in YAML files

Let's now make a new file called turtlesim_world_3.launch.py that is similar to turtlesim_world_2.launch.py and adds a third turtlesim node node.

```
...
Node(
   package='turtlesim',
   executable='turtlesim_node',
   namespace='turtlesim3',
   name='sim',
   parameters=[config]
)
```

We will now make the following changes to the turtlesim.yaml file in the /config folder:

```
/**:
   ros__parameters:
      background_b: 255
      background_g: 86
      background_r: 150
```

## 3. Namespaces

We must first remove the namespace='turtlesim2' line from the turtlesim_world_2.launch.py file because every nested node would immediately inherit that namespace. The launch_turtlesim.launch.py needs to be updated to include the following lines:

```
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

   ...
   turtlesim_world_2 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('launch_tutorial'), 'launch'),
         '/turtlesim_world_2.launch.py'])
      )
   turtlesim_world_2_with_namespace = GroupAction(
     actions=[
         PushRosNamespace('turtlesim2'),
         turtlesim_world_2,
      ]
   )
```
Finally, we change the return LaunchDescription statement's turtlesim_world_2 to turtlesim_world_2_with_namespace. As a result, each node in the turtlesim_world_2.launch.py launch description will have a turtlesim2 namespace.

## 4. Reusing nodes

A broadcaster_listener.launch.py file should now be created.

```
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
   return LaunchDescription([
      DeclareLaunchArgument(
         'target_frame', default_value='turtle1',
         description='Target frame name.'
      ),
      Node(
         package='turtle_tf2_py',
         executable='turtle_tf2_broadcaster',
         name='broadcaster1',
         parameters=[
            {'turtlename': 'turtle1'}
         ]
      ),
      Node(
         package='turtle_tf2_py',
         executable='turtle_tf2_broadcaster',
         name='broadcaster2',
         parameters=[
            {'turtlename': 'turtle2'}
         ]
      ),
      Node(
         package='turtle_tf2_py',
         executable='turtle_tf2_listener',
         name='listener',
         parameters=[
            {'target_frame': LaunchConfiguration('target_frame')}
         ]
      ),
   ])
```

## 5. Remapping

A mimic.launch.py file should now be created.

```
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
   return LaunchDescription([
      Node(
         package='turtlesim',
         executable='mimic',
         name='mimic',
         remappings=[
            ('/input/pose', '/turtle2/pose'),
            ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
         ]
      )
   ])
```

## 6. Config files

Now let's make a turtlesim_rviz.launch.py file.

```
import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
   rviz_config = os.path.join(
      get_package_share_directory('turtle_tf2_py'),
      'rviz',
      'turtle_rviz.rviz'
      )

   return LaunchDescription([
      Node(
         package='rviz2',
         executable='rviz2',
         name='rviz2',
         arguments=['-d', rviz_config]
      )
   ])
```

## 7. Environment Variables

Now let's construct fixed_broadcaster.launch.py, the final launch file in our package.

```
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import EnvironmentVariable, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
   return LaunchDescription([
      DeclareLaunchArgument(
            'node_prefix',
            default_value=[EnvironmentVariable('USER'), '_'],
            description='prefix for node name'
      ),
      Node(
            package='turtle_tf2_py',
            executable='fixed_frame_tf2_broadcaster',
            name=[LaunchConfiguration('node_prefix'), 'fixed_broadcaster'],
      ),
   ])
```

# Running launch files

## 1. Update setup.py

The following lines should be added to setup.py in order to install the launch files from the launch/ folder and the configuration file from the config/ folder. Now, the data files field ought to resemble this:

```
data_files=[
      ...
      (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*.launch.py'))),
      (os.path.join('share', package_name, 'config'),
         glob(os.path.join('config', '*.yaml'))),
   ],
```

## 2. Build and run

Build the package and start the top-level launch file using the following command to view the outcome of our code at last:

```
ros2 launch launch_tutorial launch_turtlesim.launch.py
```

![image](https://user-images.githubusercontent.com/92040822/197096815-775d19ad-e263-49ae-9584-21a383707d55.png)


Use the teleop node to command the turtle1.

```
ros2 run turtlesim turtle_teleop_key
```

![image](https://user-images.githubusercontent.com/92040822/197095974-bbf82568-6e32-4d3a-a4c1-0b78056ef3d3.png)

# Introducing tf2

The objective is to run a turtlesim demo and use a multi-robot example to demonstrate some of the potential of tf2.

## Installing the demo

Install the demonstration packages and any prerequisites.

```
sudo apt-get install ros-foxy-turtle-tf2-py ros-foxy-tf2-tools ros-foxy-tf-transformations
```

![image](https://user-images.githubusercontent.com/92040822/197098236-a4aee543-1864-4b00-955e-20eee30d9478.png)

## Running the demo

Open a new terminal and source your ROS 2 installation after installing the turtle_tf2_py instruction package. then issue the following command:

```
ros2 launch turtle_tf2_py turtle_tf2_demo.launch.py
```

The turtle simulation will begin with two turtles.

![image](https://user-images.githubusercontent.com/92040822/197098789-ee6878bf-dc2e-426d-a70a-e2aac8ef7c27.png)

You should enter the following command into the second terminal window:

```
ros2 run turtlesim turtle_teleop_key
```

You may observe that one turtle follows the turtle you are driving around repeatedly.

![image](https://user-images.githubusercontent.com/92040822/197099203-2e9b655d-fca0-4405-85a6-92d0aaabfc70.png)


## What is taking place?

The three coordinate frames in this demonstration: a world frame, a turtle1 frame, and a turtle2 frame were made using the tf2 library. In this lesson, the turtle coordinate frames are published by a tf2 broadcaster, and the turtle coordinate frames are then compared by a tf2 listener, which then causes one turtle to follow the other.

## tf2 tools

We can examine what tf2 is doing in the background using tf2 tools.

## 1. Using view_frames

view_frames generates a graphic of the frames that tf2 is transmitting over ROS.

```
ros2 run tf2_tools view_frames.py
```

You will see:

```
Listening to tf data during 5 seconds...
Generating graph in frames.pdf file...
```

![image](https://user-images.githubusercontent.com/92040822/197099940-12999863-fbfb-471f-a9ad-1d8fa4b6719e.png)

## 2. Using tf2_echo

The transform between any two frames broadcast over ROS is reported by the function tf2_echo.

Usage:

```
ros2 run tf2_ros tf2_echo [reference_frame] [target_frame]
```

![image](https://user-images.githubusercontent.com/92040822/197100357-86c5d287-2474-42bf-8839-f3f073c11f17.png)

Let’s look at the transform of the turtle2 frame with respect to turtle1 frame which is equivalent to:

```
ros2 run tf2_ros tf2_echo turtle2 turtle1
```

The transform will be visible as soon as the tf2 echo listener receives the frames sent via ROS2.

```
At time 1622031731.625364060
- Translation: [2.796, 1.039, 0.000]
- Rotation: in Quaternion [0.000, 0.000, 0.202, 0.979]
At time 1622031732.614745114
- Translation: [1.608, 0.250, 0.000]
- Rotation: in Quaternion [0.000, 0.000, 0.032, 0.999]
```

![image](https://user-images.githubusercontent.com/92040822/197100423-ac259658-f63f-41ef-848f-248bc91d1492.png)

You can vary the transform as you maneuver your turtle around by moving the two turtles in relation to one another.

## rviz and tf2

Rviz is a visualization tool that is helpful for looking at tf2 frames. Let's use rviz to inspect our turtle frames. Let's start rviz using the -d option and the turtle_rviz.rviz configuration file:

```
ros2 run rviz2 rviz2 -d $(ros2 pkg prefix --share turtle_tf2_py)/rviz/turtle_rviz.rviz
```

![image](https://user-images.githubusercontent.com/92040822/197100915-7b091667-c5c2-48cf-b1f7-714497bb9299.png)

You can view the frames that tf2 broadcasts in the sidebar. The frames will move in rviz as you maneuver the turtle about.

































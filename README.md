# ros_tutorials
1. to run the sample camera:
<pre>
  a) rosrun camera image_pub.py '/home/ixtiyor/Pictures/Screenshot from 2019-10-02 10-52-39.png'
  b) rosrun camera detect_pump.py
  (it is not reading from camera as it's name claiming, you can do it with little change if you want)
</pre>
notes:
1. ubuntu 16.04 is best suited with ros kinetic
2. if you build cv_bridge let it be alone in another workspace
3. always set interpreter as #!/usr/bin/env python
4. for python you dont need to recompile if you have it done once

useful commands:
1. command for initializing workspace
<pre>
catkin_init_workspace
</pre>
2. creating package (node)
<pre>
catkin create pkg ''pkg-name'' --catkin-deps ''dependencies''
</pre>

3. if you want to uninitialize of your workspace use:
<pre>
catkin clean --deinit
</pre>

# facial-recognition-door
Raspberry Pi Camera and OpenCV combined with some basic hardware to model a prototype of a door that unlocks based on facial recognition, thus eliminating the need for keys. Made for Shane Rogers's ENGR 171B class at Santa Clara University in Spring of 2017. Collaborators include Connor Tisch, Asa Jacob, Milan Copic, and Mani Gnanasivam.

Built on Raspberry Pi 2B running Raspbian Jessie Lite.

OpenCV code from following source: https://www.youtube.com/watch?v=1I4gHpctXbU



### Demo Video Here: https://goo.gl/photos/jnfoF5tt3ATrd4zY6

### Picture of the setup next to my laptop:
![1](https://cloud.githubusercontent.com/assets/24536303/25606270/67cdc65e-2ec5-11e7-9c1f-7c3cdd855ead.png)

### Connecting to the Raspberry Pi over VNC:
![2](https://cloud.githubusercontent.com/assets/24536303/25606272/67d0f31a-2ec5-11e7-9236-985352ade65d.png)

### Connecting with default Raspberry Pi Login:
![3](https://cloud.githubusercontent.com/assets/24536303/25606271/67ceec32-2ec5-11e7-9e9f-a3febed467e1.png)

### Running the Python script with sudo: 
![4](https://cloud.githubusercontent.com/assets/24536303/25606274/67dfb594-2ec5-11e7-9325-767f69e07db5.png)

### Fixing a Raspberry Pi Camera driver error:
Command is: sudo modprobe bcm2855-v4l2
Note: Be sure to type this in, not copy paste it. For some reason it only works when it is typed.
![5](https://cloud.githubusercontent.com/assets/24536303/25606275/67e01dea-2ec5-11e7-92cb-1eb379b96913.png)

### Terminal output after button push with no face detected:
![6](https://cloud.githubusercontent.com/assets/24536303/25606277/67e180f4-2ec5-11e7-91ff-c759f40c9d87.png)

### What the camera saw (my ceiling): 
![7](https://cloud.githubusercontent.com/assets/24536303/25606273/67dfaa72-2ec5-11e7-9628-5554b0549a2c.png)

### Output after a few more button pushes:
![8](https://cloud.githubusercontent.com/assets/24536303/25606276/67e0fada-2ec5-11e7-8ce3-25776e77bd8a.png)

### My tired and detected face from the latest button push:
![9](https://cloud.githubusercontent.com/assets/24536303/25606278/67e37954-2ec5-11e7-837e-10477b2411e5.png)


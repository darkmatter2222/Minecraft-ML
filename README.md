# Minecraft-ML

I have a personal goal to build the perfect Minecraft bot with consumer grade hardware. Moonshot? Yes.:sweat_smile:  
This is my second attempt at building this bot, this time I am using my daughter for inspiration. As I watch her grow, she becomes proficient at one task at a time and has some sort of ensemble invoking all these functions and features together. Let’s take the same approach, build one model at a time, and invoke the necessary features as we need them.  

Simple Models:
1. Jumping
2. Obstacle Avoidance  
3. Waypoint

## Jumping
The need to jump exists to navigate terrain. Train a simple model to hop over this pile of wood planks.  
Starting with a playground:  
* ![playground](https://github.com/darkmatter2222/Minecraft-ML/blob/main/selfjumping/images/training_field.png)  
* Run around and collect thousands of images using, [collectfromgame.py](https://github.com/darkmatter2222/Minecraft-ML/blob/main/selfjumping/trainingcollection/collectfromgame.py)  
  * I write mine to an external 1TB SSD (Type C) for "Disposable Flash Memory" as to not ruin my native SSDs  
* One you have ~1GB of "No Action" and "Jumping" images, you are ready to train.  
* Note: For Temoral understadning, I collected and stacked a 2 frame historcal reference, this gives the model temporal understanding as the what your trajectory is. Adding a 2nd frame increases your min data training reqquirement nearly exponentially.  


[keras-tuner](https://github.com/keras-team/keras-tuner) suggests that when we play 


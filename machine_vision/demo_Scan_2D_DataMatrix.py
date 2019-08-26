# Hello World Example
#
# Welcome to the MaixPy IDE!
# 1. Conenct board to computer
# 2. Select board at the top of MaixPy IDE: `tools->Select Board`
# 3. Click the connect buttion below to connect board
# 4. Click on the green run arrow button below to run the script!

import sensor, image, time, lcd, math


lcd.init(freq=15000000)
lcd.rotation(2)
sensor.reset()                      # Reset and initialize the sensor. It will
                                    # run automatically, call sensor.run(0) to stop
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.set_vflip(1)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.
i=0

while(True):
    #clock.tick()                    # Update the FPS clock.
    #img = sensor.snapshot()         # Take a picture and return the image.
    #lcd.display(img)                # Display on LCD
    #print(clock.fps())              # Note: MaixPy's Cam runs about half as fast when connected
                                    # to the IDE. The FPS should increase once disconnected.
    clock.tick()
    img = sensor.snapshot()
    #img.lens_corr(1.8) # 1.8的强度对于2.8mm的镜头来说是好的。
    matrices = img.find_datamatrices()

    for matrix in matrices:
        i=i+1
        img.draw_rectangle(matrix.rect(), color = (0, 255, 0),thiness=3)

        print_args = (matrix.rows(), matrix.columns(), matrix.payload(), (180 * matrix.rotation()) / math.pi, clock.fps())
        print("Matrix [%d:%d], Payload \"%s\", rotation %f (degrees), FPS %f" % print_args)
        img.draw_string(100, 25, matrix.payload(), color = (255, 0, 0), scale = 2, mono_space = False)
        img.draw_string(5, 100, str(i), color=(0,255,0), scale=3)
    if not matrices:
        print("FPS %f" % clock.fps())
    img.draw_string(100, 5, "pl32 Goodboy", color = (200, 200, 200), scale = 2, mono_space = False)
    lcd.display(img)  # Display on LCD

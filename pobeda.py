import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# GPIO pin number where the motor is connected
motor_pin = 24

# Set the pin as output
GPIO.setup(motor_pin, GPIO.OUT)

# Create a PWM object with a frequency of 50 Hz
pwm = GPIO.PWM(motor_pin, 50)

def set_motor_pulse(pulse_us):
    # Ensure the pulse width is within the allowed range (1000 to 2000 microseconds)
    #if pulse_us > 2000:
    #    pulse_us = 2000
    #elif pulse_us < 1000:
    #    pulse_us = 1000
    # Convert pulse width from microseconds to duty cycle percentage
    duty_cycle = (pulse_us / 20000) * 100
    pwm.ChangeDutyCycle(duty_cycle)

# Start PWM with 0% duty cycle
pwm.start(0)

# Calibration
try:
    print("Starting calibration...")
    set_motor_pulse(2000)
    time.sleep(2)  # Hold at minimum for 2 seconds
    set_motor_pulse(1000)
    time.sleep(2)  # Hold at maximum for 2 seconds
    set_motor_pulse(2000)
    time.sleep(4)  # Hold at minimum for 2 seconds
    print("Calibration complete. Motor running at maximum power.")
    
    # Main loop to keep the program running
    while True:
        pass
except KeyboardInterrupt:
    # Handle program interruption (Ctrl+C)
    pass
finally:
    # Stop PWM and clean up GPIO settings
    pwm.stop()
    GPIO.cleanup()
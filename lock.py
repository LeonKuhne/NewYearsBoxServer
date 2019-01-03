import RPi.GPIO as GPIO

OPEN_ANGLE = 10
CLOSE_ANGLE = 2.5
SERVO_PIN = 22

class Lock:
    def __init__(self, state):
        self.state = state
        
        # connect
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SERVO_PIN, GPIO.OUT)
        self.servo = GPIO.PWM(SERVO_PIN, 50) # 50hz frequency

        # setup
        self.servo.start(OPEN_ANGLE) if state.isOpen else self.servo.start(CLOSE_ANGLE)

    def open(self):
        print("opening box")
        self.servo.ChangeDutyCycle(OPEN_ANGLE)
        self.state.open()

    def close(self):
        print("closing box")
        self.servo.ChangeDutyCycle(CLOSE_ANGLE)
        self.state.close()

    def set(self, isOpen):
        self.open() if isOpen else self.close()

    def toggle(self):
        self.set(not self.state.isOpen)

    def end(self):
        GPIO.cleanup()

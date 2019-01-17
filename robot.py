import wpilib
from ctre import WPI_TalonSRX
import navx



class Bob(wpilib.IterativeRobot):

    def robotInit(self):
        # ctre motors defined here
        self.r_motor = WPI_TalonSRX(1)
        self.l_motor = WPI_TalonSRX(2)

        self.stick = wpilib.Joystick(1)

    def teleopPeriodic(self):
        self.r_motor.set(WPI_TalonSRX.ControlMode.PercentOutput, self.stick.getY())




if __name__ == "__main__":
    wpilib.run(Bob)

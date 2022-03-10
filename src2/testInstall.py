from core.base import Base

class TestInstall(Base):
    """Tests the environment install"""

    def initialize(self):
        print("Starting ... ")
    
    def update(self):
        pass

# instantiate this class and run it
TestInstall().run()
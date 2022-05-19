"""Sprite example"""

import math
import pathlib
import sys

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[2])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from geometry.rectangle import RectangleGeometry
from material.sprite import SpriteMaterial
from extras.movement_rig import MovementRig
from extras.grid import GridHelper

class Example(Base):
    """ Example template """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 4])
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0, 1, 5])
        self.scene.add(self.rig)
        geometry = RectangleGeometry()
        tile_set = Texture("images/rolling-ball.jpg")
        sprite_material = SpriteMaterial(tile_set, {
            "billboard" : 1, 
            "tileCount" : [4, 4],
            "tileNumber" : 0 
        })
        self.tiles_per_second = 8

        self.sprite = Mesh(geometry, sprite_material)
        self.scene.add(self.sprite)

        grid = GridHelper()
        grid.rotate_x(math.pi/2)
        self.scene.add(grid)

    def update(self):
        """Animate the rendering"""
        self.renderer.render(self.scene, self.camera)
        tileNumber = math.floor(self.time * self.tiles_per_second)
        self.sprite.material.uniform_dict["tileNumber"].data = tileNumber
        self.rig.update(self.input, self.delta_time)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()

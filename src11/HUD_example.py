"""Example of Heads Up Display (HUD) layer"""
import pathlib
import sys
import math

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
from geometry.box import BoxGeometry
from material.texture import TextureMaterial
from extras.movement_rig import MovementRig
from extras.grid import GridHelper


class Example(Base):
    """ Example template """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0, 0.5, 3])
        self.scene.add(self.rig)

        crate_geometry = BoxGeometry()
        crate_material = TextureMaterial(Texture("images/crate.jpg"))
        crate = Mesh(crate_geometry, crate_material)
        self.scene.add(crate)

        grid = GridHelper(grid_color=[1, 1, 1], center_color=[1, 1, 0])
        grid.rotate_x(math.pi/2)
        self.scene.add(grid)

        # Add the Heads Up Display (HUD) layer
        self.hud_scene = Scene()
        self.hud_camera = Camera()
        self.hud_camera.set_orthographic(0, 800, 0, 600, 1, -1)
        
        label_geolocation_1 = RectangleGeometry(width=600, height=80, position=[0, 600], alignment=[0,1])
        label_material_1 = TextureMaterial(Texture("images/crate-text.jpg"))
        label_1 = Mesh(label_geolocation_1, label_material_1)
        self.hud_scene.add(label_1)

        label_geolocation_2 = RectangleGeometry(width=400, height=80, position=[800, 0], alignment=[1,0])
        label_material_2 = TextureMaterial(Texture("images/version-1.jpg"))
        label_2 = Mesh(label_geolocation_2, label_material_2)
        self.hud_scene.add(label_2)

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(self.hud_scene, self.hud_camera, clear_color=False)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()

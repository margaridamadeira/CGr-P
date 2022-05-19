"""Example of using text in scenes"""

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from geometry.rectangle import RectangleGeometry
from material.texture import TextureMaterial
from extras.text_texture import TextTexture


class Example(Base):
    """
    Demonstrate the use of text
    """
    def initialize(self):
        """Defining example"""
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 1.5])
        geometry = RectangleGeometry()
        message = TextTexture(text="Graphics with Python",
                               system_font_name="Impact",
                               font_size=32, font_color=[0, 0, 200],
                               image_width=256, image_height=256,
                               align_horizontal=0.5, align_vertical=0.5,
                               image_border_width=4,
                               image_border_color=[255, 0, 0])
        material = TextureMaterial(message)
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        self.mesh.rotate_y(0.0114)
        self.mesh.rotate_x(0.0237)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()

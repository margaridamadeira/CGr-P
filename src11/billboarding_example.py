"""Example of billboarding"""

from core.base import Base
from core.matrix import Matrix
from core_ext.mesh import Mesh
from core_ext.camera import Camera
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from geometry.box import BoxGeometry
from geometry.rectangle import RectangleGeometry
from extras.movement_rig import MovementRig
from extras.text_texture import TextTexture
from material.texture import TextureMaterial


class Example(Base):
    """
    Demonstrate the use of look_at in billboarding
    keys: ADRF
    """
    def initialize(self):
        """Defining example"""
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([0, 1, 5])
        self.scene.add(self.rig)

        label_texture = TextTexture(text=" This is a Crate. ",
                                    system_font_name="Arial Bold",
                                    font_size=40, font_color=[0, 0, 200],
                                    image_width=256, image_height=128,
                                    align_horizontal=0.5, align_vertical=0.5,
                                    image_border_width=4,
                                    image_border_color=[255, 0, 0])

        label_material = TextureMaterial(label_texture)
        label_geometry = RectangleGeometry(width=1, height=0.5)
        label_geometry.apply_matrix(Matrix.make_rotation_y(3.14)) # Rotate to face -z
        self.label = Mesh(label_geometry, label_material)
        self.label.set_position([0, 1, 0])
        self.scene.add(self.label)

        crate_geometry = BoxGeometry()
        crate_texture = Texture("images/crate.jpg")
        crate_material = TextureMaterial(crate_texture)
        crate = Mesh(crate_geometry, crate_material)
        self.scene.add(crate)

    def update(self):
        self.rig.update(self.input, self.delta_time)
        self.label.look_at(self.camera.global_position)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()

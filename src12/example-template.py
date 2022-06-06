"""Light example"""

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
# from core_ext.texture import Texture
from geometry.box import BoxGeometry
# from geometry.geometry import Geometry
from geometry.sphere import SphereGeometry
# from material.texture import TextureMaterial
from light.ambient import AmbientLight
from light.directional import DirectionalLight
from light.point import PointLight
from material.surface import SurfaceMaterial
from material.flat import FlatMaterial
from material.lambert import LambertMaterial
from material.phong import PhongMaterial



class Example(Base):
    """ Example template """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.camera.set_position([0, 0, 4])
        geometry = BoxGeometry()
        # material = SurfaceMaterial(property_dict={"useVertexColors": True})
        material = SurfaceMaterial(
            property_dict={
                "useVertexColors": True,
                "wireframe": True,
                "lineWidth": 8
            }
        )
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

    def update(self):
        self.mesh.rotate_y(0.0514)
        self.mesh.rotate_x(0.0337)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()

"""Light example: all light types and material types"""

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.texture import Texture
from core_ext.scene import Scene
from geometry.box import BoxGeometry
# from geometry.geometry import Geometry
from geometry.sphere import SphereGeometry
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
        self.camera.set_position([0, 0, 6])

        # the scene includes a dark gray ambient light, a white directional light, and a red point light.

        ambient = AmbientLight(color=[0.5, 0.5, 0.5])
        self.scene.add(ambient)

        directional = DirectionalLight(color=[0.8, 0.8, 0.8], direction=[-1, -1, -2])
        self.scene.add(directional)

        point = PointLight(color=[0.9, 0, 0], position=[1, 1, 0.8])
        self.scene.add(point)

        sphere_geometry = SphereGeometry()


        # left sphere with a red flat-shaded material
        flat_material = FlatMaterial(property_dict={"baseColor":[0.6, 0.2, 0.2]})
        sphere1 = Mesh(sphere_geometry, flat_material)
        sphere1.set_position([-2.2, 0, 0])

        # middle sphere with a textured Lambert material
        grid = Texture("images/grid.jpg")
        lambert_material = LambertMaterial(texture=grid)
        sphere2 = Mesh(sphere_geometry, lambert_material)
        sphere2.set_position([0, 0, 0])

        # right sphere with a blue-gray Phong material
        phong_material = PhongMaterial(property_dict={"baseColor":[0.5, 0.5, 1]})
        sphere3 = Mesh(sphere_geometry, phong_material)
        sphere3.set_position([2.2, 0, 0])


        # Adding the spheres to the scene
        self.scene.add(sphere1)
        self.scene.add(sphere2) 
        self.scene.add(sphere3) 

    def update(self):
        #self.mesh.rotate_y(0.0514)
        #self.mesh.rotate_x(0.0337)
        self.renderer.render(self.scene, self.camera)


# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()

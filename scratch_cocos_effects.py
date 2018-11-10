import cocos
import cocos.euclid as eu
import cocos.particle_systems as ps

class MainLayer(cocos.layer.Layer):
    def __init__(self):
        super(MainLayer, self).__init__()
        particles = ps.Spiral()
        particles.position = (512, 300)
        self.add(particles)


if __name__ == '__main__':
    cocos.director.director.init(caption='Particle example',
                                 width=1024,
                                 height= 600
                                 )
    scene = cocos.scene.Scene(MainLayer())
    cocos.director.director.run(scene)

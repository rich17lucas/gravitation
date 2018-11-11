import cocos
import cocos.euclid as eu
import cocos.particle_systems as ps

class MainLayer(cocos.layer.Layer):
    def __init__(self):
        super(MainLayer, self).__init__()
        candle1 = ps.Fireworks()
        candle1.position = (512, 100)
        candle1.angle = 60

        candle2 = ps.Fireworks()
        candle2.position = (490, 100)
        candle2.angle = 120
        candle2.speed = 270
        candle2.speed_var = 100
        candle2.radial_accel=2


        self.add(candle1)
        self.add(candle2)


if __name__ == '__main__':
    cocos.director.director.init(caption='Particle example',
                                 width=1024,
                                 height= 600
                                 )
    scene = cocos.scene.Scene(MainLayer())
    cocos.director.director.run(scene)

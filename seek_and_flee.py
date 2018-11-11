import cocos
import cocos.euclid as eu
import cocos.particle_systems as ps
import sys


class Actor(cocos.cocosnode.CocosNode):
    def __init__(self, x, y, behaviour):
        super(Actor, self).__init__()
        self.position = (x, y)
        self.velocity = eu.Vector2(0, 0)
        self.speed = 2
        self.max_force = 5
        self.max_velocity = 200
        self.target = None
        self.add(ps.Sun())
        self.schedule(self.update)
        self._behaviour = 1 if behaviour == "seek" else -1

    def update(self, dt):
        if self.target is None:
            return
        distance = self.target - eu.Vector2(self.x, self.y)
        steering = distance * self.speed - self.velocity
        steering = self.truncate(steering, self.max_force)
        self.velocity = self.truncate(self.velocity + steering, self.max_velocity)
        self.position += self.velocity * dt * self._behaviour

    @staticmethod
    def truncate(vector, m):
        magnitude = abs(vector)
        if magnitude > m:
            vector *= m / magnitude
        return vector


class MainLayer(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self, behaviour):
        super(MainLayer, self).__init__()
        self.actor = Actor(320, 240, behaviour)
        self.add(self.actor)

    def on_mouse_motion(self, x, y, dx, dy):
        self.actor.target = eu.Vector2(x, y)


if __name__ == '__main__':

    if len(sys.argv) == 2:
        cocos.director.director.init(caption='Steering Behaviours')
        scene = cocos.scene.Scene(MainLayer(sys.argv[1]))
        cocos.director.director.run(scene)
    else:
        print("Usage: seek_and_flee.py seek|flee")
        sys.exit(99)


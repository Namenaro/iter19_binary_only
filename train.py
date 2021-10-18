def train():
    world = World()
    net = Net()
    while not stop_condition(net, world):
      do_train_step(world, net)
    return net


def do_train_step(world, net):
    etalon = world.get_random_train_3()
    ...
    net.add_new_node()
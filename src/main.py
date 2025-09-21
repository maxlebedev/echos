
EntityId = int
ComponentId = int
Type = list[ComponentId]


class Archetype:
    type: Type
    type_set: set[ComponentId]

    def __init__(self, *args):
        self.type = [a for a in args]
        self.type_set = set(self.type)


# TODO: class Index. Index.archetype
class State:
    entity_index: dict[EntityId, Archetype] = {}
    archetype_index: dict[Type, Archetype] = {}


def has_component(entity: EntityId, component: ComponentId) -> bool:
    archetype = State.entity_index[entity]
    return component in archetype.type_set


def test_component():
    pos: ComponentId = 1
    hp: ComponentId = 2
    vis: ComponentId = 3
    arch1 = Archetype(pos, hp)
    ent1 = 1
    State.entity_index[ent1] = arch1

    assert has_component(ent1, pos)
    assert has_component(ent1, hp)
    assert not has_component(ent1, vis)


def main():
    test_component()


if __name__ == "__main__":
    main()

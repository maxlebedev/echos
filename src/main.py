from collections import defaultdict

EntityId = int

ComponentId = int
Type = list[ComponentId]

ArchetypeId = int
ArchetypeRecord = int
ArchetypeDict = dict[ArchetypeId, ArchetypeRecord]


class Archetype:
    id: ArchetypeId
    type: Type

    def __init__(self, *args):
        self.id = id(self)
        self.type = [a for a in args]
        for arg in args:
            arch_dict = State.component_index[arg]
            arch_dict[self.id] = len(arch_dict)


# TODO: class Index. Index.archetype
class State:
    entity_index: dict[EntityId, Archetype] = {}
    archetype_index: dict[Type, Archetype] = {}
    component_index: dict[ComponentId, ArchetypeDict] = defaultdict(dict)


def has_component(entity: EntityId, component: ComponentId) -> bool:
    archetype = State.entity_index[entity]
    return archetype.id in State.component_index[component]


def get_component(entity: EntityId, component: ComponentId) -> int:
    # TODO: returning component ID bc that's all we have rn
    arch_dict = State.component_index[component]
    arch = State.entity_index[entity]
    column = arch_dict[arch.id]
    return arch.type[column]


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

    assert get_component(ent1, pos) == pos


def main():
    test_component()


if __name__ == "__main__":
    main()

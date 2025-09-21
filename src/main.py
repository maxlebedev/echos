from collections import defaultdict

EntityId = int
ComponentId = int
ArchetypeId = int
Type = list[ComponentId]
ArchetypeSet = set[ArchetypeId]


class Archetype:
    id: ArchetypeId
    type: Type

    def __init__(self, *args):
        self.id = id(self)
        self.type = [a for a in args]
        for arg in args:
            State.component_index[arg].add(self.id)


# TODO: class Index. Index.archetype
class State:
    entity_index: dict[EntityId, Archetype] = {}
    archetype_index: dict[Type, Archetype] = {}
    component_index: dict[ComponentId, ArchetypeSet] = defaultdict(set)


def has_component(entity: EntityId, component: ComponentId) -> bool:
    archetype = State.entity_index[entity]
    return archetype.id in State.component_index[component]


def has_components(entity: EntityId, *components: ComponentId) -> bool:
    archetype_sets = [State.component_index[cmp] for cmp in components]
    archetypes = set.intersection(*archetype_sets)
    return State.entity_index[entity].id in archetypes


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

    assert has_components(ent1, pos, hp)
    assert not has_components(ent1, pos, vis)


def main():
    test_component()


if __name__ == "__main__":
    main()

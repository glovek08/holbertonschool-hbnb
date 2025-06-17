class InMemoryRepository:
       def __init__(self):
           self.storage = {}

       def add(self, entity):
           self.storage[str(entity.id)] = entity

       def get(self, entity_id):
           return self.storage.get(str(entity_id))

       def get_by_attribute(self, attribute, value):
           for entity in self.storage.values():
               if getattr(entity, attribute) == value:
                   return entity
           return None
import graphene
from graphene.types.json import JSONString
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Fleetmanager, Datasubmanager


class Jsonify(JSONString):
    
    class Meta:
        description = "Returns a json object"
    
    @staticmethod
    def serialize(dt):
        return dt
    

class FleetmanagerObject(SQLAlchemyObjectType):
    
    fleet_id = graphene.Field(Jsonify)
    def resolve_fleets(self, args): 
        return self.fleet_id
    
    actions = graphene.Field(Jsonify)
    def resolve_actions(self, args): 
        return self.actions

    class Meta:
        model = Fleetmanager
        exclude_fields = ('id', 'fleetmanager_id', 'fleet_id', 'actions')

        
class DatasubmanagerObject(SQLAlchemyObjectType):
        
    actions = graphene.Field(Jsonify)
    def resolve_actions(self, args): 
        return self.actions

    class Meta:
        model = Datasubmanager
        exclude_fields = ('id', 'datasubmanager_id', 'actions')

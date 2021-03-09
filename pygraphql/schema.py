# encoding=utf-8
from graphene import Argument, Field, String, Schema, Union, ObjectType
from objects import FleetmanagerObject, DatasubmanagerObject, Jsonify


class Query(ObjectType):

    class Meta:
        description = "The following fields are available in the query. Provide them inside \{ \}."    
    
    fleetmanagers = Field(FleetmanagerObject,
                          fleetmanager_id=Argument(type=String, required=True, description = 'The fleet manager id of the fleet'),
                          description='Displays the available fleets and actions for a given fleet manager ')
    @staticmethod
    def resolve_fleetmanagers(self, context, **kwargs):
        query = FleetmanagerObject.get_query(context)
        query = query.filter_by(**kwargs)
        return query.first()
    
    
    datasubmanagers = Field(DatasubmanagerObject,
                          datasubmanager_id=Argument(type=String, required=True, description = 'The data sub manager id of the fleet'),
                          description='Displays the available fleets and actions for a given data sub manager ')
    @staticmethod
    def resolve_datasubmanagers(self, context, **kwargs):
        query = DatasubmanagerObject.get_query(context)
        query = query.filter_by(**kwargs)
        return query.first()
        
        
schema = Schema(query=Query, auto_camelcase=False)

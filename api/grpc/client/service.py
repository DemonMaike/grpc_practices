# api/grpc/client/service.py

from api.grpc.generated.client import client_pb2, client_pb2_grpc
import grpc

class ClientService(client_pb2_grpc.ClientServiceServicer):
    def CreateClient(self, request, context):
        if not request.name:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "name is required")
        if not request.email:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "email is required")

        return client_pb2.ClientReply(id="123", status="created")
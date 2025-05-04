import grpc
from concurrent import futures
from api.grpc.generated.client import client_pb2_grpc
from api.grpc.generated.order import order_pb2_grpc
from api.grpc.generated.account import account_pb2_grpc
from api.grpc.client.service import ClientService
from api.grpc.order.service import OrderService
from api.grpc.account.service import AccountService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    client_pb2_grpc.add_ClientServiceServicer_to_server(ClientService(), server)
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    account_pb2_grpc.add_AccountServiceServicer_to_server(AccountService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running at localhost:50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
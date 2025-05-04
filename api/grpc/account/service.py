import grpc
from api.grpc.generated.account import account_pb2, account_pb2_grpc

class AccountService(account_pb2_grpc.AccountServiceServicer):
    def GetBalance(self, request, context):
        if not request.client_id:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "client_id is required")
        return account_pb2.AccountReply(balance=1234.56)
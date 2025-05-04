from api.grpc.generated.order import order_pb2, order_pb2_grpc
import grpc

class OrderService(order_pb2_grpc.OrderServiceServicer):
    def CreateOrder(self, request, context):
        if not request.client_id:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "client_id is required")
        if not request.product:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "product is required")
        if request.quantity <= 0:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "quantity must be greater than zero")

        return order_pb2.OrderReply(order_id="order123", status="created")

    def GetOrder(self, request, context):
        if not request.order_id:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "order_id is required")

        return order_pb2.OrderReply(order_id=request.order_id, status="shipped")

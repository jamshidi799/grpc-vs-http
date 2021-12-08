from concurrent import futures
import threading
import grpc
import product_pb2_grpc
import product_pb2
from app import app


class ProductServer(product_pb2_grpc.ProductServicer):
    visit_count = 0

    def update(self, request, context):
        self.visit_count += 1
        print(request.title)
        print(type(request))
        return product_pb2.ProductStatsProto(visit_count=self.visit_count)


def start_grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor())

    product_pb2_grpc.add_ProductServicer_to_server(ProductServer(), server)

    server.add_insecure_port('[::]:50051')
    print("------------------start Python GRPC server------------------")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    threading.Thread(target=start_grpc_server).start()
    app.run(debug=False, port=5000)

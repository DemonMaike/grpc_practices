
Простой учебный проект с gRPC на Python. Включает три сервиса: `Client`, `Account`, `Order`.

---

## 📁 Структура проекта

```
grpc_practices/
├── api/
│   └── grpc/
│       ├── client/
│       │   └── client.proto
│       ├── account/
│       │   └── account.proto
│       ├── order/
│       │   └── order.proto
│       └── generated/
│           └── ... (сгенерированные .py-файлы)
├── server.py
├── README.md
```

---

## 🚀 Запуск сервера

```bash
python server.py
```

По умолчанию сервер запускается на `localhost:50051`.

---

## ⚙️ Генерация Python-файлов из `.proto`

```bash
python -m grpc_tools.protoc \
  -I api/grpc \
  --python_out=api/grpc/generated \
  --grpc_python_out=api/grpc/generated \
  api/grpc/client/client.proto \
  api/grpc/account/account.proto \
  api/grpc/order/order.proto
```
```powershell
python -m grpc_tools.protoc -I api/grpc --python_out=api/grpc/generated --grpc_python_out=api/grpc/generated api/grpc/client/client.proto api/grpc/account/account.proto api/grpc/order/order.proto
```

---

## 🔬 Тестирование через Postman

Для удобного тестирования используйте **Postman** с gRPC:

1. В Postman создайте новый **gRPC запрос**.
2. Укажите адрес: `localhost:50051`.
3. Импортируйте `.proto` файл через **"Setup" → "Import .proto file"**.
4. Выберите нужный сервис и метод.
5. Укажите входные данные в формате JSON.

### Пример запроса: `CreateClient`

```
Service: ClientService
Method: CreateClient
```

```json
{
  "name": "Mr. Freeman",
  "email": "freeman@world.com"
}
```

---

## 📌 Сервисы и методы

* **ClientService**

  * `CreateClient(ClientRequest) → ClientReply`
* **AccountService**

  * `GetBalance(AccountRequest) → AccountReply`
* **OrderService**

  * `CreateOrder(OrderRequest) → OrderReply`
  * `GetOrder(OrderId) → OrderReply`


# 📝 TodoList Backend Service

This is the backend service for a **TodoList** application, built using **FastAPI**, **PostgreSQL**, **Kafka**, and **Docker**.  
The service provides a **RESTful API** for managing tasks, with Kafka handling asynchronous task processing.

## 🚀 Technologies Used

- **FastAPI** – Web framework for building APIs
- **PostgreSQL** – Database for storing tasks
- **Kafka** – Message broker for handling task events
- **Docker** – Containerization for easy deployment

## 📞 Setup & Installation

### 1️⃣ Clone the repository

```sh
git clone https://github.com/HuynhNhatKhanh/todolist-python.git
cd todolist-python
```

### 2️⃣ Set up environment variables

Create a `.env` file and configure database & Kafka settings:

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_DB=admin
```

### 3️⃣ Run with Docker

Make sure you have **Docker** and **Docker Compose** installed. Then, start the services:

```sh
docker-compose up --build
```

### 4️⃣ Run without Docker

If running manually, install dependencies and start the service:

```sh
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 5️⃣ Start the Kafka Consumer

```sh
python kafka_consumer.py
```

## 📌 API Endpoints

| Method   | Endpoint     | Description             |
| -------- | ------------ | ----------------------- |
| `POST`   | `/task`      | Create a new task       |
| `GET`    | `/task/{id}` | Get task details by ID  |
| `GET`    | `/task`      | List all tasks          |
| `PUT`    | `/task/{id}` | Update an existing task |
| `DELETE` | `/task/{id}` | Delete a task           |

## 🛠 Contributing

1. Fork the repo
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to your branch (`git push origin feature-name`)
5. Open a Pull Request 🚀

## 🐟 License

This project is licensed under the **MIT License**.

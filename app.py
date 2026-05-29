from flask import Flask, request, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


# -----------------------------
# CONEXÃO COM BANCO
# -----------------------------
def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASS", ""),
            database=os.getenv("DB_NAME", "test")
        )
        return conn
    except mysql.connector.Error as err:
        print("Erro ao conectar no MySQL:", err)
        return None


# -----------------------------
# ROTA PRINCIPAL
# -----------------------------
@app.route("/")
def home():
    return jsonify({"msg": "API rodando 🚀"})


# -----------------------------
# CRIAR CLIENTE
# -----------------------------
@app.route("/clientes", methods=["POST"])
def criar_cliente():
    data = request.get_json()

    if not data or not data.get("nome") or not data.get("email"):
        return jsonify({"erro": "nome e email são obrigatórios"}), 400

    conn = get_connection()
    if not conn:
        return jsonify({"erro": "falha na conexão com banco"}), 500

    try:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (%s, %s)",
            (data["nome"], data["email"])
        )

        conn.commit()
        return jsonify({"msg": "cliente criado com sucesso"}), 201

    except mysql.connector.Error as err:
        return jsonify({"erro": str(err)}), 500

    finally:
        cursor.close()
        conn.close()


# -----------------------------
# LISTAR CLIENTES
# -----------------------------
@app.route("/clientes", methods=["GET"])
def listar_clientes():

    conn = get_connection()
    if not conn:
        return jsonify({"erro": "falha na conexão com banco"}), 500

    try:
        cursor = conn.cursor()

        cursor.execute("SELECT id, nome, email FROM clientes")
        rows = cursor.fetchall()

        clientes = [
            {"id": r[0], "nome": r[1], "email": r[2]}
            for r in rows
        ]

        return jsonify(clientes)

    except mysql.connector.Error as err:
        return jsonify({"erro": str(err)}), 500

    finally:
        cursor.close()
        conn.close()


# -----------------------------
# START APP
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

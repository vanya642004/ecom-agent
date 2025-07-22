from flask import Flask, request, jsonify
import sqlite3
from llama_cpp import Llama

app = Flask(__name__)
llm = Llama(model_path="models/llama-2-7b-chat.gguf")
DB = 'ecom.db'

def to_sql(question):
    prompt = (
        "Translate to SQL for tables ad_sales, total_sales, eligibility.\n"
        f"Question: {question}\nSQL:"
    )
    resp = llm(prompt=prompt, max_tokens=256)
    return resp.choices[0].text.strip()

def exec_sql(sql):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    conn.close()
    return cols, rows

@app.route('/api/query', methods=['POST'])
def query():
    q = request.json.get('question','')
    sql = to_sql(q)
    cols, rows = exec_sql(sql)
    return jsonify({'sql': sql, 'columns': cols, 'rows': rows})

if __name__=='__main__':
    app.run(debug=True)

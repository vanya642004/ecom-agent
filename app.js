document.getElementById('ask').onclick = async ()=>{
  const q = document.getElementById('question').value;
  const r = document.getElementById('result');
  r.textContent = '⏳ Thinking…';
  const res = await fetch('/api/query', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({question:q})
  });
  const d = await res.json();
  r.textContent = 
    `SQL ▶︎ ${d.sql}\n\n` +
    `${d.columns.join('\t')}\n` +
    d.rows.map(r=>r.join('\t')).join('\n');
};

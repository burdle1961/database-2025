import React, { useState } from "react";

function App() {
  const [order, setOrder] = useState("");
  const [orders, setOrders] = useState([]);

  const handleSearch = async () => {
    const res = await fetch(`http://127.0.0.1:5000/search?order=${order}`);
    const data = await res.json();
    setOrders(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>주문 조회</h2>
      <input
        type="number"
        value={order}
        onChange={(e) => setOrder(e.target.value)}
        placeholder="주문 번호"
      />
      <button onClick={handleSearch}>조회</button>

      <table border="1" className="order-table">
        <thead>
          <tr>
            <th>주문번호</th>
            <th>고객번호</th>
            <th>주문날짜</th>
            <th>배송날짜</th>
            <th>상태</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((o, idx) => (
            <tr key={idx}>
              <td>{o.주문번호}</td>
              <td>{o.고객번호}</td>
              <td>{o.주문날짜}</td>
              <td>{o.배송날짜}</td>
              <td>{o.상태}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;

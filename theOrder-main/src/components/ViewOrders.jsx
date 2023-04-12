const ViewOrders = ({ onClose, orders }) => {

  return (
    <div className="modal">
      <div className="modal-content">
        <button className="modal-close" onClick={onClose}>
          &times;
        </button>
        <h2>Lista de pedidos</h2>
        <div className="orders-container">
          <table className="orders-table">
            <thead>
              <tr>
                <th>Tipo de taco</th>
                <th>Cantidad</th>
                <th>Para llevar</th>
                <th>Estado</th>
              </tr>
            </thead>
            <tbody>
              {orders.map((order, index) => (
                <tr key={index}>
                  <td>{order.type}</td>
                  <td>{order.quantity}</td>
                  <td>{order.toGo ? 'Sí' : 'No'}</td>
                  <td>{order.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default ViewOrders;

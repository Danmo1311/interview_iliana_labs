import "./App.css";
import { useEffect, useState } from "react";
import CreateOrder from "./components/CreateOrder";
import ViewOrders from "./components/ViewOrders";

function App() {
  const [orders, setOrders] = useState([]);
  const [showOrders, setShowOrders] = useState(false);
  const [showCreateOrder, setShowCreateOrder] = useState(false);

  useEffect(() => {
     const fetchOrders = async () => {
      const response = await fetch("http://localhost:8000/pedidos");
      const data = await response.json();
      setOrders(data);
    };
    fetchOrders();
    setOrders([
      { type: 'Beef', cantidad: 1, para_llevar: false, estado: 'pendiente' },
      { type: 'Chicken', cantidad: 2, para_llevar: true, estado: 'preparando' },
      { type: 'Pork', cantidad: 3, para_llevar: false, estado: 'listo' },
      { type: 'Veggie', cantidad: 2, para_llevar: true, estado: 'pendiente' },
      { type: 'Fish', cantidad: 1, para_llevar: false, estado: 'preparando' },
      { type: 'Shrimp', cantidad: 2, para_llevar: false, estado: 'listo' },
      { type: 'Carnitas', cantidad: 3, para_llevar: false, estado: 'preparando' },
      { type: 'Al Pastor', cantidad: 2, para_llevar: true, estado: 'pendiente' },
      { type: 'Barbacoa', cantidad: 1, para_llevar: false, estado: 'listo' },
      { type: 'Lengua', cantidad: 2, para_llevar: false, estado: 'preparando' },
    ]) ;
  }, []);
  
  
    
  const handleCreateOrder = () => {
    setShowCreateOrder(!showCreateOrder);
  };

  const handleViewOrders = () => {
    setShowOrders(!showOrders);
  };


  const handleOnCloseCreate = () => {
    setShowCreateOrder(false);
  };

  const handleOnCloseView = () => {
    setShowOrders(false);
  };

  return (
    <div className="App">
      <>
        <header>
          <h1>The Order</h1>
        </header>
        <main className="container">
          <button className="button" onClick={handleCreateOrder}>
            Create Order
          </button>
          <button className="button" onClick={handleViewOrders}>
            View Orders
          </button>
        </main>
      </>
      { showCreateOrder && <CreateOrder  onClose={handleOnCloseCreate} /> }
      { showOrders && <ViewOrders orders={orders} onClose={handleOnCloseView}/> }
    </div>
  );
}

export default App;

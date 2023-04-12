import "./App.css";
import { useEffect, useState } from "react";
import CreateOrder from "./components/CreateOrder";
import ViewOrders from "./components/ViewOrders";

function App() {
  const [orders, setOrders] = useState([]);
  const [showOrders, setShowOrders] = useState(false);
  const [showCreateOrder, setShowCreateOrder] = useState(false);

  useEffect(() => {
    /* const fetchOrders = async () => {
      const response = await fetch("http://localhost:4000/orders");
      const data = await response.json();
      setOrders(data);
    };
    fetchOrders(); */
    setOrders([
      { type: 'Beef', quantity: 1, toGo: false, status: 'pendiente' },
      { type: 'Chicken', quantity: 2, toGo: true, status: 'preparando' },
      { type: 'Pork', quantity: 3, toGo: false, status: 'listo' },
      { type: 'Veggie', quantity: 2, toGo: true, status: 'pendiente' },
      { type: 'Fish', quantity: 1, toGo: false, status: 'preparando' },
      { type: 'Shrimp', quantity: 2, toGo: false, status: 'listo' },
      { type: 'Carnitas', quantity: 3, toGo: false, status: 'preparando' },
      { type: 'Al Pastor', quantity: 2, toGo: true, status: 'pendiente' },
      { type: 'Barbacoa', quantity: 1, toGo: false, status: 'listo' },
      { type: 'Lengua', quantity: 2, toGo: false, status: 'preparando' },
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

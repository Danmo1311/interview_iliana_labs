import React,{ useState, useRef } from 'react';
import useOutsideClick from '../hooks/useOutsideClick';

const CreateOrder = ({onClose}) => {
  const wrapperRef = useRef();
  useOutsideClick({
    ref: wrapperRef,
    onClickOutside: onClose,
  });
;
  const [tacoType, setTacoType] = useState('beef');
  const [tacoQuantity, setTacoQuantity] = useState(1);
  const [tacoToGo, setTacoToGo] = useState(false);

  const handleOrderSubmit = () => {
    console.log('Order submitted:', tacoType, tacoQuantity, tacoToGo);
    onClose();
  };

  const handleTacoTypeChange = (event) => {
    setTacoType(event.target.value);
  };
  const handleTacoQuantityChange = (event) => {
    setTacoQuantity(parseInt(event.target.value));
  };
  const handleToGoChange = (event) => {
    setTacoToGo(event.target.checked);
  };
  return (
    <div className="modal" ref={wrapperRef}>
      <button className="close" onClick={onClose}>
        &times;
      </button>
    <div className="modal-content" >
      <h2>Order tacos</h2>
      <form>
        <div>
          <label htmlFor="taco-type">Type:</label>
          <select id="taco-type" value={tacoType} onChange={handleTacoTypeChange}>
            <option value="Beef">Beef</option>
            <option value="Chicken">Chicken</option>
            <option value="Pork">Pork</option>
          </select>
        </div>
        <div>
          <label htmlFor="taco-quantity">Quantity:</label>
          <input
            id="taco-quantity"
            type="number"
            min="1"
            value={tacoQuantity}
            onChange={handleTacoQuantityChange}
          />
        </div>
        <div>
          <label htmlFor="taco-to-go">To go:</label>
          <input id="taco-to-go" type="checkbox" checked={tacoToGo} onChange={handleToGoChange} />
        </div>
      </form>
      <div className="modal-actions">
        <button onClick={onClose}>Cancel</button>
        <button onClick={handleOrderSubmit}>Order</button>
      </div>
    </div>
  </div>
  )
}

export default CreateOrder
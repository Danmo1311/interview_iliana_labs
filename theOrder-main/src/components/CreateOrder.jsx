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
  const [tacocantidad, setTacocantidad] = useState(1);
  const [tacopara_llevar, setTacopara_llevar] = useState(false);

  const handleOrderSubmit = () => {
    console.log('Order submitted:', tacoType, tacocantidad, tacopara_llevar);
    onClose();
  };

  const handleTacoTypeChange = (event) => {
    setTacoType(event.target.value);
  };
  const handleTacocantidadChange = (event) => {
    setTacocantidad(parseInt(event.target.value));
  };
  const handlepara_llevarChange = (event) => {
    setTacopara_llevar(event.target.checked);
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
          <label htmlFor="taco-cantidad">cantidad:</label>
          <input
            id="taco-cantidad"
            type="number"
            min="1"
            value={tacocantidad}
            onChange={handleTacocantidadChange}
          />
        </div>
        <div>
          <label htmlFor="taco-to-go">To go:</label>
          <input id="taco-to-go" type="checkbox" checked={tacopara_llevar} onChange={handlepara_llevarChange} />
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